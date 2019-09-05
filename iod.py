#!/usr/bin/env python3
# Found code that also does all this (a little more complete)
# https://github.com/aerospaceresearch/orbitdeterminator/blob/866e5c031d5b1d836061d6ec2b105b8961c657d8/orbitdeterminator/satobs.py
import sys

if sys.version_info[0] != 3 or sys.version_info[1] < 7:
	print("This script requires Python version 3.7")
	sys.exit(1)

import os
import re
from datetime import datetime
from tle_util import launch_piece_number_to_letter

import logging
log = logging.getLogger(__name__)

# FIXME: Confirm I can remove this before R1 is done
# A hack to provide user and station data for the test IOD data before we're done with coding parsing
Stations = {
	2007 : {
		'user'        : 'IOD Test User',
		'name'		  : 'Test Station',
		'lattitude'   : '0',
		'longitude'   : '0',
		'altitude'    : '0',
		'frame'		  : 'WGS84',
		'description' : 'Something so that the IOD examples do not break',
		'notes'		  : ''
		},
	4172 : {
		'user'        : 'Leo Barhorst',
		'name'		  : 'ALMERE',
		'lattitude'   : '52.3713 N',
		'longitude'   : '5.2580 E',
		'altitude'    : '–3 ASL',
		'frame'		  : 'WGS84',
		'description' : 'Setup: WATEC 910HX/RC, 50 mm F1:1.8, NTP, Celestron Nexstar',
		'notes'		  : 'Observations made and reduced with Sattools'
		},
	4353 : {
		'user'        : 'Marco Langbroek',
		'name'		  : 'Leiden',
		'lattitude'   : '52.15412 N',
		'longitude'   : '4.49081 E',
		'altitude'    : '+0 m ASL',
		'frame'		  : 'WGS84',
		'description' : 'New Camera: Canon 80D',
		'notes'		  : 'http://sattrackcam.blogspot.com'
		},
	4355 : {
		'user'        : 'Marco Langbroek',
		'name'		  : 'Cronesteyn',
		'lattitude'   : '52.13878 N',
		'longitude'   : '4.49937 E',
		'altitude'    : '-2 m ASL',
		'frame'		  : 'WGS84',
		'description' : 'unknown',
		'notes'		  : 'http://sattrackcam.blogspot.com'
		},
	7778 : {
		'user'        : 'Brad Young',
		'name'		  : 'Remote MPC Q62 - Siding Spring, NSW, Australia',
		'lattitude'   : '-31.2733',
		'longitude'   : '149.0644',
		'altitude'    : '3400ft',
		'frame'		  : 'unknown',
		'description' : 'unknown',
		'notes'		  : '22" f/4.2 UC Obsession'
		},
	8336 : {
		'user'        : 'Brad Young',
		'name'		  : 'TULSA1',
		'lattitude'   : '-31.2733',
		'longitude'   : '-95.983429',
		'altitude'    : '201m',
		'frame'		  : 'unknown',
		'description' : 'unknown',
		'notes'		  : 'Meade ETX-125'
		},
	4541 : {
		'user'        : 'Alberto Rango',
		'name'		  : 'Roma',
		'lattitude'   : '',
		'longitude'   : '',
		'altitude'    : '',
		'frame'		  : '',
		'description' : '',
		'notes'		  : ''
		}
}


# REGEXP for valid angle string format with content
angle_content_re = re.compile('\d{1,7}\s*[+-]\d{1,7}') # pylint: disable=anomalous-backslash-in-string

