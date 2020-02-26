#!/usr/bin/env python

import os
import sys
from hashlib import md5
from urllib.request import urlopen
from hashlib import md5

import logging
log = logging.getLogger(__name__)

# The following 5 lines are necessary until our modules are public
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
tle_util_path = os.path.join(parentdir, "../trusat-orbit")
sys.path.insert(1,tle_util_path) 

from tle_util import fingerprint_line

sys.path.insert(1,os.path.dirname(currentdir)) 
import database

# Set up database connection or files
CONFIG = os.path.abspath("../../trusat-config.yaml")
db = database.Database(CONFIG)

if (db._dbtype != "INFILE"):
    db.createSATCATtable()

satcat_file_fingerprint = fingerprint_file('data/satcat.txt')
with open('data/satcat.txt') as file:
    entry_batch = 0 
    for line in (file):
        entry_batch += 1
        intl_desg = line[0:11].strip()
        norad_number = int(line[13:18].strip())

        multiple_name_flag = line[19].strip()
        if not multiple_name_flag:
            multiple_name_flag = 0
        else:
            multiple_name_flag = 1

        payload_flag = line[20].strip()
        if not payload_flag:
            payload_flag = 0
        else:
            payload_flag = 1

        ops_status_code = line[21].strip()
        name = line[23:47].strip()
        source = line[49:54].strip()
        launch_date = line[56:66].strip()

        decay_date = line[75:85].strip()
        if not decay_date:
            decay_date = '0000-00-00'

        try:
            orbit_period_minutes = float(line[87:94].strip())
        except ValueError:
            orbit_period_minutes = -1

        try:
            inclination_deg = float(line[96:101])
        except ValueError:
            inclination_deg = -1

        try:
            apogee = int(line[103:109])
        except ValueError:
            apogee = -1

        try:
            perigee = int(line[111:117])
        except ValueError:
            perigee = -1

        try:
            radar_crosssec = float(line[119:127])
        except ValueError:
            radar_crosssec = -1

        orbit_status_code = line[129:132].strip()

        record_fingerprint = fingerprint_line(line)

        satcat_tuple = (intl_desg, norad_number, multiple_name_flag, payload_flag, ops_status_code,
                        name, source, launch_date, decay_date, orbit_period_minutes, inclination_deg,
                        apogee, perigee, radar_crosssec, orbit_status_code, 
                        satcat_file_fingerprint, record_fingerprint)

        satcatid = db.addSATCATentry(satcat_tuple)
        print(satcat_tuple)
        if(entry_batch>100):
            db.commit_TLE_db_writes()
            entry_batch=0
    db.commit_TLE_db_writes()
