#!/usr/bin/env python

# Online TLE update portions from  from stvid/update_tle.py
# https://github.com/cbassa/stvid/blob/master/update_tle.py
# TODO May need facility to access archived TLEs (at SpaceTrack) 
#      And something else for old McCants TLEs

from __future__ import print_function
from __future__ import division         # Eliminate need for decimals on whole values
import sys

if sys.version_info[0] != 3 or sys.version_info[1] < 6:
    print("This script requires Python version 3.6")
    sys.exit(1)

import re
import os
import configparser                 # config file parsing
import argparse                     # command line parsing
from hashlib import md5             # md5 finger printing
from shutil import copyfile
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
from datetime import date, timedelta, datetime
from time import time                               # For performance timing
from math import (degrees, pi, pow, radians, sqrt)  # Fast/precise math functions

import logging
log = logging.getLogger(__name__)

# import string
from getpass import getpass

from spacetrack import SpaceTrackClient
from skyfield.api import load
from sgp4.ext import jday

# The following 5 lines are necessary until our modules are public
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
database_path = os.path.join(parentdir, "sathunt-database")
sys.path.insert(1,database_path) 
import database

""" TODOs:
 - Implement option for "strict" or "loose" processing of element fields (i.e., allow use of non-compliant TLE formats)

    # Todo 
    # - FILEOP Look at how Brandon provided file-load progress
    # - FILEOP Look at how people typically store TLEs in array
    # - IMPORT Update TLE, fingprint, schemas
    # - QUERY Elements nearest to an EPOCH (greater than, less than, some error bounds)
    # - FILEOP XF6 Insert 42 character names into line 0 of TLE from reference file (mcnames)
    # - FILEOP XF7 Update a tle file from another TLE file
    # - FILEOP XF9 Filter out elements with "DEB" with a space before that string. 
    #    But tles with names containing SPELDA, SYLDA, TANK, DPAF, and COVER
    #    The leading 0 and space are removed from "line 0" of the spacecom 3 line tles.
    # - FILEOP XF10 The leading 0 and space are removed from "line 0"
    # - FILEOP XF11 Sort TLEs into ascending NCat order
    # - FILEOP geteccen Filter mean motion less than 8.0 and eccentricity greater than 0.1
    # - FILEOP getleo Filter mean motion is greater than 5.0
    # - FILEOP getepoch (output epoch of each elset) only an .exe
"""

def extract_zip_to_memory(input_zip):
    """Return contents of zip file(s) in memory"""

    input_zip = ZipFile(input_zip)
    return {name: input_zip.read(name) for name in input_zip.namelist()}

class Error(Exception):
   """Base class for other exceptions"""
   pass

class TLEValueError(Error):
    """Raised when TLEs fail checksum and parameter validity checks."""
    pass

def checksum_tle_line(_line):
    """ Performs TLE-defined checksum on TLE line"""

    check = 0
    for char in _line[:-1]:
        if char.isdigit():
            check += int(char)
        if char == "-":
            check += 1

    _check_val = check % 10

    return(_check_val)

def tle_fmt_epoch(EpochDateTime):
    """ Return an Epoch string in TLE format

    YYDDD.dddddddd where Midnight Jan 1 2019 is 19001.00000000
    """
    # (year, month, day, hour, minute, second, wday, yday, dst) = EpochDateTime.timetuple()
    # Get just the variables we need - to avoid lint errors for unused variables
    (hour, minute, second, _, yday) = EpochDateTime.timetuple()[3:8]
    yday = EpochDateTime.timetuple()[7]
    YY = EpochDateTime.strftime("%y")

    # Probably missing 1 digit of precision by dropping microseconds
    frac_days = (yday) + (((second / 3600) + (minute/60) + hour)/24)
    return "{:2s}{:012.8f}".format(YY,frac_days)


def fingerprint_file(file):
    """Open, read file and calculate MD5 on its contents"""
    with open(file,'rb') as fd:
        # read contents of the file
        _file_data = fd.read()    
        # pipe contents of the file through
        file_fingerprint = md5(_file_data).hexdigest()
    return file_fingerprint


def fingerprint_line(line):
    """ Creates a unique signature from a line."""
    return md5(line.encode('utf-8')).hexdigest()


def read_tle_decimal(pack):
    """Convert *pack* to decimal value."""
    if pack[0] in ["-", " ", "+"]:
        digits = pack[1:-2].strip()
        val = pack[0] + "." + digits + "e" + pack[-2:]
    else:
        digits = pack[:-2].strip()
        val = "." + digits + "e" + pack[-2:]
    return float(val)