# TODO: Angle - Make python unittest for this
# TODO: Angle - Convert RA/DEC to AZ/EL and reverse (from David Vallado code)
class Angle:
	"""Observed Angle

	# IOD - First four are OWTG system, minus one digit of precision
	#                    00000000001111
	#                    01234567890123
	# Format 1: RA/DEC = HHMMSSs+DDMMSS MX   (MX in seconds of arc)
	# 		 2: RA/DEC = HHMMmmm+DDMMmm MX   (MX in minutes of arc)
	# 		 3: RA/DEC = HHMMmmm+DDdddd MX   (MX in degrees of arc)
	# 		 4: AZ/EL  = DDDMMSS+DDMMSS MX   (MX in seconds of arc)
	# 		 5: AZ/EL  = DDDMMmm+DDMMmm MX   (MX in minutes of arc)
	# 		 6: AZ/EL  = DDDdddd+DDdddd MX   (MX in degrees of arc)
	# 		 7: RA/DEC = HHMMSSs+DDdddd MX   (MX in degrees of arc)

	# UK (RDE uses Code 1 with no sub-seconds)	
	#  		      Column 0000000000111111
	# 				     0123456789012345
	#   Code 1: RA/DEC = HHMMSSss+DDMMSSs
	# 	     2: RA/DEC = HHMMmmmm+DDMMmmm
	# 	     3: RA/DEC = HHMMmmmm+DDddddd
	# 	     4: AZ/EL  = DDDMMSSs DDMMSSs (elevation corrected for refraction)
	# 	     5: AZ/EL  = DDDMMmmm DDMMmmm (elevation corrected for refraction)
	# 	     6: AZ/EL  = DDDddddd DDddddd (elevation corrected for refraction)
	# 	     7: AZ/EL  = DDDMMSSs DDMMSSs (elevation not corrected for refraction)
	# 	     8: AZ/EL  = DDDMMmmm DDMMmmm (elevation not corrected for refraction)
	# 	     9: AZ/EL  = DDDddddd DDddddd (elevation not corrected for refraction)

	# TODO: Figure out what to do about elevation / refraction

	   Given a packed Angle string of two angle pairs matching the format above,
	   create one of the following formats.
	   RA =   HH.ddddd
	   DEC = DDD.ddddd

	   AZ =  DDD.ddddd
	   EL =   DD.ddddd

	   Where MX (Uncertainty) is not in degrees of arc, convert to degrees of arc

	The IOD and UK angle codes (1-6) are functionaly equivalent,
	noting the difference in precision.

	IOD Format 7 is unique to it.

	UK Formats 7-9 are identical in formatting to 4-6, noting the 
	considerations for atmospheric refraction.

	RDE Format 1 is the same as IOD/UK format without the sub-seconds
	"""

	def __init__(self,AngleFormatCode,EpochCode,Angle1,Angle2,Uncertainty,UncertaintyString,RecordFormat="IOD"):
		self.AngleFormatCode = AngleFormatCode
		self.EpochCode = EpochCode
		self.Epoch = None
		self.Angle1 = Angle1
		self.Angle2 = Angle2
		self.Uncertainty = Uncertainty
		self.UncertaintyString = UncertaintyString
		self.RA = 0.0
		self.DEC = 0.0
		self.AZ = 0.0
		self.EL = 0.0
		self.RecordFormat = RecordFormat

		EpochDict = {
			0 : 0,		# TODO: of Date (need to implement this somewhere)
			1 : 1855,
			2 : 1875,
			3 : 1900,
			4 : 1950,
			5 : 2000,
			6 : 2050
		}

		self.Epoch = EpochDict[self.EpochCode]

		# 1: RA/DEC = HHMMSSs+DDMMSS MX   (MX in seconds of arc)
		if(self.AngleFormatCode == 1):
			try:
				RA_HH = int(self.Angle1[0:2])
			except ValueError:
				RA_HH = 0 # We should probably just declare it invalid...

			try:
				RA_MM = int(self.Angle1[2:4])
			except ValueError:
				RA_MM = 0

			try:
				RA_SS = int(self.Angle1[4:6])
			except ValueError:
				RA_SS = 0

			try:
				RA_s = int(self.Angle1[6])
			except ValueError:
				RA_s = 0

			self.RA = (360.0*RA_HH/24.0) + RA_MM/60.0 + RA_SS / 3600.0 + RA_s*(0.1/3600.0)

			DEC_SIGN = self.Angle2[0]
			DEC_SIGN = int(DEC_SIGN + "1") # This operation doesn't appear strictly necessary

			try:
				DEC_DD = int(self.Angle2[1:3])
			except ValueError:
				DEC_DD = 0 # We should probably just declare it invalid...

			try:
				DEC_MM = int(self.Angle2[3:5])
			except ValueError:
				DEC_MM = 0

			try:
				DEC_SS = int(self.Angle2[5:7])
			except ValueError:
				DEC_SS = 0

			self.DEC  = DEC_DD + DEC_MM/60.0 + DEC_SS / 3600.0
			self.DEC *= DEC_SIGN

			# Convert uncertainty in seconds of arc to fractional degrees
			self.Uncertainty *= (1/3600)

		# 2: RA/DEC = HHMMmmm+DDMMmm MX   (MX in minutes of arc)
		elif(self.AngleFormatCode == 2):
			try:
				RA_HH = int(self.Angle1[0:2])
			except ValueError:
				RA_HH = 0 # We should probably just declare it invalid...

			try:
				RA_MM = int(self.Angle1[2:4])
			except ValueError:
				RA_MM = 0

			try:
				RA_mm_d1 = int(self.Angle1[4])
			except ValueError:
				RA_mm_d1 = 0

			try:
				RA_mm_d2 = int(self.Angle1[5])
			except ValueError:
				RA_mm_d2 = 0

			try:
				RA_mm_d3 = int(self.Angle1[6])
			except ValueError:
				RA_mm_d3 = 0

			# self.RA = 15.0*((RA_HH) + RA_MM/60.0 + ((RA_mm_d1*0.1 + RA_mm_d2*0.01 + RA_mm_d3*0.001)/3600.0))
			self.RA = 15.0*((RA_HH) + RA_MM/60.0 + ((RA_mm_d1*100 + RA_mm_d2*10 + RA_mm_d3)/60000.0))

			DEC_SIGN = self.Angle2[0]
			DEC_SIGN = int(DEC_SIGN + "1") # This operation doesn't appear strictly necessary

			try:
				DEC_DD = int(self.Angle2[1:3])
			except ValueError:
				DEC_DD = 0 # We should probably just declare it invalid...

			try:
				DEC_MM = int(self.Angle2[3:5])
			except ValueError:
				DEC_MM = 0

			try:
				DEC_mm_d1 = int(self.Angle2[5])
			except ValueError:
				DEC_mm_d1 = 0

			try:
				DEC_mm_d2 = int(self.Angle2[6])
			except ValueError:
				DEC_mm_d2 = 0

			self.DEC = DEC_DD + DEC_MM/60.0 + DEC_mm_d1*(0.1/60.0) + DEC_mm_d2*(0.01/60.0)
			self.DEC *= DEC_SIGN

			# Convert uncertainty in minutes of arc to fractional degrees
			self.Uncertainty *= (1/60)

		# 3: RA/DEC = HHMMmmm+DDdddd MX   (MX in degrees of arc, no need to convert)
		elif(self.AngleFormatCode == 3):
			try:
				RA_HH = int(self.Angle1[0:2])
			except ValueError:
				RA_HH = 0 # We should probably just declare it invalid...

			try:
				RA_MM = int(self.Angle1[2:4])
			except ValueError:
				RA_MM = 0

			try:
				RA_mmm =  int(self.Angle1[4:7])
			except ValueError:
				RA_mmm = 0

			self.RA = 15.0*(RA_HH + RA_MM/60.0 + (RA_mmm * (0.001/60.0)))

			try:
				DEC_SIGN = self.Angle2[0]
			except ValueError:
				DEC_SIGN = 0

			try:
				DEC_DD = int(self.Angle2[1:3])
			except ValueError:
				DEC_DD = 0 # We should probably just declare it invalid...

			try:
				DEC_d1 = int(self.Angle2[3])
			except ValueError:
				DEC_d1 = 0

			try:
				DEC_d2 = int(self.Angle2[4])
			except ValueError:
				DEC_d2 = 0

			try:
				DEC_d3 = int(self.Angle2[5])
			except ValueError:
				DEC_d3 = 0

			try:
				DEC_d4 = int(self.Angle2[6])
			except ValueError:
				DEC_d4 = 0

			DEC_SIGN =  int(DEC_SIGN + "1") # This operation doesn't appear strictly necessary
			self.DEC =  DEC_DD + (DEC_d1 * .1) + (DEC_d2 * 0.01) + (DEC_d3 * .001) + (DEC_d4 * 0.0001)
			self.DEC *= DEC_SIGN

		# 4: AZ/EL  = DDDMMSS+DDMMSS MX   (MX in seconds of arc)
		elif(self.AngleFormatCode == 4):
			try:
				AZ_DDD = int(self.Angle1[0:3])
			except ValueError:
				AZ_DDD = 0 # We should probably just declare it invalid...

			try:
				AZ_MM = int(self.Angle1[3:5])
			except ValueError:
				AZ_MM = 0

			try:
				AZ_SS = int(self.Angle1[5:7])
			except ValueError:
				AZ_SS = 0

			self.AZ = AZ_DDD + AZ_MM/60.0 + AZ_SS/3600.0

			EL_SIGN = self.Angle2[0]
			# It's theoretically possible for someone to submit an EL > 90, but not a negative AZ.
			EL_SIGN = int(EL_SIGN + "1") # This operation doesn't appear strictly necessary

			try:
				EL_DD = int(self.Angle2[1:3])
			except ValueError:
				EL_DD = 0 # We should probably just declare it invalid...

			try:
				EL_MM = int(self.Angle2[3:5])
			except ValueError:
				EL_MM = 0

			try:
				EL_SS = int(self.Angle2[5:7])
			except ValueError:
				EL_SS = 0

			self.EL  = EL_DD  + EL_MM/60.0 + EL_SS/3600.0
			self.EL *= EL_SIGN

			# Convert uncertainty in seconds of arc to fractional degrees
			self.Uncertainty *= (1/3600)

		# 5: AZ/EL  = DDDMMmm+DDMMmm MX   (MX in minutes of arc)
		elif(self.AngleFormatCode == 5):
			try:
				AZ_DDD = int(self.Angle1[0:3])
			except ValueError:
				AZ_DDD = 0 # We should probably just declare it invalid...

			try:
				AZ_MM = int(self.Angle1[3:5])
			except ValueError:
				AZ_MM = 0

			try:
				AZ_mm_d1 = int(self.Angle1[5])
			except ValueError:
				AZ_mm_d1 = 0

			try:
				AZ_mm_d2 = int(self.Angle1[6])
			except ValueError:
				AZ_mm_d2 = 0

			self.AZ = AZ_DDD + AZ_MM/60.0 + AZ_mm_d1*(0.1/60.0) + AZ_mm_d2*(0.01/60.0)

			EL_SIGN = self.Angle2[0]
			# It's theoretically possible for someone to submit an EL > 90, but not a negative AZ.
			EL_SIGN = int(EL_SIGN + "1") # This operation doesn't appear strictly necessary

			try:
				EL_DD = int(self.Angle2[1:3])
			except ValueError:
				EL_DD = 0 # We should probably just declare it invalid...

			try:
				EL_MM = int(self.Angle2[3:5])
			except ValueError:
				EL_MM = 0

			try:
				EL_mm_d1 = int(self.Angle2[5])
			except ValueError:
				EL_mm_d1 = 0

			try:
				EL_mm_d2 = int(self.Angle2[6])
			except ValueError:
				EL_mm_d2 = 0

			self.EL = EL_DD + EL_MM/60.0 + EL_mm_d1*(0.1/60.0) + EL_mm_d2*(0.01/60.0)

			# Convert uncertainty in minutes of arc to fractional degrees
			self.Uncertainty *= (1/60)


		# 6: AZ/EL  = DDDdddd+DDdddd MX   (MX in degrees of arc, no need to convert)
		elif(self.AngleFormatCode == 6):
			try:
				AZ_DDD = int(self.Angle1[0:3])
			except ValueError:
				AZ_DDD = 0 # We should probably just declare it invalid...

			try:
				AZ_d1 = int(self.Angle1[3])
			except ValueError:
				AZ_d1 = 0

			try:
				AZ_d2 = int(self.Angle1[4])
			except ValueError:
				AZ_d2 = 0

			try:
				AZ_d3 = int(self.Angle1[5])
			except ValueError:
				AZ_d3 = 0

			try:
				AZ_d4 = int(self.Angle1[6])
			except ValueError:
				AZ_d4 = 0

			self.AZ =  AZ_DDD + (AZ_d1 * .1) + (AZ_d2 * 0.01) + (AZ_d3 * .001) + (AZ_d4 * 0.0001)

			EL_SIGN = self.Angle2[0]
			# It's theoretically possible for someone to submit an EL > 90, but not a negative AZ.
			EL_SIGN = int(EL_SIGN + "1") # This operation doesn't appear strictly necessary

			try:
				EL_DD = int(self.Angle2[1:3])
			except ValueError:
				EL_DD = 0 # We should probably just ELlare it invalid...

			try:
				EL_d1 = int(self.Angle2[3])
			except ValueError:
				EL_d1 = 0

			try:
				EL_d2 = int(self.Angle2[4])
			except ValueError:
				EL_d2 = 0

			try:
				EL_d3 = int(self.Angle2[5])
			except ValueError:
				EL_d3 = 0

			try:
				EL_d4 = int(self.Angle2[6])
			except ValueError:
				EL_d4 = 0

			self.EL =  EL_DD + (EL_d1 * .1) + (EL_d2 * 0.01) + (EL_d3 * .001) + (EL_d4 * 0.0001)
			self.EL *= EL_SIGN

		# 7: RA/DEC = HHMMSSs+DDdddd MX   (MX in degrees of arc, no need to convert)
		elif(self.AngleFormatCode == 7 and self.RecordFormat == "IOD"):
			try:
				RA_HH = int(self.Angle1[0:2])
			except ValueError:
				RA_HH = 0 # We should probably just declare it invalid...

			try:
				RA_MM = int(self.Angle1[2:4])
			except ValueError:
				RA_MM = 0

			try:
				RA_SS = int(self.Angle1[4:6])
			except ValueError:
				RA_SS = 0

			try:
				RA_s = int(self.Angle1[6])
			except ValueError:
				RA_s = 0

			self.RA = 15.0*(RA_HH + RA_MM/60.0 + RA_SS / 3600.0 + RA_s*(0.1/3600.0))

			try:
				DEC_SIGN = self.Angle2[0]
			except ValueError:
				DEC_SIGN = 0

			try:
				DEC_DD = int(self.Angle2[1:3])
			except ValueError:
				DEC_DD = 0 # We should probably just declare it invalid...

			try:
				DEC_d1 = int(self.Angle2[3])
			except ValueError:
				DEC_d1 = 0

			try:
				DEC_d2 = int(self.Angle2[4])
			except ValueError:
				DEC_d2 = 0

			try:
				DEC_d3 = int(self.Angle2[5])
			except ValueError:
				DEC_d3 = 0

			try:
				DEC_d4 = int(self.Angle2[6])
			except ValueError:
				DEC_d4 = 0

			DEC_SIGN =  int(DEC_SIGN + "1") # This operation doesn't appear strictly necessary
			self.DEC =  DEC_DD + (DEC_d1 * .1) + (DEC_d2 * 0.01) + (DEC_d3 * .001) + (DEC_d4 * 0.0001)
			self.DEC *= DEC_SIGN
		# TODO: Add in the remaining format codes for UK (7-9)
		# TODO: Parse the Angle uncertainty code in the UK format
		else:
			log.error("Did not find an Angle case with AngleFormatCode '{}'".format(self.AngleFormatCode))
