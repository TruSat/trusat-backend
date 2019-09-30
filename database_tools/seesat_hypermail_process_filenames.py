#!/usr/bin/env python

""" 
This is a script to rename files retrieved from John's hypermail scraper, 
try and determine the date from the filename, and then rename the filename
with the successfully parsed date.

Note that I've had to do some manual cleanup both before and after this 
script to create a clean dataset
"""

import os
import re
import sys
from csv import writer 
from datetime import datetime
from dateutil import parser
from dateutil.tz import gettz
import shutil

def get_submit_time_from_filename(filename):
    """ Determine the submitted date from the filename string from John's hypermail scraper """
    file_string = os.path.basename(filename)
    file_string = os.path.splitext(file_string)[0]

    # Fri,_10_Jul_1998_14:11:27_+0200
    # 'Fri,_11_Dec_1998_05:53:14_-0800_(PST)'
    # '8_Feb_99_17:27:56_MET'
    # (4) 01 Dec 1995 14:48:46
    # (5) '8_Feb_99_17:27:56_MET'
    # (6) Fri,_10_Jul_1998_14:11:27_+0200
    # (6) Fri,_01_Dec_95_14:48:46_gmt
    # (6) Fri,_10_Nov_95_18:08_+0100
    # (7) 'Fri,_11_Dec_1998_05:53:14_-0800_(PST)'
    # (7) 'Fri,_10_Nov_95_05:49:00_UTC_0000'
    # (7) 'Fri,_13_Oct_95__09:38:39_EDT'
    # (7) 'Fri,_14_Jul_1995_23:22:18_-40975532_(EDT)'
    # (8) 'Fri,_14_Jul_1995_01:13:15_+0200_(MET_DST)'
    # (8) 'Fri,__1_Dec_95_06:13:00_UTC_0000
    # (9) 'Fri,_15_Dec_1995___10:30:09__+0100'
    # (10) 'Fri,__1_Dec_1995___13:41:05__+0100'
    # (11) 'Fri,__1_Dec_1995___13:41:05__+0100'

    #tzinfos = {"BRST": -7200, "CST": gettz("America/Chicago")}
 

    date_patterns = [
        "%a,_%d_%b_%Y_%X_%z",  # Fri,_10_Jul_1998_14:11:27_+0200
        "%d_%b_%Y_%X_%Z",      # 01_Aug_1995_12:14:27_GMT
        "%d_%b_%Y_%X_%z",      # 05_Dec_1995_20:53:00_+0200
        "%d_%b_%y_%X_%Z",      # 09_Nov_95_11:45:55_EST
        "%d_%b_%y_%X_"         # 10_Feb_1995_08:20:13_U
        ]

    file_string_spaces = file_string.replace('_',' ')
    try:
#        print("1st: {}".format(file_string_spaces))
        submit_datetime = parser.parse(file_string_spaces)
        if submit_datetime.utcoffset():
            submit_datetime = submit_datetime - submit_datetime.utcoffset()
            submit_datetime = submit_datetime.replace(tzinfo=None)
        return submit_datetime.strftime('%Y-%m-%d %H:%M:%S')
    except:
        for pattern in date_patterns:
            try:
                submit_datetime = datetime.strptime(file_string, pattern)
                if submit_datetime.utcoffset():
                    submit_datetime = submit_datetime - submit_datetime.utcoffset()
                    submit_datetime = submit_datetime.replace(tzinfo=None)
                return submit_datetime.strftime('%Y-%m-%d %H:%M:%S')
            except:
                pass
    try:
        # 'Fri,_10_Nov_95_05:49:00_UTC_0000'
        # 'Fri,_14_Jul_1995_01:13:15_+0200_(MET_DST)'
        # 'Fri,_14_Jul_1995_23:22:18_-40975532_(EDT)'
        file_string_spaces = file_string_spaces.replace('gmt', '')
        file_string_spaces = file_string_spaces.replace('0000', '')
        file_string_spaces = file_string_spaces.replace('- ', '')
        file_string_spaces = file_string_spaces.replace('MET DST', '')
        file_string_spaces = file_string_spaces.replace('CST6CDT', '')
        file_string_spaces = file_string_spaces.replace('-40975532', '')
        file_string_spaces = file_string_spaces.replace('(EDT)', '-0400')
        file_string_spaces = file_string_spaces.replace('EDT', '-0400')
        file_string_spaces = file_string_spaces.replace('(EST)', '-0500')
        file_string_spaces = file_string_spaces.replace('est', '-0500')
        file_string_spaces = file_string_spaces.replace('W. Europe Standard Time+', '')
        file_string_spaces = file_string_spaces.replace('-500', '-0500')
        file_string_spaces = file_string_spaces.replace('+-1000', '-1000')
        file_string_spaces = file_string_spaces.replace('+-100', '-0100')
        file_string_spaces = file_string_spaces.replace('+120', '+1200')
        file_string_spaces = file_string_spaces.replace('+-300', '-0300')
        file_string_spaces = file_string_spaces.replace('ind', 'IST')
        file_string_spaces = file_string_spaces.replace('"GMT"', '')
        file_string_spaces = file_string_spaces.replace(':_', ':00_')

        file_string_spaces = re.sub(':_(\d)_', ':0\1_', file_string_spaces) # pylint: disable=anomalous-backslash-in-string
        file_string_spaces = re.sub('\(.*\)', '', file_string_spaces) # pylint: disable=anomalous-backslash-in-string
        
#        print("2nd: {}".format(file_string_spaces))
        submit_datetime = parser.parse(file_string_spaces)

        if submit_datetime.utcoffset():
            submit_datetime = submit_datetime - submit_datetime.utcoffset()
            submit_datetime = submit_datetime.replace(tzinfo=None)
        return submit_datetime.strftime('%Y-%m-%d %H:%M:%S')
    except:
        pass    
    print("Date is not in expected format: String: '{}'  Filename: '{}'".format(file_string,filename)) 

DateFile = open("seesat_hypermail_dates.csv", 'w')
writer_date = writer(DateFile, dialect='unix')

for dirName, subdirList, fileList in os.walk('/Users/chris/Downloads/all_emails'):
    subdirList.sort()
    for fname in sorted(fileList):
        if(fname == ".DS_Store"):
            continue
        submit_time = get_submit_time_from_filename(fname)

        try:
            submit_datetime = datetime.strptime(submit_time,'%Y-%m-%d %H:%M:%S')
            new_fname = submit_datetime.strftime('%Y%m%d_%H%M%S.txt')
        except:
            new_fname = '00FIXME_' + fname    

        old_fname_full = os.path.join(dirName,fname)
        new_fname_full = os.path.join(dirName,new_fname)

        os.rename(old_fname_full, new_fname_full)

        writer_date.writerow( [submit_time, fname, new_fname, new_fname_full] )