def launch_letter_to_number(letters):
    """Convert 24 upper case letter 3-letter code to integer, omitting I (eye) and O (oh) from the alphabet.
    
    The TLE standard is 24 upper case letter 3-letter code, omitting I (eye) and O (oh) from the alphabet,
    with no representation for zero.
    
    The 1st piece of a launch is denoted by 'A', and subsequent pieces 'B', 'C', 'D'... 'Z'.
    The 25th (24*1 + 1) piece would be denoted by 'AA', and subsequent pieces 'AB', 'AC'... 'AZ', 'BA', BB', 'BC',... 'ZZ'.
    The 601st (24*24 + 24 + 1) piece would be denoted by 'AAA', and subsequent pieces, 'AAB', 'AAC'... AZZ', 'BAA', 'BAB'... 'ZZZ'
    This allows for a maximum of 24^3 + 24^2 + 24 pieces, or 14424 pieces for a single launch (ZZZ)
    """

    letters = letters.strip()

    # Omit I (eye) and O (oh)
    dictionary = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
    'J':9,'K':10,'L':11,'M':12,'N':13,'P':14,'Q':15,'R':16,'S':17,
    'T':18,'U':19,'V':20,'W':21,'X':22,'Y':23,'Z':24}

    base = len(dictionary)
    strlen = len(letters)

    if strlen == 1:
        number = dictionary[letters]
    elif strlen == 2:
        first_number = dictionary[letters[0]]
        second_number = dictionary[letters[1]]
        number = (first_number * base) + second_number
    elif strlen == 3:
        first_number = dictionary[letters[0]]
        second_number = dictionary[letters[1]]
        third_number = dictionary[letters[2]]
        number = (first_number * base * base) + (second_number * base) + third_number
    return number


def launch_piece_number_to_letter(piece_num):
    """ Converts UK/RDE format 2-digit launch piece to three-letter TLE standard, left-justified, space-padded.

    The TLE standard is 24 upper case letter 3-letter code, omitting I (eye) and O (oh) from the alphabet,
    with no representation for zero.
    
    The 1st piece of a launch is denoted by 'A', and subsequent pieces 'B', 'C', 'D'... 'Z'.
    The 25th (24*1 + 1) piece would be denoted by 'AA', and subsequent pieces 'AB', 'AC'... 'AZ', 'BA', BB', 'BC',... 'ZZ'.
    The 601st (24*24 + 24 + 1) piece would be denoted by 'AAA', and subsequent pieces, 'AAB', 'AAC'... AZZ', 'BAA', 'BAB'... 'ZZZ'
    This allows for a maximum of 24^3 + 24^2 + 24 pieces, or 14424 pieces for a single launch (ZZZ)
    """

    # Zero is not a valid result, so we should never use the zero index
    dictionary='!ABCDEFGHJKLMNPQRSTUVWXYZ'
    piece_letters=''
    
    # FIXME: Figure out what the right thing to do is if we're passed 0 (Assign to 1=A?)
    x = int(piece_num)
    if (x == 0):
        x = 1

    # 14424 = 24*24*24 + 24*24 + 24
    # Just rail it high to preserve the format width
    if x > 14424:
        x = 14424
        log.warning("Exceeded maximum value (14424) for launch piece number")

    while x>0:
        x,idx = divmod(x,24)
        # With no zero value, zero remainder means we are at the maximum value in the alphabet
        # Not the first of the next!
        if(idx==0):
            idx = 24
            x-=1
        piece_letters = dictionary[idx] + piece_letters			

    return "{:<s}".format(piece_letters)