# End of the Angle parsing cases


def DateTime_frompacked(DateTimeString,type="IOD"):
	""" Unpack the datetime format from IOD strings 
	
	Of the format:
		 000000000011111111
	     012345678901234567
	IOD: YYYYMMDDHHMMSSsss
	UK:    YYMMDDHHMMSSssss
	RDE:   YYMMDDHHMMSS.ss
	"""
	# FIXME: This could be made more efficient (remove try/except) by better dealing with spaces, non-valid characters

	if(type=="IOD"):
		YEAR = int(DateTimeString[0:4])
	else:
		YEAR = int(DateTimeString[0:2])
		if (YEAR < 57):		# Year of Sputnik launch, first cataloged object
			YEAR = 2000 + YEAR
			# Make the input string of consistent between formats for the rest of the parsing
			DateTimeString = '20' + DateTimeString 
		else:
			YEAR = 1900 + YEAR
			DateTimeString = '19' + DateTimeString 

	MONTH = int(DateTimeString[4:6])
	DAY = int(DateTimeString[6:8])

	try:
		HOUR = int(DateTimeString[8:10])
		try:
			MINUTE = int(DateTimeString[10:12])
			try:
				SECOND = int(DateTimeString[12:14])
			except ValueError:
				SECOND = MICROSECONDS = 0
		except ValueError:
			MINUTE = SECOND = MICROSECONDS = 0
	except ValueError:
		HOUR = MINUTE = SECOND = MICROSECONDS = 0

	try:
		if (DateTimeString[14]=="."):
			SUBSECS = DateTimeString[15:].rstrip()
		else:
			SUBSECS = DateTimeString[14:].rstrip()

		if (SUBSECS):
			SUBSECONDf = float('.' + SUBSECS)
			MICROSECONDS = int("{:.6f}".format(SUBSECONDf)[2:])
		else:
			MICROSECONDS = 0
	except (IndexError, ValueError):
		MICROSECONDS = 0

	return datetime(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, MICROSECONDS)


