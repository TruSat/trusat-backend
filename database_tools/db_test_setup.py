import os
import sys

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG) 

# The following 5 lines are necessary until our modules are public
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import database

try:
    CONFIG = os.path.abspath("../../trusat-config.yaml")
    db = database.Database(CONFIG)
except: 
    log.error("DB Login credentials not available.")
    sys.exit()

### Put whatever database.py function you want to call after this line

# result = db.selectObjectInfluence_JSON(2173)
# result = db.selectCatalog_All_JSON()
#result = db.selectTLE_all()
# result = db.selectFindObject('Delta')
# result = db.selectFindObject('Dango')
#result = db.selectFindObject('12')
#result = db.selectFindObject(12)
# text_block = "                9999 O 201911011                                                "
# result = db.addObserverParsedIOD(text_block)
query = "SELECT tle_id FROM TLE WHERE line1 LIKE '% 0.%' and classification='T';"

# query = "SELECT tle_id FROM TLE WHERE satellite_number < 10000"

db.c.execute(query)
result = db.c.fetchall()
tle_ids = database.QueryTupleListToList(result)
for tle_id in tle_ids:
    TLE = db.selectTLEid(tle_id)
    print(TLE.line1)
    fp = TLE.tle_fingerprint
    TLE.correct_value_ranges()
    TLE.derived_values()
    TLE.make_tle_lines()
    TLE._fingerprint_tle()
    print(TLE.line1)
    print(fp)
    print(TLE.tle_fingerprint)
    print
    query = """
        UPDATE TLE SET 
        line1 = %(LINE1)s,
        mean_motion_derivative = %(MMD)s,
        tle_fingerprint = %(TLEFP)s
        WHERE tle_id = %(TLEID)s
        LIMIT 1;"""
    query_parms = { 
        "LINE1": TLE.line1,
        "MMD": TLE.mean_motion_derivative,
        "TLEFP": TLE.tle_fingerprint,
        "TLEID": TLE.tle_id
    }
    db.c.execute(query,query_parms)
    db.conn.commit()




