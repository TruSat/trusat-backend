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


def get_table_total(db, table):
    # Get total number of database records for reference
    query = f"""SELECT COUNT(*) FROM {table}"""
    db.c.execute(query)
    total = db.c.fetchall()[0][0]
    if (total):
        return total
    else:
        return 0

def get_TLE_process_count(db, Station_queryParams):
    query = """WITH user_obs AS
        (SELECT obs_id FROM ParsedIOD WHERE station_number = %(STATION)s)
        SELECT COUNT(process_id) FROM TLE_process WHERE obs_id IN 
            (SELECT T2.obs_id as id FROM TLE_process T2,user_obs WHERE T2.obs_id = user_obs.obs_id);"""
    db.c.execute(query, Station_queryParams)
    count = db.c.fetchall()[0][0]
    if (count):
        return count
    else:
        return 0

def get_ParsedIOD_count(db, Station_queryParams):    
    query = """SELECT COUNT(obs_id) FROM ParsedIOD WHERE station_number = %(STATION)s"""
    db.c.execute(query, Station_queryParams)
    count = db.c.fetchall()[0][0]
    if (count):
        return count
    else:
        return 0


def opt_out_station(db, Station_queryParams):   
    # Leave the user_id in place in case its useful in the future
    station_null_query = """UPDATE Station SET
        initial = NULL,
        latitude = NULL,
        longitude = NULL,
        elevation_m = NULL,
        name = NULL,
        MPC = NULL,
        details = NULL,
        preferred_format = NULL,
        source_url = NULL,
        notes = NULL,
        opt_out = 1
        WHERE station_num = %(STATION)s
        LIMIT 1;"""
    stoo = db.conn.cursor()
    stoo.execute(station_null_query, Station_queryParams)
    if (stoo.rowcount != 1):
        log.error("User null row count not expected {}".format(stoo.rowcount))
        Station_check = False
    else:
        print("Successfully NULLed station")
        Station_check = True

    return Station_check

try:
    CONFIG = os.path.abspath("../../trusat-config.yaml")
    db = database.Database(CONFIG)
    db.conn.autocommit = False # Turn off autocommit so we can verify/commit results
except: 
    log.error("DB Login credentials not available.")
    sys.exit()

### Put whatever database.py function you want to call after this line