class IOD:
	"""IOD/Visual Observation (includes UK and RDE encoded data)

	   NameCode, or NameString indicates packed data requiring further processing (to disentagle variable names)

       # Array of variable names for IOD parsing.
       # NameCode, or NameString indicates packed data requiring further processing (to disentagle variable names)
	"""
	def __init__(self, line):					# (Element #, start_col, end_col)
		self.line = line
		self.UserString = None 					# A preMVP hack before we're parsing it fully.
		self.ObjectNumber = None				# (0, 0, 4)  	Object number (NORAD)
		self.LaunchYear = None					# (1, 6, 7)  	Launch year. Implied century.
		self.InternationalDesignation = None	# (2, 9, 14)  	International Designation (COSPAR)
		self.Station = 9999						# (3, 16, 19)  	Four digit station number
		self.StationStatusCode = None			# (4, 21, 21)  	Station status code
		self.StationStatus = None				# 				Only in the IOD format
		self.DateTimeString = None				# (5, 23, 39)  	DateTime string YYYYMMDDHHMMSSsss
		self.DateTime = None
		self.TimeUncertainty = None				# (6, 41, 42)  	Time Uncertainty, expressed as MX, Evaluated as M*10E(X-8).
		self.TimeStandardCode = None			#               In the UK, RDE formats
		self.AngleFormatCode = None				# (7, 44, 44)  	Angle format code
		self.EpochCode = None
		self.Epoch = None						# (8, 45, 45)  	Epoch code
		self.RA = None
		self.DEC = None
		self.AZ = None
		self.EL = None
		self.ValidPosition = -1
		self.PositionUncertainty = None			# (10, 62, 63) 	Positional uncertainty, expressed as MX, Evaluated as M*10E(X-8).
		self.OpticalCode = None					# (11, 65, 65) 	Optical behavior code
		self.VisualMagnitude = None				# (12, 66, 69) 	Visual magnitude. Implied decimal point.
		self.MagnitudeUncertainty = None		# (13, 71, 72) 	Magnitude uncertainty. Implied decimal point.
		self.FlashPeriod = None					# (14, 74, 79) 	Flash period in seconds. Implied decimal point.
		self.VisualMagnitude_high = None		#               In the UK, RDE formats
		self.VisualMagnitude_low = None			#               In the UK, RDE formats
		self.Remarks = None
		self.message_id = None
		self.IODType = None						# IOD, UK or RDE

	# TODO: The following functions are to-do
	def calc_AZ_EL_from_RA_DEC(self):
		# Create as a class function call, but put the actual workings as a module function
		# so it can be accessed separately
		pass

	def calc_RA_DEC_from_AZ_EL(self):
		# Create as a class function call, but put the actual workings as a module function
		# so it can be accessed separately
		pass
