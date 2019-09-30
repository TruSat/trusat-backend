#!/usr/bin/env python

from hashlib import md5
import logging
log = logging.getLogger(__name__)

import database
from tle_util import fingerprint_file, fingerprint_line

dbname = 'opensatcat_dev'
dbhostname = 'opensatcat.cvpypmmxjtv1.us-east-2.rds.amazonaws.com'
dbusername = 'chris.lewicki'
dbpassword = ''
dbtype = 'INFILE'
#dbtype = 'sqlite'
#dbtype = 'sqlserver'

# Set up database connection or files
db = database.Database(dbname,dbtype,dbhostname,dbusername,dbpassword)
if (dbtype != "INFILE"):
    db.createUCSSATDBtable()

file_to_import = 'data/UCS_Satellite_Database_4-1-2019.txt'

ucsdb_file_fingerprint = fingerprint_file(file_to_import)
# FIXME: There still appear to be some character encoding issues around "Earth's geomagnetic field"
# Doesn't work with UTF-8 type on import.
with open(file_to_import, 'r', encoding='latin-1') as file:
    entry_batch = 0 
    for line in (file):
        entry_batch += 1
        if (entry_batch == 1):
            continue
        fields = line.split('\t')

        # The source CSV file has many more columns encoded than actual valid data
        good_part = fields[0:35]

        record_fingerprint = fingerprint_line(line)

        ucsdb_tuple = tuple(good_part) + (ucsdb_file_fingerprint, record_fingerprint)

        ucsdbid = db.addUCSDBentry(ucsdb_tuple)
        print(ucsdb_tuple)
        if(entry_batch>100):
            # FIXME: This is not actually the right function call.  Need to make it.
            db.commit_TLE_db_writes()
            entry_batch=0
    db.commit_TLE_db_writes()