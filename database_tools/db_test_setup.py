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
    with open('../../login.txt', 'r') as f:
        lines = f.readlines()
        dbname = lines[0].strip()
        dbtype = lines[1].strip()
        dbhostname = lines[2].strip()
        dbusername = lines[3].strip()
        dbpassword = lines[4].strip()
except:
    pass
# --- CONSTANTS ---

dbname = dbname or os.getenv('TRUSAT_DATABASE_NAME', None)
dbhostname = dbhostname or os.getenv('TRUSAT_DATABASE_HOST', None)
dbusername = dbusername or os.getenv('TRUSAT_DATABASE_USER', None)
dbpassword = dbpassword or os.getenv('TRUSAT_DATABASE_PASSWORD', "")

dbname or print("No database name specified")
dbhostname or print("No database host specified")
dbusername or print("No database user specified")

try:
    db = database.Database(dbname,dbtype,dbhostname,dbusername,dbpassword)
except: 
    log.error("DB Login credentials not available.")
    sys.exit()

### Put whatever database.py function you want to call after this line

result = db.selectCatalog_Priorities_JSON()

print(result)