# end of class IOD


# Don't worry about the lint warnings on these: https://github.com/PyCQA/pylint/issues/1451
# This one works
# FIXME: This could be potentially speeded up and use less memory by eliminating (or using) the parentheses, which make variable assignments
iod_format_re = re.compile ('^(\d{5}\s\d{2}\s\d{3}\D*)*\s{1,16}(\d{4}\s)(\D)\s(\d{8})(\d{0,9}$|\d{0,9}\s+\d{2}\s*\d*\s*\d*\s*[-+]*\d*\s*\d{0,2}\s[EFIRSXBHPADMNV]{0,1})') # pylint: disable=anomalous-backslash-in-string

# This string *should* work to detect the full format (uses several ORs) but python doesn't like it
#iod_format_re = re.compile ('^(\d{5}\s\d{2}\s\d{3}\D*)*\s{1,16}(\d{4}\s)(\D)\s(\d{8})(\d{0,9}$|\d{0,9}\s+\d{2}\s*\d*\s*\d*\s*[-+]*\d*\s*\d{0,2}\s[EFIRSXBHPADMNV]{0,1}$|\d{0,9}\s+\d{2}\s*\d*\s*\d*\s*[-+]*\d*\s*\d{0,2}\s[EFIRSXBHPADMNV]{0,1}[+-]\d+\s+\d+$|\d{0,9}\s+\d{2}\s*\d*\s*\d*\s*[-+]*\d*\s*\d{0,2}\s[EFIRSXBHPADMNV]{0,1}[+-]\d+\s+\d+\s+\d+$)')

# Simple format
#iod_format_re = re.compile ('^(\d{5}\s\d{2}\s\d{3}\D*)*\s{1,16}(\d{4}\s)(\D)\s(\d{8})(\d{0,9}$|\d{0,9}\s+\d\d.*)')
def format_test_iod(line=False):
	match = iod_format_re.search(line)
	if match:
		return True
	else:
		return False


""" 
Notes on the UK format:

This format is deficient for the following reasons:
- Uses international designator as the identifier (no NORAD number)
- Uses a 2 digit numeric code for launch piece number, as opposed to a 3-letter code in the TLE standard.
- Column 33, "Time Standard Code" appears to be meaningless, as 0 is listed as possible by the example, which lists 1-3 being valid.
- Doesn't require leading zeros (i.e., on positional accuracy numbers)
However, it is superior for the following reason:
- One more digit of precision in reported angles

"""
uk_format_re = re.compile ('^\d{17}(?=\d+[ ]*)[ \d]{10}(?=\d+[ ]*)[\d ]{5}[1-3][1-9](?=\d*[ ]*)[\d ]{8}[-+ ](?=\d+[ ]*)[\d ]{7}[ \d]{4}[0-6$]') # pylint: disable=anomalous-backslash-in-string
# Weaker UK format test which matches the beginning of a UK line but NOT the beginning of an RDE line
# uk_format_re = re.compile('^(?=\d+[ ]*?)[\d ]{24}(?=\d)[ \d]{3}') # pylint: disable=anomalous-backslash-in-string
# uk_format_re = re.compile('^(\d{17})') # pylint: disable=anomalous-backslash-in-string

# UK Format full length, but doesn't deal with early end-of-lines yet
# uk_format_re = re.compile('^\d{17}(?=\d+[ ]*)[ \d]{10}(?=\d+[ ]*)[\d ]{5}[1-3][1-9](?=\d*[ ]*)[\d ]{8}[-+ ](?=\d+[ ]*)[\d ]{7}[ \d]{4}[0-6$][\d ]{8}[\d ]{5}(?=[+-]?\d+\s*)[-+\d ]{3}(?=[+-]?\d+\s*)[-+\d ]{3}(?=[ ]*\d+[ ]*)[\d ]{5}[ SIRFXE]{1}') # pylint: disable=anomalous-backslash-in-string
def format_test_uk(line=False):
	match = uk_format_re.search(line)
	if match:
		return True
	else:
		return False


rde_format_re = re.compile('\d{4}\s\d{4}\s(?=\d.\d*[ ]*)[\d. ]{4}\d\s\d{3}[0-6]\n(^\d{2}\n(^\d{7}\s\d{6}.\d{2}\s\d{6}[-+ ]\d{6}(?=[- ]\d.\d)[- \d.]{4}(?=[- ]\d.\d)[- \d.]{4}.*\n){2,}){1,}999', re.MULTILINE) # pylint: disable=anomalous-backslash-in-string
rde_data_line_re = re.compile('\d{7}\s\d{6}.\d{2}\s\d{6}[-+ ]\d{6}(?=[- ]\d.\d)[- \d.]{4}(?=[- ]\d.\d)[- \d.]{4}')
def format_test_rde(block=False):
	match = rde_format_re.search(block)
	if match:
		return True
	else:
		return False