while (True):
    station_string = input("\nEnter station number to purge: ").strip()
    try:
        station_number = int(station_string)
    except ValueError:
        log.error("station must be a numeric value")
        continue

    Station_queryParams = {'STATION': station_number}

    query = """SELECT * FROM Station WHERE station_num = %(STATION)s AND opt_out IS NULL;"""
    db.cdict.execute(query, Station_queryParams)
    result = db.cdict.fetchall()

    if (result and result[0]["user"] is not None):
        user_id = int(result[0]["user"])
    elif(result[0]["user"] is None):
        log.warning("Found station, but no user data for station {}".format(station_number))
        Station_check = opt_out_station(db,Station_queryParams)
        if (Station_check):
            print("Successfully NULLed and opted-out station {}.  Restarting...".format(station_number))
            db.conn.commit()
            continue
        else:
            log.error("Failed to NULL and opt-out station {}.  Restarting".format(station_number))
            continue
    else:
        continue

    if (db.cdict.rowcount > 1):
        log.error("More than one Station row matched for: {}.  Aborting.".format(station_number))
        continue
    else:
        print("Deleting data for Station: {}  User (ID): {} ({})".format(station_number,result[0]["name"],user_id))

    # See if there is more than one station per this user
    query = f"""SELECT GROUP_CONCAT(station_num SEPARATOR ', ') AS stations FROM Station, Observer
        WHERE Station.user = Observer.id
        AND Observer.id = {user_id}
        AND opt_out IS NULL;
        """
    db.c.execute(query)
    result = db.c.fetchall()

    if (len(result) == 1 and result[0][0] is not None):
        User_stations = result[0][0].split(',')
        station_count = len(User_stations)
        if (station_count == 1):
            print("Only one station associated with this user ID.")
        else:
            print("Stations associated with this user: {}".format(User_stations))
    else:
        log.error("Didn't understand User -> Station query result. Restarting...")
        continue

    # Get user record on one line, with emails comma-separated
    query = f"""SELECT Observer.*, GROUP_CONCAT(Observer_email.email SEPARATOR ', ') AS emails 
        FROM Observer,Observer_email 
        WHERE Observer.id = Observer_email.user_id
        AND Observer.id = {user_id}
        GROUP BY Observer.id;"""

    db.cdict.execute(query)
    result = db.cdict.fetchall()

    if (db.cdict.rowcount == 1):
        emails = result[0]["emails"].split(',')
        email_count = len(emails)
        print("Found {} email record(s) - {}".format(email_count,emails))
    elif (db.cdict.rowcount == 0):
        print("No emails associated with this user")
        email_count = 0

    else:
        log.error("Found more than one user that matches station.  Restarting...")
        continue

    # Get current record counts for before/after comparison
    ParsedIOD_total   = get_table_total(db, "ParsedIOD")
    TLE_process_total = get_table_total(db, "TLE_process")

    # Get number of records in TLE_process to delete
    TLE_process_count = get_TLE_process_count(db, Station_queryParams)

    # Get number of records in Parsed_IOD to delete
    ParsedIOD_count = get_ParsedIOD_count(db, Station_queryParams)

    confirm_answer = ParsedIOD_count + TLE_process_count
    print("{} obs in ParsedIOD, {} obs referenced in TLE_process".format(ParsedIOD_count,TLE_process_count))
    print("{} rows total to be deleted.".format(confirm_answer))

    try:
        confirm = int(input("Confirm deletion by entering total number of rows to be deleted: ").strip())
    except ValueError:
        log.error("Did not understand input. Restarting...")
        continue

    if not (confirm == confirm_answer):
        print("Input does not match expected result. Restarting...")
        continue

    ##!!
    ##!! Deletion queries past this point
    ##!!   
    # Use separate cursors so we can commit / rollback the entire group  

    # Only touch the tables if we need to
    if (confirm_answer > 0):
        # There appears to be no way to LIMIT a MULTI TABLE delete
        delete_TLE_process_query = """DELETE FROM TLE_process USING TLE_process
            INNER JOIN ParsedIOD P ON P.obs_id = TLE_process.obs_id 
            WHERE P.station_number = %(STATION)s;"""
        tpc = db.conn.cursor()
        tpc.execute(delete_TLE_process_query, Station_queryParams)
        if (tpc.rowcount != TLE_process_count):
            log.error("TLE_process DELETE count {} does not match expected {}".format(tpc.rowcount,TLE_process_count*2))

        delete_ParsedIOD_query = """DELETE FROM ParsedIOD 
            WHERE station_number = %(STATION)s 
            LIMIT %(ParsedIOD_COUNT)s;"""
        delete_ParsedIOD_queryParams = {'STATION': station_number, 'ParsedIOD_COUNT': ParsedIOD_count}
        pic = db.conn.cursor()
        pic.execute(delete_ParsedIOD_query, delete_ParsedIOD_queryParams)
        if (pic.rowcount != ParsedIOD_count):
            log.error("ParsedIOD DELETE count {} does not match expected {}".format(pic.rowcount,ParsedIOD_count))


    # Get record counts post-delete
    # Get current record counts for before/after comparison
    ParsedIOD_total_post   = get_table_total(db, "ParsedIOD")
    TLE_process_total_post = get_table_total(db, "TLE_process")

    ParsedIOD_delta   = ParsedIOD_total - ParsedIOD_total_post
    TLE_Process_delta = TLE_process_total - TLE_process_total_post

    # Belt and suspenders check that the correct amount of records are gone
    ParsedIOD_delete_check   = True if (ParsedIOD_delta == ParsedIOD_count)     else False 
    TLE_process_delete_check = True if (TLE_Process_delta == TLE_process_count) else False 

    if not ParsedIOD_delete_check:
        log.error("Incorrect number of ParsedIOD records gone. Delta: {}".format(ParsedIOD_delta))

    if not TLE_process_delete_check:
        log.error("Incorrect number of TLE_process records gone. Delta: {}".format(TLE_Process_delta))

    # Belt, suspenders and two-hands check that the correct amount of records are gone
    # These both should be zero
    ParsedIOD_count = get_ParsedIOD_count(db, Station_queryParams)
    TLE_process_count = get_TLE_process_count(db, Station_queryParams)

    Station_check = opt_out_station(db,Station_queryParams)

    if (ParsedIOD_delete_check and TLE_process_delete_check and (ParsedIOD_count==0) and (TLE_process_count == 0) and Station_check):
        log.info("ParsedIOD and TLE_process deletions successful.")
        db.conn.commit()
    else:
        log.error("One or more checks failed... Restarting")
        db.conn.rollback()
        continue

    if (station_count > 1):
        remaining_stations = [int(x) for x in User_stations if int(x) != station_number ]
        print("Remaining stations for user {}: {}".format(user_id, remaining_stations))
    else:
        # Delete User records if we've deleted all the station records

        user_delete_query = """DELETE FROM Observer WHERE id = %(USER_ID)s LIMIT 1;"""
        user_delete_queryParams = {'USER_ID': user_id}
        db.c.execute(user_delete_query, user_delete_queryParams)
        if (db.c.rowcount != 1):
            log.error("User null row count not expected {}".format(db.c.rowcount))
            db.conn.rollback()
        else:
            db.conn.commit()
            print("Successfully deleted Observer")
        if (email_count > 0):
            user_email_delete_query = """DELETE FROM Observer_email WHERE user_id = %(USER_ID)s LIMIT %(EMAIL_COUNT)s;"""
            user_email_delete_queryParams = {'USER_ID': user_id, 'EMAIL_COUNT': email_count}
            db.c.execute(user_email_delete_query, user_email_delete_queryParams)
            if (db.c.rowcount != email_count):
                log.error("User null row count {} not expected {}".format(db.c.rowcount, email_count))
                db.conn.rollback()
            else:
                db.conn.commit()
                print("Successfully deleted {} Observer emails".format(email_count))