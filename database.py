import sqlite3

import secrets
import datetime
import hashlib
import mysql.connector as mariadb
from csv import writer 
import logging
log = logging.getLogger(__name__)

"""
database.py: Does database interactions for the Open Satellite Catalog
"""


""" Generate 32-bit random number """
def generate_user_id():
    return secrets.randbelow(2147483647) # Maximum signed value of SQL INT type

""" Generate 256-bit random number as a string """
def generate_object_id():
    ran = secrets.randbits(256)
    return str(ran)


"""
Database class opens and stores connection to the database.
"""
class Database:
    # Connect to database
    # input: db - name of the database
    def __init__(self, dbname,dbtype,dbhostname,dbusername,dbpassword):
        self._dbname     = dbname
        self._dbtype     = dbtype
        self._dbhostname = dbhostname
        self._dbusername = dbusername
        self._dbpassword = dbpassword

        self._last_observer_id = None
        self._entryList = []
        self._observerDict = {} # Used for INFILE method
        self._obsid = 0
        self._new_observerid = 0

        if self._dbtype == "INFILE": # Make CSV files
            self._f_ParsedIOD =  open(self._dbname + "_ParsedIOD.csv", 'w')
            self._writer_ParsedIOD = writer(self._f_ParsedIOD, dialect='unix')

            self._f_Observer =  open(self._dbname + "_Observer.csv", 'w')
            self._writer_Observer = writer(self._f_Observer, dialect='unix')

        else: # Make database
            if self._dbtype == "sqlserver":
                self.conn = db = mariadb.connect(
                                                host=self._dbhostname,
                                                user=self._dbusername,
                                                passwd=self._dbpassword,
                                                db=self._dbname,
                                                charset='utf8',
                                                use_unicode=True
                                                )
                self.c = self.conn.cursor()

                # Need a cursor for each prepared statement
                self.c_addParsedIOD = self.conn.cursor(prepared=True)
                self.c_addStation_query = None
                self.c_addObserver_query = self.conn.cursor(prepared=True)
                self.c_selectObserver_query = self.conn.cursor(prepared=True)
                self.c_updateObserverNonce_query = self.conn.cursor(prepared=True)
                self.c_updateObserverJWT_query = self.conn.cursor(prepared=True)
                self.c_getObserverNonce_query = self.conn.cursor(prepared=True)
                self.c_getObservationCount_query = self.conn.cursor(prepared=True)
                self.c_getCommunityObservationByYear_query = self.conn.cursor(prepared=True)
                self.c_getCommunityObservationByMonth_query = self.conn.cursor(prepared=True)
                self.c_getObserverCountByID_query = self.conn.cursor(prepared=True)
                self.c_getRecentObservations_query = self.conn.cursor(prepared=True)

            else:
                self.conn = sqlite3.connect(self._dbname)
                self.c = self.conn.cursor()

            # Predefined queries - In the case of sqlserver, prepared statements accelerate / secure import queries
            #  %s only works for sqlserver, ? works for both sqlite and sqlserver
            self.addParsedIOD_query = '''INSERT INTO ParsedIOD
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
            self.addStation_query = None
            self.addObserver_query = '''INSERT INTO Observer VALUES(?,?,?,?,?)'''
            self.selectObserver_query = '''SELECT id FROM Observer WHERE verified LIKE ? LIMIT 1'''
            self.updateObserverNonce_query = '''UPDATE Observer SET nonce=? WHERE id=?'''
            self.updateObserverJWT_query = '''UPDATE Observer SET jwt=?, password=?, WHERE id=?'''
            self.getObserverNonce_query = '''SELECT nonce FROM Observer WHERE id=?'''
            self.getObservationCount_query = '''SELECT object_number, COUNT(object_number) as querycount from ParsedIOD GROUP BY object_number order by querycount DESC'''
            self.getCommunityObservationByYear_query = '''SELECT utc_year, COUNT(*) as querycount from ParsedIOD GROUP BY utc_year order by utc_year ASC'''
            self.getCommunityObservationByMonth_query = '''SELECT utc_month, COUNT(*) as querycount from ParsedIOD GROUP BY utc_month order by utc_month'''
            self.getObserverCountByID_query = '''SELECT id, COUNT(*)from Observer WHERE id=?'''
            self.getRecentObservations_query = '''SELECT * FROM ParsedIOD ORDER BY submitted LIMIT 5'''


    # Generate tables
    def createTables(self):
        print("Creating tables...")

        """ ParsedIOD """
        createquery = '''CREATE TABLE IF NOT EXISTS ParsedIOD (
            obs_id INTEGER PRIMARY KEY,
            submitted  DATETIME(4),
            observer_id    INTEGER, 
            object_number    INTEGER,
            international_designation    CHAR(11),
            station_number    SMALLINT,
            station_status_code    CHAR(1),
            utc_year    SMALLINT,
            utc_month    TINYINT,
            utc_day    TINYINT,
            utc_hour    TINYINT,
            utc_minute    TINYINT,
            utc_second    TINYINT,
            utc_millisecond    SMALLINT,
            time_uncertainty    REAL,
            angle_format_code    CHAR(1),
            epoch_code    CHAR(1),
            ra    REAL,
            az    REAL,
            dec_el_sign    CHAR(1), /* dec appears to be namespace collision */
            declination    REAL,
            elivation    REAL,
            positional_uncertainty    REAL,
            optical_behavior_code    CHAR(1),
            visual_magnitude_sign    CHAR(1),
            visual_magnitude    REAL,
            magnitude_uncertainty    REAL,
            flash_period    REAL,
            iod_string TEXT,
            obsFingerPrint TEXT,
            reference    TEXT
            )''' 
        if (self._dbtype == "sqlserver"):
            createquery = createquery + "CHARSET=utf8;"
        self.c.execute(createquery)

        """ Station """
        createquery = '''CREATE TABLE IF NOT EXISTS Station (
            id    INTEGER PRIMARY KEY,
            latitude    REAL,
            longitude    REAL,
            altitude    SMALLINT
            )'''
        if (self._dbtype == "sqlserver"):
            createquery = createquery + "CHARSET=utf8;"
        self.c.execute(createquery)

        """ TLE """
        createquery = '''CREATE TABLE IF NOT EXISTS TLE (
            tle_id    INTEGER PRIMARY KEY,
            title    TEXT,
            satellite_number    INTEGER,
            classification    TEXT,
            international_designator_year    INTEGER,
            international_designator_launch_number    INTEGER,
            international_designator_piece_of_launch    TEXT,
            epoch_year    INTEGER,
            epoch_day    REAL,
            mean_motion_first_derivative    INTEGER,
            mean_motion_second_derivative    TEXT,
            bstar_drag_term    TEXT,
            element_set_number    INTEGER,
            inclination    REAL,
            right_ascension    REAL,
            eccentricity    INTEGER,
            argument_of_perigee   REAL,
            mean_anomaly    REAL,
            mean_motion    REAL,
            revolution_number    INTEGER
            )'''
        if (self._dbtype == "sqlserver"):
            createquery = createquery + "CHARSET=utf8;"
        self.c.execute(createquery)


        """ Observer """
        createquery = '''CREATE TABLE IF NOT EXISTS Observer (
            id   INTEGER PRIMARY KEY,
            eth_addr	TEXT,
            verified	TEXT,
            reputation	INTEGER,
            reference   TEXT
            )'''
        if (self._dbtype == "sqlserver"):
            createquery = createquery + "CHARSET=utf8;"
        self.c.execute(createquery)

        self.conn.commit()

#######################################################################

    # Add an entry to database
    # input: entry - IOD
    def addParsedIOD(self, entry, observer_id):
        # spotting_id = generate_object_id()
        # print("Spotting ID: ", spotting_id)

        # Create fingerprint string from the time and position data only
        # Should uniquely identify the observation
        # Note that this will have uniqueness problems with people who report time but not position (roll call posts)
        obsFingerPrintString = entry.line[23:64].strip()
        obsFingerPrint = hashlib.md5(obsFingerPrintString.encode('utf-8')).hexdigest()
        #log.debug("%s : %s", obsFingerPrintString, obsFingerPrint)
        self._obsid += 1
        newentryTuple = (
                self._obsid, # Use the AUTO_INCREMENT-ed value
                datetime.datetime.now(),
                observer_id,  # Use the one passed from the function, not our own AUTO_INCREMENT one
                entry.ObjectNumber,
                entry.InternationalDesignation,
                entry.Station,
                entry.StationStatusCode,
                entry.DateTime.year,
                entry.DateTime.month,
                entry.DateTime.day,
                entry.DateTime.hour,
                entry.DateTime.minute,
                entry.DateTime.second,
                entry.DateTime.microsecond/1000,
                entry.TimeUncertainty,
                entry.AngleFormatCode,
                entry.Epoch,
                entry.RA,
                entry.AZ,
                "",
                entry.DEC,
                entry.EL,
                entry.PositionUncertainty,
                entry.OpticalCode,
                "",
                entry.VisualMagnitude,
                entry.MagnitudeUncertainty,
                entry.FlashPeriod,
                entry.line,
                obsFingerPrint,
                ""
                )

        if self._dbtype == "INFILE": # Make CSV files
            self._writer_ParsedIOD.writerow(newentryTuple)
        elif self._dbtype == "sqlite":
            try:
                self.c.execute(self.addParsedIOD_query,newentryTuple)
            except sqlite3.IntegrityError as e:
                log.error("{}".format(e))
        else:
            self._entryList.append(newentryTuple)

        return self._obsid

        # return self.c_addParsedIOD.lastrowid

    def addStation(self, station):
        print("not done yet, get on it")

    def addObserver(self,
            eth_addr, 
            verification,
            reputation,
            first_line):

        self._new_observerid += 1

        observerTuple = (
                self._new_observerid, # Use the AUTO_INCREMENT-ed value
                eth_addr,
                verification,
                reputation,
                first_line
                )
    
        if self._dbtype == "INFILE": # Make CSV files
            self._writer_Observer.writerow(observerTuple)
            self._observerDict[verification] = self._new_observerid
        elif self._dbtype == "sqlite":
            try:
                self.c.execute(self.addObserver_query,observerTuple)
                self.conn.commit()
            except sqlite3.IntegrityError as e:
                log.error("{}".format(e))
        else:
            try:
                self.c_addObserver_query.execute(self.addObserver_query, observerTuple)
            except Exception as e:
                log.error("MYSQL ERROR: {}".format(e))
    
        return self._new_observerid

    ### SELECT OBSERVER ###
    def selectObserver(self, observer_name):
        if self._dbtype == "INFILE": # Manage array
            try:
                results = [self._observerDict[observer_name]]
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.selectObserver_query, [observer_name])
            results = self.c.fetchone()
        else:
            self.c_selectObserver_query.execute(self.selectObserver_query, [observer_name])
            results = self.c_selectObserver_query.fetchone()
        return results

    ### GET OBSERVER NONCE ###
    def getObserverNonce(self, public_address):
        if self._dbtype == "INFILE":
            try:
                results = (self.getObserverNonce_query, [public_address])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.getObserverNonce_query, [public_address])
            results = self.c.fetchone()
        else:
            self.c_getObserverNonce_query.execute(self.getObserverNonce_query, [public_address])
            results = self.c_getObserverNonce_query.fetchone()
        return results

    ### GET OBSERVATION COUNT ###
    def getObservationCount(self):
        if self._dbtype == "INFILE":
            try:
                results = (self.getObservationCount_query, [])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.getObservationCount_query, [])
            results = self.c.fetchone()
        else:
            self.c_getObservationCount_query.execute(self.getObservationCount_query, [])
            results = self.c_getObservationCount_query.fetchone()
        return results

    ### GET COMMUNITY OBSERVATION BY YEAR ###
    def getCommunityObservationByYear(self):
        if self._dbtype == "INFILE":
            try:
                results = (self.getCommunityObservationByYear_query, [])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.getCommunityObservationByYear_query, [])
            results = self.c.fetchall()
        else:
            self.c_getCommunityObservationByYear_query.execute(self.getCommunityObservationByYear_query, [])
            results = self.c_getCommunityObservationByYear.fetchall()
        return results

    ### GET COMMUNITY OBSERVATION BY YEAR ###
    def getCommunityObservationByMonth(self):
        if self._dbtype == "INFILE":
            try:
                results = (self.getCommunityObservationByMonth_query, [])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.getCommunityObservationByMonth_query, [])
            results = self.c.fetchall()
        else:
            self.c_getCommunityObservationByMonth_query.execute(self.getCommunityObservationByMonth_query, [])
            results = self.c_getCommunityObservationByMonth.fetchall()
        return results
    
    ### GET OBSERVER COUNT BY ID ###
    def getObserverCountByID(self, public_address):
        if self._dbtype == "INFILE":
            try:
                results = (self.getObserverCountByID_query, [public_address])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.getObserverCountByID_query, [public_address])
            results = self.c.fetchone()
        else:
            self.c_getObserverCountByID_query.execute(self.getObserverCountByID_query, [public_address])
            results = self.c_getObserverCountByID.fetchone()
        return results

    ### GET RECENT OBSERVATIONS ###
    def getRecentObservations(self):
        if self._dbtype == "INFILE":
            try:
                results = (self.getRecentObservations_query, [])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.getRecentObservations_query, [])
            results = self.c.fetchall()
        else:
            self.c_getRecentObservations_query.execute(self.getRecentObservations_query, [])
            results = self.c_getRecentObservations.fetchall()
        return results

    def commit_db_writes(self):
        if (self._dbtype == "sqlserver"):
            if(len(self._entryList) > 0):
                try: 
                    self.c_addParsedIOD.executemany(self.addParsedIOD_query,self._entryList)
                    self._entryList = []
                except Exception as e:
                    log.error("MYSQL ERROR: {}".format(e))
        if (self._dbtype != "INFILE"):
            self.conn.commit()

#######################################################################

    def clean(self):
        self.conn.close()