# Parse enter blocks of text instead of just lines
# This is the typical use-case, as IOD entries usually come in clusters
def parse_iod_lines(block=False):
	""" Parse a block of text containing IOD-formatted observation records, and return formatted records + count.

	Format documented at: http://www.satobs.org/position/IODformat.html
	"""
	lines = block.split('\n')
	IODentryList = []
	iod_count = 0
	for line in lines:
		line = line.rstrip()
		match = format_test_iod(line)
		if (match):
			IOD_line = IOD(line)
			IOD_line.IODType = "IOD"
			line_length = len(line)

			IOD_line.ObjectNumber = int(line[0:5])

			LaunchYearTwoDigit = int(line[6:8])
			if (LaunchYearTwoDigit < 57):		# Year of Sputnik launch, first cataloged object
				IOD_line.LaunchYear = 2000 + LaunchYearTwoDigit
			else:
				IOD_line.LaunchYear = 1900 + LaunchYearTwoDigit

			IOD_line.InternationalDesignation = str(IOD_line.LaunchYear) + ' ' + line[9:15]
			IOD_line.Station = int(line[16:20])
			IOD_line.StationStatusCode = line[21]	# Future TODO - Expand out the short and long description of the codes

			IOD_line.DateTimeString = line[23:40]
			IOD_line.DateTime = DateTime_frompacked(IOD_line.DateTimeString)

			# Expressed as MX, where M = mantissa, and X = exponent input. Evaluated as M*10E(X-8).
			IOD_line.TimeUncertainty = float(line[41]) * 10 **(int(line[42]) - 8)

			if (line_length >= 45):
				try:
					IOD_line.AngleFormatCode = int(line[44])
				except ValueError:
					IOD_line.AngleFormatCode = -1
					IOD_line.ValidPosition = -1	# Need format code to parse angle

				try:
					EpochCodeString = line[45]
					if (EpochCodeString == " "):
						IOD_line.EpochCode = 0
					else:
						IOD_line.EpochCode = int(line[45])
				except ValueError:
					IOD_line.EpochCode = -1
					IOD_line.ValidPosition = -1	# If EpochCode as read as Zero (not blank), we won't trigger this error
			else:
				IOD_line.AngleFormatCode = -1 
				IOD_line.EpochCode = -1
				IOD_line.ValidPosition = -1

			# TODO: Figure out which of the missing data parts to actuall warn users about
			if (line_length>61 and IOD_line.AngleFormatCode >0):
				AngleString = line[47:61]
				angle_content = angle_content_re.search(AngleString)

				try:
					IOD_line.PositionUncertainty = float(line[62]) * 10 **(int(line[63]) - 8)
				except ValueError:
					IOD_line.PositionUncertainty = None # Don't really need this (initialized state)

				if ( (IOD_line.AngleFormatCode>=0) and (IOD_line.EpochCode>=0) and (angle_content is not None) ):
					try:
						angle = Angle(
							IOD_line.AngleFormatCode, 
							IOD_line.EpochCode, 
							AngleString[0:7], 
							AngleString[7:14], 
							IOD_line.PositionUncertainty, 
							"",
							"IOD")
						IOD_line.AZ = angle.AZ
						IOD_line.EL = angle.EL
						IOD_line.RA = angle.RA
						IOD_line.DEC = angle.DEC
						IOD_line.Epoch = angle.Epoch
					except:
						log.error("Problem angle: '{}' - Offending line:".format(AngleString))
						log.error(line)
						IOD_line.ValidPosition = -1
				elif ((IOD_line.AngleFormatCode>=0) and (IOD_line.EpochCode>=0)):
					# Note - Not an error, because the standards provide for "reporting for duty"
					# even if no observations are made.
					log.warning("Valid Angle ({}) and Epoch ({}) codes, but no valid position data. Offending line:".format(IOD_line.AngleFormatCode,IOD_line.EpochCode ))
					log.warning(line)
					IOD_line.ValidPosition = -1
				else:
					IOD_line.ValidPosition = -1
			else:
				IOD_line.ValidPosition = -1


			if (line_length >= 65):
				IOD_line.OpticalCode = line[65]

			if (line_length >= 70):
				# Cols 67-70 Visual Magnitude
				vmag = line[66:70]
				vmag_sign = vmag[0]
				vmag_whole = vmag[1:3]
				vmag_frac = vmag[3]

				try:
					IOD_line.VisualMagnitude = float(vmag_sign + vmag_whole + '.' + vmag_frac)
				except ValueError:
					IOD_line.VisualMagnitude = 99


			if (line_length >= 73):
				# Cols  72- 73: Magnitude uncertainty. Implied decimal point
				# Implied decimal point between cols 72 and 73. 
				vmag_unc = line[71:73]
				try:
					IOD_line.MagnitudeUncertainty = float(vmag_unc[0] + '.' + vmag_unc[1])
				except ValueError:
					IOD_line.MagnitudeUncertainty = 0

			if (line_length >= 80):
				# Cols  75- 80: Flash period in seconds. 
				# Implied decimal point between cols 77 and 78. BLANK IF NO DATA.
				flash_period = line[74:80]
				try:
					IOD_line.FlashPeriod = float(flash_period[0:3] + '.' + flash_period[3:6])
				except ValueError:
					IOD_line.FlashPeriod = 0

			if (line_length >= 80):
				IOD_line.Remarks = line[80:]
					
			iod_count += 1
			IODentryList.append(IOD_line)
	if (len(IODentryList)):
		return IODentryList
	else:
#		log.warning("Error: no data found. Call parse_iod_lines with a properly formatted IOD line comfirmed by format_test_iod")
		return(False)