# Note: Can't call it "Satellite" as that appears to interfere with Satellite class in python-skyfield
class Satellite_cal(object):
    """ Class for TLE data objects and methods

    Do everything you would need to parse and validate an individual TLE to
    prepare it for next steps.

    Special things:
    - tle_file_signature is to reference the parent of this TLE, 
    default is "orphan" unless overridden (e.g., by script-generated TLE)
    - checksum defaults to "flag" to reject TLEs that don't arrive with a valid checksum
    Setting it to anything else overrides the received checksum with the correct checksum.
    """

    # Calculations and constants we want to compute exactly once
    # User can over-ride these with different values if desired
    _XKMPER = 6378.137       # WGS84 Earth Equatorial Radius
    _GE     = 398600.4418    # Earth gravitational constant km3/s2
    _GEsqrt = sqrt(_GE)
    _XKE    = sqrt((3600.0 * _GE) / (pow(_XKMPER,3)))


    def __init__(self, catalog=None, line0=None, line1=None, line2=None, tle_source_filename=None, tle_file_fingerprint=None, strict=True, checksum="flag"):
        self._tle_file = tle_source_filename
        self.line0     = line0.rstrip()
        self.line1     = line1.rstrip()
        self.line2     = line2.rstrip()
        self.strict    = strict
        self.checksum  = checksum

        # Variables users would likely want regular access to
        self.sat_num = None
        self.classification = None  # Note: Set this to "O" (or some less ambiguous character) to indicate source?
        self.designation = None
        self.mean_motion_derivative = None          # TODO orbits_per day - and MKS versions
        self.mean_motion_sec_derivative = None      # TODO orbits_per day - and MKS versions
        self.bstar = None
        self.ephemeris_type = None
        self.element_num = None
        self.line1_checksum = None

        self.inclination_degrees = None
        self.raan_degrees = None
        self.eccentricity = None
        self.arg_perigee_degrees = None
        self.mean_anomaly_degrees = None    # revs / day
        self.mean_motion_orbits_per_day     = None
        self.orbit_num = None
        self.line2_checksum = None

        # Sourced from TLEs, but less useful directly
        self._id_launch_year = None
        self._id_launch_num = None
        self._id_launch_piece_letter = None
        self._epoch_year = None
        self._epoch_day = None

        # Derived quantities - MKS units
        self.inclination_radians = None
        self.raan_radians = None
        self.arg_perigee_radians = None
        self.mean_anomaly_radians = None
        self.mean_motion_radians_per_second = None

        # Derived quantities - other
        self.epoch = None
        self.epoch_string = None
        self.launch_piece_number = None
        self.tle_fingerprint = None
        self._tle_file_fingerprint = tle_file_fingerprint
        self._tle_source_filename = tle_source_filename
        self.analyst_object = None
        self.tle_good = None

        # Convenience variables
        _GEsqrt = Satellite_cal._GEsqrt
        _XKMPER = Satellite_cal._XKMPER
        self.name = self.line0

        # Step through TLE import process
        try:
            self._checksum_tle()
            self._parse_tle()
            self._validity_check_tle()
            self._fingerprint_tle()

            self.period = 2*pi/(self.mean_motion_radians_per_second)                            # In seconds
            self.semi_major_axis = pow(_GEsqrt / self.mean_motion_radians_per_second,2/3)  # in km
            self.perigee = self.semi_major_axis*(1 - self.eccentricity) - _XKMPER               # in km
            if(self.perigee < 0):
                log.warning("{}: Perigee {:0f} intersects the Earth.".format(self._tle_source_filename, self.perigee))

            self.apogee  = self.semi_major_axis*(1 + self.eccentricity) - _XKMPER               # in km

            # Add in the calculations for the non SGP4 things here...

        except TLEValueError:
            log.warning("{}: Encountered errors in processing the following TLE block:\t{}\n\t{}\n\t{}".format(self._tle_source_filename, self.line0,self.line1,self.line2))


    def _parse_tle(self):
        """Parse fields in TLE data"""

        # Parse line 0
        self.name_long = self.line0[0:24].rstrip()

        # Parse line 1
        try:
            self.sat_num = int(self.line1[2:7])
        except ValueError:
            log.warning("{}: TLE Sat # NaN for {}".format(self._tle_source_filename, self.name_long))
            self.tle_good = False
 
        self.classification  = self.line1[7]

        self._id_launch_year         = self.line1[ 9:11]
        self._id_launch_num          = self.line1[11:14]
        self._id_launch_piece_letter = self.line1[14:17].strip()

        if (80000 <= self.sat_num <= 89999):
            # Analyst object
            self.designation = self.line1[ 9:17].rstrip()
            self.analyst_object = True

            # It's probably the case that analyst objects don't have this detail defined
            # Doublecheck with T.S. Kelso
            self._id_launch_year = None
            self._id_launch_num = None
            self._id_launch_piece_letter = None
        elif (not self._id_launch_year.isspace() and not self._id_launch_num.isspace() and not self._id_launch_piece_letter.isspace()):
            try:
                self._id_launch_year  = int(self._id_launch_year)
                if (self._id_launch_year >= 57):
                    self._id_launch_year = 1900 + self._id_launch_year
                elif (self._id_launch_year < 57):
                    self._id_launch_year = 2000 + self._id_launch_year
            except ValueError:
                log.warning("{}: TLE Launch year NaN for {}".format(self._tle_source_filename, self.sat_num))
                if(self.strict):
                    self.tle_good = False

            try:
                self._id_launch_num   = int(self._id_launch_num)
            except ValueError:
                log.warning("{}: TLE Launch number NaN for {}".format(self._tle_source_filename, self.sat_num))
                if(self.strict):
                    self.tle_good = False

            else:
                try: 
                    assert self._id_launch_piece_letter.isupper() == True
                    assert self._id_launch_piece_letter.find('I') < 0
                    assert self._id_launch_piece_letter.find('O') < 0
                    self.launch_piece_number = launch_letter_to_number(self._id_launch_piece_letter)                                                            
                except AssertionError: 
                    # This is a real error (and not an analyst object) if we're this far...
                    log.warning("{}: TLE invalid characters in launch piece field\n\t{}".format(self._tle_source_filename, self.line1))
                    if(self.strict):
                        self.tle_good = False

                try:
                    self.designation = "{:4d}-{:>03d}{:<3s}".format(self._id_launch_year,
                                                                    self._id_launch_num,
                                                                    self._id_launch_piece_letter)
                except (ValueError):
                    if(self.strict):
                        self.tle_good = False
                    else:
                        self.designation = self.line1[ 9:17].rstrip()
        else:
            log.warning("{}: Non-analyst object {} with no valid launch info.".format(self._tle_source_filename, self.sat_num))

        self._epoch_year      = int(self.line1[18:20])
        if (self._epoch_year >= 57):
            self._epoch_year = 1900 + self._epoch_year
        elif (self._epoch_year < 57):
            self._epoch_year = 2000 + self._epoch_year

        self._epoch_day       = float(self.line1[20:32])
        self.epoch = datetime(self._epoch_year, 1, 1, 0, 0, 0, 0) + timedelta(days = (self._epoch_day - 1) )
        # self.epoch_string = self.epoch.strftime("%Y-%m-%d %H:%M:%S.%f")
        self.epoch_string = self.epoch.isoformat()

        (year, monnth, day, hour, minute, second) = self.epoch.timetuple()[:6]

        self.jdsatepoch = jday(year, monnth, day, hour, minute, second)
        self.jdSGP4epoch = self.jdsatepoch - 2433281.5

        self.mean_motion_derivative     = float(self.line1[33:43])
        self.mean_motion_sec_derivative = read_tle_decimal(self.line1[44:52])
        self.bstar                      = read_tle_decimal(self.line1[53:61])

        try:
            self.ephemeris_type = int(self.line1[62])
        except ValueError:
            self.ephemeris_type = 0
        self.element_num  = int(self.line1[64:68])

        # Parse line 2
        # Figure out where to do the error / type checking on these
        self.inclination_degrees  = float(self.line2[ 8:16])
        self.inclination_radians = radians(self.inclination_degrees)

        self.raan_degrees         = float(self.line2[17:25])
        self.raan_radians         = radians(self.raan_degrees)

        self.eccentricity =   int(self.line2[26:33]) * 10 ** -7

        self.arg_perigee_degrees  = float(self.line2[34:42])
        self.arg_perigee_radians  = radians(self.arg_perigee_degrees)

        self.mean_anomaly_degrees = float(self.line2[43:51])
        self.mean_anomaly_radians = radians(self.mean_anomaly_degrees)
        
        self.mean_motion_orbits_per_day  = float(self.line2[52:63])
        self.mean_motion_radians_per_second = 2 * pi * self.mean_motion_orbits_per_day / 86400

        xpdotp   =  1440.0 / (2.0 *pi)  #  229.1831180523293
        self.mean_motion_radians_per_minute = self.mean_motion_orbits_per_day / xpdotp 

        self.orbit_num =   int(self.line2[63:68])

        # Create a tuple convenient for handing to python-SGP4 satrec variable
        # SGP expecting:
        #  Angles in radians
        #  Angle rates in radians per minute 
        #  epoch time in days from jan 0, 1950. 0 hr
        self.satrec = [self.sat_num, self.jdSGP4epoch, self.bstar, self.eccentricity, 
                       self.arg_perigee_radians, self.inclination_radians, self.mean_anomaly_radians, 
                       self.mean_motion_radians_per_minute, self.raan_radians]


    def _checksum_tle(self):
        """ Performs TLE-defined checksum on TLE """

        _check_val = [None, None, None]
        _linenum = 1

        for _line in [self.line1, self.line2]:
            _check_val[_linenum] = checksum_tle_line(_line)

            if (_check_val[_linenum] != int(_line[-1])) and (self.checksum!="fix"):
                log.warning("{}: TLEChecksumError: {}".format(self._tle_source_filename, _line))
                self.tle_good = False
            elif (_line == 1):
                self.line1_checksum = _check_val[_line]
            elif (_line == 2):
                self.line2_checksum = _check_val[_line]
            _linenum += 1   


    def _validity_check_tle(self):
        """ Perform format and range-checking tests described at: https://celestrak.com/columns/v04n03/"""
        # TODO: Make sure the line1 object number matches the line2 object number 
        _thisyear = date.today().year
        _validity_errors = {}
        if (not (0 <= self.raan_degrees < 360)):
             _validity_errors["RAAN_degrees"] = self.raan_degrees
        if (not (0 <= self.arg_perigee_degrees < 360)):
             _validity_errors["arg_perigee_degrees"] = self.arg_perigee_degrees
        if (not (0 <= self.mean_anomaly_degrees < 360)):
             _validity_errors["mean_anomaly_degrees"] = self.mean_anomaly_degrees
        if (not (0 <= self.inclination_degrees < 180)):
             _validity_errors["inclination_degrees"] = self.inclination_degrees
        if (not (0 <= self.eccentricity < 1)):
             _validity_errors["eccentricity"] = self.eccentricity
            # Might need some allowance for future epochs here

        # TODO Determine a reasonable date in the future to check against epoch
        if (not (datetime(1957,10,4,0,0,0,0) <= self.epoch )):
             _validity_errors["epoch"] = self.epoch

        # Launch year might be None or string
        try:
            if (not (date(1957,1,1) <= date(self._id_launch_year,1,1) <= date.today() )):
                _validity_errors["launch_year"] = self._id_launch_year
        except TypeError:
            pass    # Should only be None types

        if (not (0 <= self.ephemeris_type <= 5)):
             _validity_errors["ephemeris_type"] = self.ephemeris_type
        if (len(_validity_errors) == 0):
            self.tle_good = True
        else: # 
            log.warning("{}: TLE failed validity error for sat_num {} ({})".format(self._tle_source_filename, self.sat_num,_validity_errors))
            log.info("  {}\n  {}\n  {}".format(self.line0,self.line1,self.line2))
            self.tle_good = False


    def _fingerprint_tle(self):
        """ Creates a unique signature from a TLE.
        
        Incorporates those parts of the TLE that contribute to the orbit properties."""

        _line1fragment = self.line1[19:64] # Epoch year through Ephemeris type
        _line2fragment = self.line2[9:64]  # Inclination through Mean Motion

        _TLE_fingerprint_string = self.line1 + self.line2
                    
        self.tle_fingerprint = md5(_TLE_fingerprint_string.encode('utf-8')).hexdigest()


