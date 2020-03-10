import os
import database

CONFIG = os.path.abspath("../trusat-config.yaml")
db = database.Database(CONFIG)

db.createObsTables()
db.createTLETables()
db.create_celestrak_satcat_table()
db.create_ucs_satdb_table()