# Parse enter blocks of text instead of just lines
# This is the typical use-case, as IOD entries usually come in clusters
def parse_uk_lines(block=False):
	""" Parse a block of text containing UK-formatted observation records, and return formatted records + count.

	Format documented at: http://www.satobs.org/position/UKformat.html
	"""
	lines = block.split('\n')
	IODentryList = []
	uk_count = 0
	for line in lines:
		line = line.rstrip()
		match = format_test_uk(line) # Handle this separately? I.E. assume its properly formatted?  Would require more exception handling below.
		if (match):
			UK_line = IOD(line)
			UK_line.IODType = "UK"
			line_length = len(line)

			LaunchYearTwoDigit = int(line[0:2])
			if (LaunchYearTwoDigit < 57):		# Year of Sputnik launch, first cataloged object
				UK_line.LaunchYear = 2000 + LaunchYearTwoDigit
			else:
				UK_line.LaunchYear = 1900 + LaunchYearTwoDigit

			piece_letters = launch_piece_number_to_letter(line[5:7])
			UK_line.InternationalDesignation = str(UK_line.LaunchYear) + '-' + line[2:5] + piece_letters
			# 'Observing Site Number'
			UK_line.Station = int(line[7:11])

			UK_line.DateTimeString = line[11:27]
			UK_line.DateTime = DateTime_frompacked(UK_line.DateTimeString,"UK")

			# Expressed as MX, where M = mantissa, and X = exponent input. Evaluated as M*10E(X-8).
			try:
				UK_line.TimeUncertainty = float(line[27] + '.' + line[28:32])
			except ValueError:
				UK_line.TimeUncertainty = 0

			try:
				UK_line.TimeStandardCode = int(line[32])
			except ValueError:
				UK_line.TimeStandardCode = 0

			# Position Format Code
			try:
				UK_line.AngleFormatCode = int(line[33])
			except ValueError:
				log.error("Valid Angle Format Code not specified.")
				UK_line.AngleFormatCode = -1
				UK_line.ValidPosition = -1	# Need format code to parse angle

			AngleString = line[34:50]
			# FIXME: Look at this angle content regexp across the formats
			# angle_content = angle_content_re.search(AngleString)

			# Cols  51-54: Position Accuracy.
			try:
				PositionUncertaintyString = line[50:54]
			except ValueError:
				PositionUncertaintyString = None # Not required (initialized state)

			try:
				UK_line.EpochCode = int(line[54])
			except ValueError:
				log.error("Valid Epoch Code not specified.")
				UK_line.EpochCode = 0
				UK_line.ValidPosition = -1	# If EpochCode as read is Zero (not blank), we won't trigger this error

			if (UK_line.AngleFormatCode>0):
				try:
					angle = Angle(
						UK_line.AngleFormatCode, 
						UK_line.EpochCode, 
						AngleString[0:8], 
						AngleString[8:16], 
						0, 
						PositionUncertaintyString,
						"UK"
						)
					UK_line.AZ = angle.AZ
					UK_line.EL = angle.EL
					UK_line.RA = angle.RA
					UK_line.DEC = angle.DEC
					UK_line.Epoch = angle.Epoch
					# FIXME: Need to pass on uncertainty data as well
				except:
					log.error("Problem angle: '{}'".format(AngleString))
					UK_line.ValidPosition = -1
			else:
				# Note - Not an error, because the standards provide for "reporting for duty"
				# even if no observations are made.
				# FIXME: Although this does not exist in the UK format (?
				log.warning("No Position Data")
				UK_line.ValidPosition = -1

			# This is the brightest stellar magnitude attained by the satellite during
			# the period of one minute centred on the time of the observation. It is
			# entered as a 3 digit number, in one of the following forms:

			# (1) if the satellite is brighter than magnitude +9.9
			# 	Column 69 is entered + or -
			# 	Columns 70 and 71 state the numerical value, formatted as Mm

			# (2) if the satellite is fainter than magnitude +9.9
			# 	The sign is omitted, and the numerical format is MMm

			if (line_length>=71):
				# Cols  69-71: Brightest Visual Magnitude
				vmag = line[68:71]
				if (vmag[0]=="+" or vmag[0]=="-"):
					UK_line.VisualMagnitude_high = float(vmag[0] + vmag[1] + '.' + vmag[2])
				else:
					UK_line.VisualMagnitude_high = float(vmag[0:2] + '.' + vmag[2])


			if (line_length>=74):
				# Cols  72-74: Faintest Visual Magnitude
				vmag = line[71:74]
				if (not vmag):
					pass
				elif (vmag == "INV"):
					UK_line.VisualMagnitude_low	= 99
				elif (vmag[0]=="+" or vmag[0]=="-"):
					UK_line.VisualMagnitude_low = float(vmag[0] + vmag[1] + '.' + vmag[2])
				elif(vmag):
					UK_line.VisualMagnitude_low = float(vmag[0:2] + '.' + vmag[2])

				if (UK_line.VisualMagnitude_high and not UK_line.VisualMagnitude_low):
					UK_line.VisualMagnitude = UK_line.VisualMagnitude_high	

			if (line_length>=79):
				# Cols  75-79: Flash Period
				# Time in seconds between successive maxima, formatted as SSSss
				FlashPeriodString = line[74:79]
				try:
					UK_line.FlashPeriod = float(FlashPeriodString[0:3] + '.' + FlashPeriodString[3:5])
				except ValueError:
					UK_line.FlashPeriod = None 

				UK_line.Remarks = line[79:].strip()

			uk_count += 1
			IODentryList.append(UK_line)
	if (len(IODentryList)):
		return IODentryList
	else:
#		log.warning("Error: No data found. Call parse_uk_lines with a properly formatted UK line comfirmed by format_test_uk")
		return(False)