class TLEFile(object):
    """TLEFile: Class for TLE file operations
    
        Returns an Dict of TLE objects with NORAD id as KEY
    """


    def __init__(self, tle_file, strict=True, parse=True):
        self.tle_file = tle_file
        self._tle_fd = None                 # TLE file descriptor
        self.tle_file_fingerprint = None
        self._TLEs = []
        self.strict = strict
        self.parse = parse
        self._tle_basename = os.path.basename(self.tle_file)
        self.Satellites = {}

        if (strict):
            # FROM: https://www.orekit.org/static/jacoco/org.orekit.propagation.analytical.tle/TLE.java.html
            self._tle_line1_re = re.compile ('^1 [ 0-9]{5}[A-Z] [ 0-9]{5}[ A-Z]{3} [ 0-9]{5}[.][ 0-9]{8} (?:(?:[ 0+-][.][ 0-9]{8})|(?: [ +-][.][ 0-9]{7})) [ +-][ 0-9]{5}[+-][ 0-9] [ +-][ 0-9]{5}[+-][ 0-9] [ 0-9] [ 0-9]{4}[ 0-9]')
            self._tle_line2_re = re.compile ('^2 [ 0-9]{5} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{7} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{2}[.][ 0-9]{13}[ 0-9]')
        else:
            self._tle_line1_re = re.compile ('^1 ')
            self._tle_line2_re = re.compile ('^2 ')

        self.load_tles()

        if (parse):
            self.parse_tles()


    def fingerprint_file(self):
        """Open, read file and calculate MD5 on its contents"""
        with open(self.tle_file,'rb') as fd:
            # read contents of the file
            _file_data = fd.read()    
            # pipe contents of the file through
            self.file_fingerprint = md5(_file_data).hexdigest()
        return self.file_fingerprint


    def load_tles(self):
        """Read TLE data.
        
        Perform an MD5 checksum of the source file, and store with the Class variables.
        """

        def _line012(_l0, _l1, _l2):
            """Mini routine to format the TLE set"""
            _l0 = _l0.rstrip()
            if _l0.startswith('0 '): # Spacetrack 3-line format
                name = _l0[2:].rstrip()
            else:
                name = _l0.rstrip()
            return(name, _l1.rstrip(), _l2.rstrip())

        if not (self.tle_file_fingerprint):
            self.fingerprint_file()

        l0 = l1 = ""
        tlecount = 0
        tlefileline = 0 
        with open(self.tle_file,'r') as tlefd:
            for l2 in tlefd:
                l2 = l2.rstrip()
                tlefileline += 1

                simplematch1 = (l1.startswith('1 ') and len(l1) >= 69)
                simplematch2 = (l2.startswith('2 ') and len(l2) >= 69)

                match1 = self._tle_line1_re.search(l1)                    
                match2 = self._tle_line2_re.search(l2)

                if (match1 and match2 and self.strict):
                    (name, line1, line2) = _line012(l0, l1, l2)
                    tlecount += 1
                    self._TLEs.append([name,line1,line2])
                elif ((simplematch1 and simplematch2) and not self.strict):
                    (name, line1, line2) = _line012(l0, l1, l2)
                    tlecount += 1
                    self._TLEs.append([name,line1,line2])
                elif ( (self.strict and simplematch1 and simplematch2) and (match1==None or match2==None)):
                    if not (match1 or match2):
                        log.warning("{}: Strict record structure checks failed for both TLE lines at file line: {}".format(self._tle_basename,tlefileline))
                        log.info("  {}\n  {}\n  {}\n".format(l0,l1,l2))
                    elif not match1:
                        log.warning("{}: Strict record structure checks failed for TLE line 1 at file line {}".format(self._tle_basename,tlefileline))
                        log.info("  {}\n  {}\n  {}\n".format(l0,l1,l2))
                    elif not match2:
                        log.warning("{}: Strict record structure checks failed for TLE line 2 at file line {}".format(self._tle_basename,tlefileline))
                        log.info("  {}\n  {}\n  {}\n".format(l0,l1,l2))
                    else:
                        log.warning("{}: Should not be here.".format(self._tle_basename))

                l0 = l1
                l1 = l2
        log.info("Read {} TLEs".format(tlecount))


    def parse_tles(self):
        log.info("Parsing...")
        for (line0, line1, line2) in self._TLEs:
            sat = Satellite_cal(line0=line0, 
                            line1=line1, 
                            line2=line2, 
                            tle_file_fingerprint=self.tle_file_fingerprint,
                            tle_source_filename=self._tle_basename)
            self.Satellites[sat.sat_num] = sat
        return self.Satellites


