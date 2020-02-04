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

result = db.selectCatalog_Priorities_JSON()

print(result)