# Parse enter blocks of text instead of just lines
# This is the typical use-case, as IOD entries usually come in clusters
# We are assuming there is only one full RDE record (with multiple observations) per message block
def parse_rde_record(block=False):
	""" Parse a block of text containing RDE-formatted observation records, and return formatted records + count.

	Format documented at: http://www.satobs.org/position/RDEformat.html
	"""
	match = rde_format_re.search(block)
	IODentryList = []
	rde_count = 0
	if (match):
		lines = match.group(0).split('\n')

		# Match automatically returns the first line
		# Pop off the list and process the header which applies to all following records
		line = lines.pop(0)

		# TODO: We'll need to do something else with this line.  Maybe UK-format it?
		RDE_line = IOD(line)
		RDE_line.IODType = "RDE"

		# 'Observing Site Number'
		RDE_line.Station = int(line[0:4])
		YYMM = line[5:9]

		try:
			RDE_line.TimeUncertainty = float(line[10:13])
		except ValueError:
			RDE_line.TimeUncertainty = 0

		try:
			RDE_line.TimeStandardCode = int(line[13])
		except ValueError:
			RDE_line.TimeStandardCode = 0

		# Col 15: Position Format Code.
		# Russell always uses Code 1, with whole arc seconds
		try:
			RDE_line.AngleFormatCode = int(line[14])
		except ValueError:
			log.error("Valid Angle Format Code not specified.")
			RDE_line.AngleFormatCode = 0
			RDE_line.ValidPosition = -1	# Need format code to parse angle

		# Cols  17-19: Position Accuracy.
		# Russell reports 120 arc seconds, as SSS
		try:
			PositionUncertaintyString = line[16:19]
		except ValueError:
			PositionUncertaintyString = None # Not required (initialized state)

		# Col 20: Epoch of star chart used to determine position
		# Russell always uses code 4.
		try:
			RDE_line.EpochCode = int(line[19])
		except ValueError:
			log.error("Valid Epoch Code not specified.")
			RDE_line.EpochCode = 0
			RDE_line.ValidPosition = -1	# If EpochCode as read is Zero (not blank), we won't trigger this error

		line = lines.pop(0)
		YYMMDD = YYMM + line[0:2]

		for line in lines:
			line = line.rstrip()
			if( len(line)>2 and line != "999"):
				LaunchYearTwoDigit = int(line[0:2])
				if (LaunchYearTwoDigit < 57):		# Year of Sputnik launch, first cataloged object
					RDE_line.LaunchYear = 2000 + LaunchYearTwoDigit
				else:
					RDE_line.LaunchYear = 1900 + LaunchYearTwoDigit

				piece_letters = launch_piece_number_to_letter(line[5:7])
				RDE_line.InternationalDesignation = str(RDE_line.LaunchYear) + '-' + line[2:5] + piece_letters

				# Doesn't exist in RDE format
				# RDE_line.StationStatusCode = line[21]  # TODO: - Expand out the short and long description of the codes

				RDE_line.DateTimeString = YYMMDD + line[8:17]
				RDE_line.DateTime = DateTime_frompacked(RDE_line.DateTimeString,"RDE")

				AngleString = line[18:31]
				# FIXME: Look at this angle content regexp across the formats
				# angle_content = angle_content_re.search(AngleString)

				if RDE_line.AngleFormatCode:
					try:
						angle = Angle(
							RDE_line.AngleFormatCode, 
							RDE_line.EpochCode, 
							AngleString[0:8], 
							AngleString[8:16], 
							0, 
							PositionUncertaintyString,
							"RDE"
							)
						RDE_line.AZ = angle.AZ
						RDE_line.EL = angle.EL
						RDE_line.RA = angle.RA
						RDE_line.DEC = angle.DEC
						RDE_line.Epoch = angle.Epoch
						# FIXME: Need to pass on uncertainty data as well
					except:
						log.error("Problem angle: '{}'".format(AngleString))
						RDE_line.ValidPosition = -1
				else:
					# Note - Not an error, because the standards provide for "reporting for duty"
					# even if no observations are made.
					# FIXME: Although this does not exist in the RDE format (?
					log.warning("No Position Data")
					RDE_line.ValidPosition = -1

				# This is the brightest stellar magnitude attained by the satellite during
				# the period of one minute centred on the time of the observation. It is
				# entered as a 3 digit number, in one of the following forms:

				# (1) if the satellite is brighter than magnitude +9.9
				# 	Column 69 is entered + or -
				# 	Columns 70 and 71 state the numerical value, formatted as Mm

				# (2) if the satellite is fainter than magnitude +9.9
				# 	The sign is omitted, and the numerical format is MMm

				# Cols  32-35: Brightest Visual Magnitude
				#  This is the brightest stellar magnitude attained by the satellite during
				#  the period of one minute centred on the time of the observation, It is
				#  entered as a 3 digit number.

				#  If magnitude is negative, enter "-" in column 32
				#  Columns 32-35 state the numerical value, formatted as M.m
				vmag = line[31:35]
				RDE_line.VisualMagnitude_high = float(vmag.strip())

				# Cols  36-39: Faintest Visual Magnitude
				#  Format is the same as for Brightest Visual Magnitude.
				#  If the magnitude is constant, repeat the Brightest Visual Magnitude entry
				vmag = line[35:39]
				if (not vmag):
					RDE_line.VisualMagnitude_low	= None
				else:
					RDE_line.VisualMagnitude_low = float(vmag.strip())

				# Cols  40-42: Flash Period
				#  Time in seconds between successive maxima, formatted as SSS.sss
				#  If value is less than 1, show one leading zero.
				#  Show only significant trailing zeros.
				#  Omit decimal point for whole number values.

				FlashPeriodString = line[39:42]
				try:
					RDE_line.FlashPeriod = float(FlashPeriodString.strip())
				except ValueError:
					RDE_line.FlashPeriod = None 

				# Col      43: Remarks.
				RDE_line.Remarks = line[42:].strip()
				RDE_line.line = RDE_line.line[0:20] + ' ' + YYMM + line.strip()
				rde_count += 1
				IODentryList.append(RDE_line)
			elif (line != "999"):
				YYMMDD = YYMM + line[0:2]
	if (len(IODentryList)):
		return IODentryList
	else:
#		log.warning("Error: no records found. Call parse_rde_record with a properly formatted RDE line comfirmed by format_test_rde")
		return(False)

""" The following three functions provide a simple interface to:
	1) Open a file
	2) Test for presence of requested record.
	3) Parse the records if they exist, and
	4) Return a list of parsed records, plus the count
"""

def get_iod_records_from_file(filename):
	""" Open a file and return a list with parsed IOD records, and record count."""
	with open(filename) as file:
		IOD_file_lines = file.read()

	IOD_records = []
	count = 0 
	IOD_records = parse_iod_lines(IOD_file_lines)

	if (len(IOD_records)):
		return IOD_records
	else:
		return False


def get_uk_records_from_file(filename):
	""" Open a file and return a list with parsed UK records, and record count """
	with open(filename) as file:
		UK_file_lines = file.read()

	UK_records = []
	count = 0 
	UK_records = parse_uk_lines(UK_file_lines)

	if (len(UK_records)):
		return UK_records
	else:
		return False


def get_rde_records_from_file(filename):
	""" Open a file and return a list with parsed RDE records, and record count."""
	with open(filename) as file:
		RDE_file_string = file.read()

	RDE_records = []
	count = 0 
	RDE_records = parse_rde_record(RDE_file_string)

	if (len(RDE_records)):
		return RDE_records
	else:
		return False

def get_iod_records(block):
	""" Return a list with parsed IOD records"""
	IOD_records = parse_iod_lines(block)

	if (len(IOD_records)):
		return IOD_records
	else:
		return False


def get_uk_records(block):
	""" Return a list with parsed UK records"""
	UK_records = parse_uk_lines(block)

	if (len(UK_records)):
		return UK_records
	else:
		return False


def get_rde_records(block):
	""" Return a list with parsed RDE records."""	
	RDE_records = parse_rde_record(block)

	if (len(RDE_records)):
		return RDE_records
	else:
		return False