def assumed_decimal_point(num_less_than_one, digits=7):
    """ Return a string with DIGITS of precision, with the decimal point removed """
    string_num = "{0:.{DIGITS}f}".format(num_less_than_one,DIGITS=digits)
    return(string_num[2:])


def make_tle(*, name="None", ssn, desig="0000000", epoch_datetime, xincl, xnodeo, eo, omegao, xmo, xno, deg=True, quiet=False):
    """ write TLE to output file and to screen """

    # ssn               Spacecraft number
    # desig             International Designation
    # epoch_datetime    Epoch in pythonDATETIME format
    # xincl             inclination
    # xnodeo            RAAN
    # eo                eccentricity
    # omegao            argument of perigee
    # xmo               mean anomaly
    # xno               mean motion
    # TODO: Find standard variable names for First Derivative xno, Second derivative xno, Bstar

    line0 = None
    tle_epoch = tle_fmt_epoch(epoch_datetime)
    eo_string = assumed_decimal_point(eo,7)

    if (deg==False):
        xincl  = degrees(xincl)
        xnodeo = degrees(xnodeo)
        omegao = degrees(omegao)
        xmo    = degrees(xmo)

    # //   sprintf(bstar_string, "%12.4e", bstar*10);
    # //   bstar_fract[0] = bstar_string[0]; // sign
    # //   bstar_fract[1] = bstar_string[1];
    # //   bstar_fract[2] = bstar_string[3];
    # //   bstar_fract[3] = bstar_string[4];
    # //   bstar_fract[4] = bstar_string[5];
    # //   bstar_fract[5] = bstar_string[6];
    # //   bstar_fract[6] = '\0';
    # //   bstar_exp[0] = bstar_string[8];
    # //   bstar_exp[1] = bstar_string[11];
    # //   bstar_exp[2] = '\0';

    # //   double xns = 2160 * bstar * nn * c2;

    # //   sprintf(line1, "1 %05dU %-8s %014.8f %.8f  00000-0 %6s%2s 0    00"
    # //            ,ssn, desig, tle, xns, bstar_fract, bstar_exp);

    if name:
        line0  = "{:24s}".format(name) 
        if not quiet:
            print("{:s}".format(line0))

    line1 = "1 {:5d}U {:<8s} {:14s} 0.00000073  00000-0  50000-4 0    00".format(ssn,desig,tle_epoch)
    # TODO: Deal with First Derivative xno, Second derivative xno, Bstar
    line2 = "2 {:05d} {:8.4f} {:8.4f} {:7s} {:8.4f} {:8.4f} {:11.8f}    00".format(
            ssn, xincl, xnodeo, eo_string, omegao, xmo, xno)

    line1 = line1[:68] + str(checksum_tle_line(line1))
    line2 = line2[:68] + str(checksum_tle_line(line2))

    if not quiet:
        print("{:s}".format(line1))
        print("{:s}".format(line2))
    return(line0, line1, line2)


def append_tle_file(file_out, line0, line1, line2):
    try:
        with open(file_out, "a") as fp:
            fp.write("\n")
            if(line0):
                fp.write("{:s}\n".format(line0))
            fp.write("{:s}\n".format(line1))
            fp.write("{:s}\n".format(line2))
            fp.close()
    except IOError:
        log.warning("Can not open file: {}".format(file_out))    


def update_from_online(tle_path):
    log.info("Updataing TLEs in {}".format(tle_path))

    now = datetime.datetime.utcnow()
    time = now.strftime("%Y%m%d_%H%M%S")

    # Get Space Track TLEs
    catalog_tle = os.path.join(tle_path, 'catalog.tle')
    st = SpaceTrackClient(identity=cfg.get('Credentials', 'st-username'),
                        password=cfg.get('Credentials', 'st-password'))

    data = st.tle_latest(iter_lines=True, epoch='>now-30',
                        ordinal=1, format='3le')

    with open(catalog_tle, 'w') as fp:
        for line in data:
            # Fix missing leading zeros
            line = re.sub("^1     ", "1 0000", line)
            line = re.sub("^2     ", "2 0000", line)
            line = re.sub("^1    ", "1 000", line)
            line = re.sub("^2    ", "2 000", line)
            line = re.sub("^1   ", "1 00", line)
            line = re.sub("^2   ", "2 00", line)
            line = re.sub("^1  ", "1 0", line)
            line = re.sub("^2  ", "2 0", line)
            fp.write(line + '\n')

    copyfile(catalog_tle, os.path.join(tle_path, time + '_catalog.txt'))

    # Get classified TLEs
    resp = urlopen("http://www.prismnet.com/~mmccants/tles/classfd.zip")
    zipfile = ZipFile(BytesIO(resp.read()))
    zipfile.extractall(path=tle_path)
    classfd_tle = os.path.join(tle_path, 'classfd.tle')

    content = None
    outsize = 0
    with open(classfd_tle, 'rb') as infile:
        content = infile.read()
    with open(classfd_tle, 'wb') as output:
        for line in content.splitlines():
            outsize += len(line) + 1
            output.write(line + b'\n')

    copyfile(classfd_tle, os.path.join(tle_path, time + '_classfd.txt'))

    # Get int TLEs
    resp = urlopen("http://www.prismnet.com/~mmccants/tles/inttles.zip")
    zipfile = ZipFile(BytesIO(resp.read()))
    zipfile.extractall(path=tle_path)
    int_tle = os.path.join(tle_path, 'inttles.tle')

    content = None
    outsize = 0
    with open(int_tle, 'rb') as infile:
        content = infile.read()
    with open(int_tle, 'wb') as output:
        for line in content.splitlines():
            outsize += len(line) + 1
            output.write(line + b'\n')

    copyfile(int_tle, os.path.join(tle_path, time + '_inttles.txt'))

    # Create bulk catalog
    catalogs = [catalog_tle, classfd_tle]
    with open(os.path.join(tle_path, 'bulk.tle'), 'w') as outfile:
        for fname in catalogs:
            with open(fname) as infile:
                outfile.write(infile.read())


# Main
def main():
    t0 = time()
    # Read commandline options
    conf_parser = argparse.ArgumentParser(description='Collection of utilities' +
                                                      ' to manage TLEs')
    conf_parser.add_argument("-c", "--conf_file",
                             help="Specify configuration file. [Default configuration.ini]",
                             dest='conf_file',
                             nargs='?',
                             const=1,
                             default='configuration.ini',
                             type=str,
                             metavar="FILE")
    conf_parser.add_argument("-f", "--tle",
                             help="Specify TLE file. [Default bulk.tle]",
                             dest='tle_file',
                             nargs='?',
                             type=str,
                             metavar="FILE")
    conf_parser.add_argument("--tlepath",
                             help="Specify TLE path. [Default ./tle]",
                             dest='tle_path',
                             nargs='?',
                             type=str,
                             metavar="PATH")
    conf_parser.add_argument("--update", help="update TLEs from online sources",
                             action="store_true")
    conf_parser.add_argument("-dbname", "--database", 
                             help="database to USE",
                             dest='dbname',
                             default='opensatcat_dev',                           
                             nargs='?',
                             const=1,                             
                             type=str,                             
                             metavar="NAME")
    conf_parser.add_argument("-H", "--hostname", 
                             help="database hostname",
                             dest='dbhostname',
                             default='opensatcat.cvpypmmxjtv1.us-east-2.rds.amazonaws.com',
                             nargs='?',
                             const=1,
                             type=str,                             
                             metavar="HOSTNAME")
    conf_parser.add_argument("-u", "--user", 
                             help="database user name",
                             dest='dbusername',
                             nargs='?',
                             type=str,                             
                             metavar="USER")
    conf_parser.add_argument("-p", "--password", 
                             help="database user password",
                             dest='dbpassword',
                             nargs='?',
                             type=str,                             
                             metavar="PASSWD")
    conf_parser.add_argument("-t", "--dbtype", 
                             help="database type [INFILE, sqlserver, sqlite] \
                                   default: INFILE",
                             dest='dbtype',
                             nargs='?',
                             choices=['INFILE', 'sqlserver', 'sqlite'],
                             default='INFILE',
                             type=str,                             
                             metavar="TYPE")
    conf_parser.add_argument("-i", "--import", help="Import TLEs to database",
                             dest='importTLE',
                             action="store_true")
    conf_parser.add_argument("-q", "--quiet", help="Suppress console output",
                             dest='quiet',
                             action="store_true")
    conf_parser.add_argument("-V", "--verbose", 
                             help="increase verbosity: 0 = only warnings, 1 = info, 2 = debug. No number means info. Default is no verbosity.",
                             const=1, 
                             default=0, 
                             type=int, 
                             nargs="?")

    # Command to upload McCants files from DIR
    # python ./tle_util.py --import --dbtype sqlserver --user chris.lewicki --tlepath /Users/chris/Dropbox/code/preMVP/tle/mccants_archive

    # Process commandline options and parse configuration
    cfg = configparser.ConfigParser(inline_comment_prefixes=('#', ';'))
    args = conf_parser.parse_args()
    log = logging.getLogger()

    # make it print to the console.
    console = logging.StreamHandler()
    log.addHandler(console)

    conf_file = args.conf_file
    tle_file = args.tle_file
    tle_path = args.tle_path
    update = args.update
    dbname = args.dbname
    dbhostname = args.dbhostname
    dbusername = args.dbusername
    dbpassword = args.dbpassword
    dbtype = args.dbtype
    importTLE = args.importTLE
    verbose = args.verbose
    quiet = args.quiet

    if (quiet == False):
        if verbose == 0:
            log.setLevel(logging.WARN) 
        elif verbose == 1:
            log.setLevel(logging.INFO) 
        elif verbose == 2:
            log.setLevel(logging.DEBUG) 
        log.debug("Log level set to {}".format(log.level))

    if verbose:
        for arg in vars(args):
            log.debug("%s : %s",arg, getattr(args, arg))

    cfg.read([args.conf_file])
    log.info("Reading config from: {}".format(args.conf_file))

    if not (tle_path):
        try:
            tle_path = cfg.get('Common', 'tle_path')
        except KeyError:
            tle_path = "./"

    if not (tle_file):
        tle_file = os.path.join(tle_path,"bulk.tle")
    else:
        tle_file = os.path.join(tle_path,tle_file)


    if update:
        update_from_online(tle_path)

    if (importTLE):
        if (dbtype == "sqlserver"):
            if dbusername == None:
                try: 
                    dbusername = input("Username: ") 
                except Exception as error: 
                    log.warning("ERROR: password must be specified {}".format(error)) 
            if dbpassword == None:
                try: 
                    dbpassword = getpass() 
                except Exception as error: 
                    log.warning("ERROR: password must be specified {}".format(error))

        # Set up database connection or files
        db = database.Database(dbname,dbtype,dbhostname,dbusername,dbpassword)
        # TODO: Probably need an error check to ensure this was set up correctly
        if (dbtype != "INFILE"):
            try:
                db.createTLETables()
            except:
                log.warning("Tables already exist or there is a big problem buddy.")



    # Main processing loop
    t1 = time()
    log.debug(t1-t0)

    # Initialize variables we want fresh for the processing loop
    existing_files = {} # A rolling list of users that have already had addresses assigned
    TLETotalCount = 0
    runningFileCount = 0
    runningUserCount = 0

    # Traverse the directory
    # FIXME: Make this deal gracefully with a non-existent directory
    totalFileCount = sum([len(fileList) for dirName, subdirList, fileList in os.walk(tle_path)])
    totalDirCount = sum(os.path.isdir(os.path.join(tle_path, i)) for i in os.listdir(tle_path)) 

    if (quiet == False):
        print("Processing {} files in {}...".format(totalFileCount,tle_path))

    for dirName, subdirList, fileList in os.walk(tle_path):
        subdirList.sort()
        # Go through individual files from the subdirectories
        dirfileTotal = len(fileList)
        dirfileCount = 0
        for fname in sorted(fileList):
            time_start = time()
            dirfileCount += 1
            if("DS_Store" in fname):
                continue
            _file = os.path.join(dirName,fname)
            log.info("\nReading TLEs from {}".format(_file))
            TLEs = TLEFile(_file)

            # In theory, we could md5 the file directly *before* reading the TLE, but it really doesn't save much.
            # And we'd still want to check in the class, so we'd be doubling-up the MD5 checks.
            tle_file_fingerprint_array = db.selectTLEFile(TLEs.file_fingerprint)

            if(tle_file_fingerprint_array):     
                log.warning("Skipping {} TLEs in file: {} - fingerprint {} already in database.".format(len(TLEs.Satellites), fname, TLEs.file_fingerprint))   
                continue # Already have the file
            else:
                print("Processing file {}...".format(fname))
                for sat_num in TLEs.Satellites:
                    Sat = TLEs.Satellites[sat_num]

                    tle_fingerprint_array = db.selectTLEFingerprint(Sat.tle_fingerprint)
                    if(tle_fingerprint_array):     
                        log.warning("Skipping TLE in file: {} for sat {} - fingerprint {} already in database.".format(fname, sat_num, Sat.tle_fingerprint))   
                        continue # Already have the TLE
                    else:
                        result = db.addTLE(Sat)

                TLETotalCount += len(TLEs.Satellites)

                # Make note of file if it contained valid TLEs
                if (len(TLEs.Satellites) > 0):
                    result = db.addTLEFile(TLEs)

                # Commit the writes after we're done with the file.
                # We might also want to do this every maximum number of elements (i.e. 1000)    
                db.commit_TLE_db_writes()

            # Check to see if the file is in the DB or local file
            # But defer the database interaction until we have a need to post an observation
            # tle_file_fingerprint_array = db.selectTLEFILE(TLEs.tle_file_fingerprint)

                # if id_array:
                #     sender_id = id_array[0]
                # else:
                #     # Note that this is creating users who may have not submitted an observation
                #     acct = Account.create('password123')
                #     sender_id = db.addObserver(acct.address, sender, 0, first_line)
                #     log.debug("Creating account {} for Sender (ID)".format(acct.address,sender,sender_id))
                #     runningUserCount += 1
                # '''try:
                #     sender_id = existing_users[sender]
                # # If the user is new and does not have
                # except:
                #     acct = Account.create('password123')
                #     existing_users[sender] = acct.address'''
                # log.debug(" Sender (ID): {} ({})".format(sender,sender_id))

                # obsid = db.addParsedIOD(IOD_line, sender_id)
                # log.debug(" {} {} ({}) {}".format(obsid,sender,sender_id, IOD_line.line))

            # for sat_num in TLEs.Satellites:
            #     Sat = TLEs.Satellites[sat_num]

            # log.info("Imported {} TLE records.".format(len(TLEs.Satellites)))
            # log.info("Fingerprint of {} is {}".format(tle_file,TLEs.tle_file_fingerprint))
    if (not quiet):
        print("Imported {} TLEs from {} files in {} directories.".format(TLETotalCount,totalFileCount,totalDirCount))

    t2 = time()
    log.debug(t2-t1)

if (__name__ == '__main__'):
    main()