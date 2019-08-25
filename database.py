import sqlite3
import mysql.connector as mariadb
from secrets import randbelow, randbits
from datetime import datetime, timedelta
from hashlib import md5
from csv import writer 
import json
import logging
log = logging.getLogger(__name__)

import random # Temporary for faking some results in DEV

"""
database.py: Does database interactions for the Open Satellite Catalog
"""

def generate_user_id():
    """ Generate 32-bit random number """
    return randbelow(2147483647) # Maximum signed value of SQL INT type


def generate_object_id():
    """ Generate 256-bit random number as a string """
    return str(randbits(256))

def stringArrayToJSONArray(string_array):
    json_array = []
    for item in string_array:
        json_array.append(json.loads(item[0]))
    return json_array

def datetime_from_sqldatetime(sql_date_string):
    """ The 4 digit sub-seconds are not the standard 3 or 6, which creates problems with datetime.fromisoformat """
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    return datetime.strptime(sql_date_string, date_format)

# TODO: Add index statements to the appropriate fields when creating the tables
class Database:
    """ Database class opens and stores connection to the database, and performs database operations.

    Connect to database
    inputs:
        dbname     - name of the database
        dbtype     - database type INFILE, sqlserver or sqlite3
        dbhostname - hostname for sqlserver
        dbusernmae - username for sqlserver
        dbpassword - password for sqlserver
    """
    def __init__(self, dbname,dbtype,dbhostname,dbusername,dbpassword):
        self._dbname     = dbname
        self._dbtype     = dbtype
        self._dbhostname = dbhostname
        self._dbusername = dbusername
        self._dbpassword = dbpassword

        self._last_observer_id = None
        self._IODentryList = []
        self._TLEentryList = []
        self._TLEFileDict = {} # Used for INFILE method
        self._observerDict = {} # Used for INFILE method
        self._tle_fingerprintDict = {} # Used for INFILE method
        self._obsid = 0
        self._new_observerid = 0
        self._iod_line_fingerprintDict = {} # Used for INFILE method
        self._tle_file_fingerprintDict = {} # Used for INFILE method
        self._SATCAT_file_fingerprintDict = {} # Used for INFILE method
        self._UCSDB_file_fingerprintDict = {} # Used for INFILE method

        # Account for differences in SQL expressions
        if (self._dbtype == "sqlserver"):
            self.charset_string = "CHARSET=utf8 ENGINE=Aria;"
            self.increment = " AUTO_INCREMENT"
        else:
            self.charset_string = ""
            self.increment = " AUTOINCREMENT"

        if self._dbtype == "INFILE": # Make CSV files
            self._f_ParsedIOD =  open(self._dbname + "_ParsedIOD.csv", 'w')
            self._writer_ParsedIOD = writer(self._f_ParsedIOD, dialect='unix')

            self._f_Observer =  open(self._dbname + "_Observer.csv", 'w')
            self._writer_Observer = writer(self._f_Observer, dialect='unix')

            self._f_TLE = open(self._dbname + "_TLE.csv", 'w')
            self._writer_TLE = writer(self._f_TLE, dialect='unix')

            self._f_TLEFile = open(self._dbname + "_TLEFILE.csv", 'w')
            self._writer_TLEFile = writer(self._f_TLEFile, dialect='unix')

            self._f_SATCAT = open(self._dbname + "_SATCAT.csv", 'w')
            self._writer_SATCAT = writer(self._f_SATCAT, dialect='unix')

            self._f_UCSDB = open(self._dbname + "_UCSDB.csv", 'w')
            self._writer_UCSDB = writer(self._f_UCSDB, dialect='unix')

        elif self._dbtype == "sqlserver":  # Make database
            self.conn = mariadb.connect(
                host=self._dbhostname,
                user=self._dbusername,
                passwd=self._dbpassword,
                db=self._dbname,
                charset='utf8',
                use_unicode=True
                )
            self.c = self.conn.cursor()

            # Need a cursor for each prepared statement
            # TODO: Probably don't need prepared statements for all of these
            self.c_addParsedIOD = self.conn.cursor(prepared=True)
            self.c_addStation_query = None
            self.c_addObserver_query = self.conn.cursor(prepared=True)
            self.c_selectObserver_query = self.conn.cursor(prepared=True)
            self.c_updateObserverNonce_query = self.conn.cursor(prepared=True)
            self.c_updateObserverJWT_query = self.conn.cursor(prepared=True)
            self.c_getObserverNonce_query = self.conn.cursor(prepared=True)
            self.c_getObserverJWT_query = self.conn.cursor(prepared=True)
            self.c_getObservationCount_query = self.conn.cursor(prepared=True)
            self.c_getCommunityObservationByYear_query = self.conn.cursor(prepared=True)
            self.c_getCommunityObservationByMonth_query = self.conn.cursor(prepared=True)
            self.c_getObserverCountByID_query = self.conn.cursor(prepared=True)
            self.c_getRecentObservations_query = self.conn.cursor(prepared=True)
            self.c_selectTLEFile_query = self.conn.cursor(prepared=True)
            self.c_selectTLEFingerprint_query = self.conn.cursor(prepared=True)
            self.c_selectIODFingerprint_query = self.conn.cursor(prepared=True)
            self.c_addTLE_query = self.conn.cursor(prepared=True)
            self.c_addTLEFile_query = self.conn.cursor(prepared=True)
            self.c_addSATCAT_query = self.conn.cursor(prepared=True)
            self.c_addUCSDB_query = self.conn.cursor(prepared=True)
            self.c_selectObserverID_query = self.conn.cursor(prepared=True)
            self.selectObserverID_query = '''SELECT max(id) from Observer'''
            try:
                self.c_selectObserverID_query.execute(self.selectObserverID_query, [])
                self._new_observerid = self.c_selectObserverID_query.fetchone()[0]
            except Exception as e:
                log.error("Could not get ObserverID: {}".format(e))
                self._new_observerid = 0

        else:
            self.conn = sqlite3.connect(self._dbname + ".db")
            self.c = self.conn.cursor()

        # Predefined queries - In the case of sqlserver, prepared statements accelerate / secure import queries
        #  %s only works for sqlserver, ? works for both sqlite and sqlserver
        self.addStation_query = None
        self.addObserver_query = '''INSERT INTO Observer VALUES(?,?,?,?,?)'''
        self.selectObserver_query = '''SELECT id FROM Observer WHERE verified LIKE ? LIMIT 1'''
        self.updateObserverNonce_query = '''UPDATE Observer SET nonce=? WHERE id=?'''
        self.updateObserverJWT_query = '''UPDATE Observer SET jwt=?, password=?, WHERE id=?'''
        self.getObserverNonce_query = '''SELECT nonce FROM Observer WHERE id=?'''
        self.getObserverJWT_query = '''SELECT jwt FROM Observer WHERE eth_addr=?'''
        self.getObservationCount_query = '''SELECT object_number, COUNT(object_number) as querycount from ParsedIOD where valid_position>0 GROUP BY object_number order by querycount DESC'''
        self.getCommunityObservationByYear_query = '''SELECT YEAR(obs_time), COUNT(*) as querycount from ParsedIOD where valid_position>0 GROUP BY YEAR(obs_time) order by YEAR(obs_time) ASC'''
        self.getCommunityObservationByMonth_query = '''SELECT MONTH(obs_time), COUNT(*) as querycount from ParsedIOD where valid_position>0 GROUP BY MONTH(obs_time) order by MONTH(obs_time) ASC'''
        self.getObserverCountByID_query = '''SELECT id, COUNT(*)from Observer WHERE id=?'''
        self.getRecentObservations_query = '''SELECT * FROM ParsedIOD where valid_position>0 ORDER BY obs_time DESC LIMIT 5'''
        self.selectTLEFile_query = '''SELECT file_fingerprint FROM TLEFILE WHERE file_fingerprint LIKE ? LIMIT 1'''
        self.selectTLEFingerprint_query = '''SELECT tle_fingerprint FROM TLE WHERE tle_fingerprint LIKE ? LIMIT 1'''
        self.selectIODFingerprint_query = '''SELECT obsFingerPrint FROM ParsedIOD WHERE obsFingerPrint LIKE ? LIMIT 1'''
        self.addParsedIOD_query = '''INSERT INTO ParsedIOD (
            submitted,
            user_string,
            object_number,
            international_designation,
            station_number,
            station_status_code,
            obs_time_string,
            obs_time,
            time_uncertainty,
            time_standard_code,
            angle_format_code,
            epoch_code,
            epoch,
            ra,
            declination,
            azimuth,
            elevation,
            positional_uncertainty,
            optical_behavior_code,
            visual_magnitude,
            visual_magnitude_high,
            visual_magnitude_low,
            magnitude_uncertainty,
            flash_period,
            remarks,
            iod_type,
            iod_string,
            valid_position,
            message_id,
            obsFingerPrint
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        self.addTLE_query = '''INSERT INTO TLE (
            line0,
            line1,
            line2,
            sat_name,
            satellite_number,
            classification,
            designation,
            epoch,
            mean_motion_derivative,
            mean_motion_sec_derivative,
            bstar,
            ephemeris_type,
            element_set_number,
            inclination,
            inclination_radians,
            raan_degrees,
            raan_radians,
            eccentricity,
            arg_perigee_degrees,
            arg_perigee_radians,
            mean_anomaly_degrees,
            mean_anomaly_radians,
            mean_motion_orbits_per_day,
            mean_motion_radians_per_second,
            orbit_number,
            launch_piece_number,
            analyst_object,
            strict_import,
            tle_fingerprint,
            file_fingerprint
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        self.addTLEFile_query = '''INSERT INTO TLEFILE (file_fingerprint, source_filename) VALUES (?,?)'''
        self.addSATCAT_query = '''INSERT INTO celestrak_SATCAT (
            intl_desg,
            norad_num,
            multiple_name_flag,
            payload_flag,
            ops_status_code,
            name,
            source,
            launch_date,
            decay_date,
            orbit_period_minutes,
            inclination_deg,
            apogee,
            perigee,
            radar_crosssec,
            orbit_status_code,
            line_fingerprint,
            file_fingerprint) VALUES
            (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

        self.addUCSDB_query = '''INSERT INTO ucs_SATDB (
            name,
            country_registered,
            country_owner,
            owner_operator,
            users,
            purpose,
            purpose_detailed,
            orbit_class,
            orbit_type,
            GEO_longitude,
            perigee_km,
            apogee_km,
            eccentricity,
            inclination_degrees,
            period_minutes,
            launch_mass_kg,
            dry_mass_kg,
            power_watts,
            launch_date,
            expected_lifetime_years,
            contractor,
            contractor_country,
            launch_site,
            launch_vehicle,
            international_designator,
            norad_number,
            comments,
            detailed_comments,
            source_1,
            source_2,
            source_3,
            source_4,
            source_5,
            source_6,
            source_7,
            line_fingerprint,
            file_fingerprint) VALUES
            (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''


    def createObsTables(self):
        """ Generate Observation tables """
        log.info("Creating Observation tables...")

        """ ParsedIOD """
        createquery = '''CREATE TABLE IF NOT EXISTS ParsedIOD (
            obs_id                      INT NOT NULL ''' + self.increment + ''',
            submitted                   DATETIME,   
            user_string                 TEXT, 
            object_number               MEDIUMINT(5) UNSIGNED,
            international_designation   VARCHAR(14),
            station_number              SMALLINT(4) UNSIGNED NOT NULL,
            station_status_code         CHAR(1),
            obs_time_string             VARCHAR(27),
            obs_time                    DATETIME(4),
            time_uncertainty            FLOAT,
            time_standard_code          TINYINT,
            angle_format_code           CHAR(1),
            epoch_code                  CHAR(1),
            epoch                       SMALLINT,
            ra                          DOUBLE,
            declination                 DOUBLE, /* dec appears to be namespace collision */
            azimuth                     DOUBLE,
            elevation                   DOUBLE,
            positional_uncertainty      DOUBLE,
            optical_behavior_code       CHAR(1),
            visual_magnitude            FLOAT,
            visual_magnitude_high       FLOAT,
            visual_magnitude_low        FLOAT,
            magnitude_uncertainty       FLOAT,
            flash_period                FLOAT,
            remarks                     TEXT,
            iod_type                    VARCHAR(3),
            iod_string                  TEXT NOT NULL,
            valid_position              BOOL,
            message_id                  TEXT,
            obsFingerPrint              CHAR(32) NOT NULL UNIQUE,
            import_timestamp            TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            PRIMARY KEY (`obs_id`),
            UNIQUE KEY `ParsedIOD_obsFingerPrint_idx` (`obsFingerPrint`),
            KEY `ParsedIOD_user_string_40_idx` (`user_string`(40)) USING BTREE,
            KEY `ParsedIOD_object_number_idx` (`object_number`) USING BTREE,
            KEY `ParsedIOD_international_designation_idx` (`international_designation` (14)) USING BTREE,
            KEY `ParsedIOD_station_number_idx` (`station_number`) USING BTREE,
            KEY `ParsedIOD_obs_time_idx` (`obs_time`) USING BTREE,
            KEY `ParsedIOD_valid_position_idx` (`valid_position`) USING BTREE
            )''' + self.charset_string
        self.c.execute(createquery)

        # Requires setting log_bin_trust_function_creators=1 on the AWS RDS instance
        # https://stackoverflow.com/a/30874794
        # Note we're counting on iod.py to set object_number to 0 if it is not available (UK/RDE formats)
        create_trigger_query = """CREATE TRIGGER IF NOT EXISTS add_object_number
            BEFORE INSERT ON ParsedIOD FOR EACH ROW 
            BEGIN
                IF NEW.object_number = 0 THEN 
                    SET NEW.object_number = (
                    SELECT celestrak_SATCAT.norad_num from celestrak_SATCAT
                    WHERE NEW.international_designation = celestrak_SATCAT.intl_desg LIMIT 1);
                END IF;
            END;"""
        self.c.execute(create_trigger_query)

        # Note we're counting on iod.py to set international designation to "?" if it's questionable
        create_trigger_query = """CREATE TRIGGER IF NOT EXISTS add_international_designation
            BEFORE INSERT ON ParsedIOD FOR EACH ROW 
            BEGIN
                IF NEW.international_designation = "?" THEN 
                    SET NEW.international_designation = (
                    SELECT celestrak_SATCAT.intl_desg from celestrak_SATCAT
                    WHERE NEW.object_number = celestrak_SATCAT.norad_num LIMIT 1);
                END IF;
            END;"""
        self.c.execute(create_trigger_query)

        """ Station """
        createquery = """CREATE TABLE IF NOT EXISTS Station (
            station_num INT UNSIGNED NOT NULL,
            initial TINYTEXT,
            latitude FLOAT,
            longitude FLOAT,
            elevation_m SMALLINT(4),
            name TINYTEXT,
            MPC TINYTEXT,
            details TINYTEXT,
            preferred_format TINYTEXT,
            source_url TINYTEXT,
            notes TINYTEXT,
            user INT,
            KEY Station_station_num_idx (station_num) USING BTREE,
            KEY Station_user_idx (user) USING BTREE
            )""" + self.charset_string
        self.c.execute(createquery)

        """ Station Status """
        createquery = """CREATE TABLE IF NOT EXISTS station_status (
            code                ENUM('B','C','E','F','G','O','P','T') NOT NULL,
            short_description   TINYTEXT DEFAULT NULL,
            description         TINYTEXT DEFAULT NULL,
            KEY station_status_code_id (code) USING BTREE
            )""" + self.charset_string
        self.c.execute(createquery)

        """ Station Status contents """
        insertquery = """INSERT INTO station_status (code, short_description, description) VALUES 
            ('E', 'excellent', 'no Moon/clouds, great seeing, minimal air/light pollution'),
            ('G', 'good', 'no Moon/clouds, conditions could be better, but not much'),
            ('F', 'fair     ', 'young/old Moon, some air/light pollution making fainter stars invisible'),
            ('P', 'poor', 'gibbous Moon, haze, more air/light pollution making more stars invisible'),
            ('B', 'bad', 'bright Moon, air/light pollution, some clouds; difficult'),
            ('T', 'terrible', 'bright Moon, air/light pollution, looking through clouds'),
            ('C', 'clouded out', 'station unavailable'),
            ('O', 'sky clear, but observer not available', 'station unavailable');"""
        self.c.execute(insertquery)

        """ Observer """
        createquery = """CREATE TABLE IF NOT EXISTS Observer (
            id          INTEGER PRIMARY KEY''' + self.increment + ''',
            eth_addr    CHAR(42),
            verified    TEXT,
            reputation  INTEGER,
            reference   TEXT,
            nonce       INTEGER,
            jwt         TEXT,
            password    TEXT,
            jwt_secret  CHAR(78),
            KEY `Observer_id_idx` (`id`) USING BTREE,
            KEY `Observer_eth_addr_idx` (`eth_addr`) USING BTREE,
            KEY `Observer_reputation_idx` (`reputation`) USING BTREE
            )""" + self.charset_string
        self.c.execute(createquery)
        self.conn.commit()


    def createTLETables(self):
        log.info("Creating TLE tables...")

        """ TLE """
        createquery = '''CREATE TABLE IF NOT EXISTS TLE (
            tle_id                      INTEGER PRIMARY KEY''' + self.increment + ''',
            line0                       TINYTEXT,
            line1                       TINYTEXT,
            line2                       TINYTEXT,

            sat_name                    TINYTEXT,
            satellite_number            MEDIUMINT NOT NULL,
            classification              CHAR(1),
            designation                 CHAR(24),
            epoch                       DATETIME NOT NULL,
            mean_motion_derivative      DOUBLE,
            mean_motion_sec_derivative  DOUBLE,
            bstar                       DOUBLE,
            ephemeris_type              TINYINT,
            element_set_number          MEDIUMINT,
            inclination                 DOUBLE NOT NULL,
            inclination_radians         DOUBLE,
            raan_degrees                DOUBLE,
            raan_radians                DOUBLE,
            eccentricity                DOUBLE NOT NULL,
            arg_perigee_degrees         DOUBLE,
            arg_perigee_radians         DOUBLE,
            mean_anomaly_degrees        DOUBLE,
            mean_anomaly_radians        DOUBLE,
            mean_motion_orbits_per_day  DOUBLE,
            mean_motion_radians_per_second DOUBLE,
            orbit_number                MEDIUMINT,

            launch_piece_number         SMALLINT,
            analyst_object              BOOL,
            strict_import               BOOL,
            tle_fingerprint             CHAR(32) NOT NULL,
            file_fingerprint            CHAR(32),
            import_timestamp            TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            KEY `TLE_epoch_idx` (`epoch`) USING BTREE,
            KEY `TLE_sat_name_idx` (`sat_name`(24)) USING BTREE,
            KEY `TLE_tle_fingerprint_idx` (`tle_fingerprint`(33)) USING BTREE,
            KEY `TLE_file_fingerprint_idx` (`file_fingerprint`(33)) USING BTREE,
            KEY `TLE_norad_idx` (`satellite_number`) USING BTREE
        )''' + self.charset_string
        self.c.execute(createquery)
        self.conn.commit()

        createquery = '''CREATE TABLE IF NOT EXISTS TLEFILE (
            file_id                 INTEGER PRIMARY KEY''' + self.increment + ''',
            file_fingerprint        CHAR(32) NOT NULL,
            source_filename         TINYTEXT,
            import_timestamp        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            KEY `TLEFILE_file_fingerprint_33_idx` (`file_fingerprint`(33)) USING BTREE
        )''' + self.charset_string
        self.c.execute(createquery)
        self.conn.commit()


    def createSATCATtable(self):
        """ Celestrak SATCAT """
        print("Creating Celestrak SAT CAT table...")

        # TODO: make another table from the multiple_name_flag data in https://celestrak.com/pub/satcat-annex.txt
        createquery = '''CREATE TABLE IF NOT EXISTS celestrak_SATCAT (
            satcat_id               INTEGER ''' + self.increment + ''',
            intl_desg               VARCHAR(11) NOT NULL,
            norad_num               MEDIUMINT UNSIGNED NOT NULL,
            multiple_name_flag      TINYINT(1) UNSIGNED NOT NULL,
            payload_flag            TINYINT(1) UNSIGNED NOT NULL,
            ops_status_code         VARCHAR,
            name                    VARCHAR(24) NOT NULL,
            source                  CHAR(5),
            launch_date             DATE,
            decay_date              DATE,
            orbit_period_minutes    MEDIUMINT,
            inclination_deg         DOUBLE,
            apogee                  DOUBLE,
            perigee                 DOUBLE,
            radar_crosssec          DOUBLE,
            orbit_status_code       CHAR(3),
            line_fingerprint        CHAR(32) NOT NULL,
            file_fingerprint        CHAR(32) NOT NULL,
            import_timestamp        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            PRIMARY KEY (`satcat_id`),
            KEY `celestrak_SATCAT_intl_desg_idx` (`intl_desg`(11)) USING BTREE,
            KEY `celestrak_SATCAT_norad_num_idx` (`norad_num`) USING BTREE,
            KEY `celestrak_SATCAT_name_idx` (`name`) USING BTREE,
            KEY `celestrak_SATCAT_orbit_status_code_idx` (`orbit_status_code`) USING BTREE
        )''' + self.charset_string
        self.c.execute(createquery)

        self.conn.commit()

    def createUCSSATDBtable(self):
        """ Union of Concerned Scientists Satellite Database """
        print("Creating Union of Concerned Scientists Satellite Database table...")

        # FIXME: Need to optimize these auto-gen types
        createquery = '''CREATE TABLE IF NOT EXISTS ucs_SATDB (
            satdb_id              INTEGER PRIMARY KEY''' + self.increment + ''',
            name text DEFAULT NULL,
            country_registered text DEFAULT NULL,
            country_owner text DEFAULT NULL,
            owner_operator text DEFAULT NULL,
            users text DEFAULT NULL,
            purpose text DEFAULT NULL,
            purpose_detailed text DEFAULT NULL,
            orbit_class text DEFAULT NULL,
            orbit_type text DEFAULT NULL,
            GEO_longitude int(11) DEFAULT NULL,
            perigee_km int(11) DEFAULT NULL,
            apogee_km int(11) DEFAULT NULL,
            eccentricity float DEFAULT NULL,
            inclination_degrees float DEFAULT NULL,
            period_minutes int(11) DEFAULT NULL,
            launch_mass_kg int(11) DEFAULT NULL,
            dry_mass_kg text DEFAULT NULL,
            power_watts text DEFAULT NULL,
            launch_date DATE DEFAULT NULL,
            expected_lifetime_years text DEFAULT NULL,
            contractor text DEFAULT NULL,
            contractor_country text DEFAULT NULL,
            launch_site text DEFAULT NULL,
            launch_vehicle text DEFAULT NULL,
            international_designator text DEFAULT NULL,
            norad_number int(11) DEFAULT NULL,
            comments text DEFAULT NULL,
            detailed_comments text DEFAULT NULL,
            source_1 text DEFAULT NULL,
            source_2 text DEFAULT NULL,
            source_3 text DEFAULT NULL,
            source_4 text DEFAULT NULL,
            source_5 text DEFAULT NULL,
            source_6 text DEFAULT NULL,
            source_7 text DEFAULT NULL,
            line_fingerprint        CHAR(32) NOT NULL,
            file_fingerprint        CHAR(32) NOT NULL,
            import_timestamp        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            KEY `ucs_SATDB_satdb_id_idx` (`satdb_id`) USING BTREE,
            KEY `ucs_SATDB_norad_number_idx` (`norad_number`) USING BTREE,
            KEY `ucs_SATDB_international_designator_idx` (`international_designator`(11)) USING BTREE
        )''' + self.charset_string
        self.c.execute(createquery)
        self.conn.commit()


    def addParsedIOD(self, entryList, user_string, submit_time, fast_import = False):
        """ Add an IOD entry to the database """
        for entry in entryList:
            # Create fingerprint string from the time and position data only
            # Should uniquely identify the observation
            # Note that this will have uniqueness problems with people who report time but not position (roll call posts)
            if (entry.IODType == "IOD"):
                obsFingerPrintString = entry.line[23:64].strip()
            elif (entry.IODType == "UK"):
                obsFingerPrintString = entry.line[11:32].strip() + entry.line[33:55].strip()
            elif (entry.IODType == "RDE"):
                obsFingerPrintString = entry.line[14:20].strip() + entry.line[20:24].strip() + entry.line[34:56].strip()
            else:
                log.error("unknown type specified to {}".format(__name__))

            obsFingerPrint = md5(obsFingerPrintString.encode('utf-8')).hexdigest()

            if(self.selectIODFingerprint(obsFingerPrint)):     
                log.warning(" Skipping IOD - fingerprint {} already in database.".format(obsFingerPrint))   
                if (fast_import):
                    log.warning(" ...fast import set, skipping IODs in rest of message.")
                    return False
                else:
                    continue # Already have the IOD
            else:
                newentryTuple = (
                        submit_time,
                        user_string,
                        entry.ObjectNumber,
                        entry.InternationalDesignation,
                        entry.Station,
                        entry.StationStatusCode,
                        entry.DateTimeString,
                        entry.DateTime,
                        entry.TimeUncertainty,
                        entry.TimeStandardCode,
                        entry.AngleFormatCode,
                        entry.EpochCode,
                        entry.Epoch,
                        entry.RA,
                        entry.DEC,
                        entry.AZ,
                        entry.EL,
                        entry.PositionUncertainty,
                        entry.OpticalCode,
                        entry.VisualMagnitude,
                        entry.VisualMagnitude_high,
                        entry.VisualMagnitude_low,
                        entry.MagnitudeUncertainty,
                        entry.FlashPeriod,
                        entry.Remarks,
                        entry.IODType,
                        entry.line,
                        entry.ValidPosition,
                        entry.message_id,
                        obsFingerPrint,
                        )

                if self._dbtype == "INFILE": # Make CSV files
                    self._writer_ParsedIOD.writerow(newentryTuple)
                elif self._dbtype == "sqlite":
                    try:
                        self.c.execute(self.addParsedIOD_query,newentryTuple)
                    except sqlite3.IntegrityError as e:
                        log.error("{}".format(e))
                else:
                    self._IODentryList.append(newentryTuple)
        return len(self._IODentryList)
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


    def addTLE(self, entry):
        """ Add an TLE entry to the database """
        self._tleid = 0 # Set this as a variable in case we want to generate out own in the future
        newentryTuple = (
            entry.line0,
            entry.line1,
            entry.line2,

            entry.name,
            entry.sat_num,
            entry.classification,
            entry.designation,
            entry.epoch_string,
            entry.mean_motion_derivative,
            entry.mean_motion_sec_derivative,                
            entry.bstar,
            entry.ephemeris_type,
            entry.element_num,
            entry.inclination_degrees,
            entry.inclination_radians,
            entry.raan_degrees,
            entry.raan_radians,

            entry.eccentricity,
            entry.arg_perigee_degrees,
            entry.arg_perigee_radians,
            entry.mean_anomaly_degrees,
            entry.mean_anomaly_radians,
            entry.mean_motion_orbits_per_day,
            entry.mean_motion_radians_per_second,
            entry.orbit_num,

            entry.launch_piece_number,
            entry.analyst_object,
            entry.strict,

            entry.tle_fingerprint,
            entry._tle_file_fingerprint
            )

        if self._dbtype == "INFILE": # Make CSV files
            self._writer_TLE.writerow(newentryTuple)
        elif self._dbtype == "sqlite":
            try:
                self.c.execute(self.addTLE_query,newentryTuple)
            except sqlite3.IntegrityError as e:
                log.error("{}".format(e))
        else:
            self._TLEentryList.append(newentryTuple)
        return self._tleid


    def addTLEFile(self, entry):
        """ Add an TLE file entry to the database """
        self._tlefileid = 0 # Set this as a variable in case we want to generate our own in the future

        # self._tlefileid, # Use the AUTO_INCREMENT-ed value
        newentryTuple = (
                entry.file_fingerprint,
                entry._tle_basename
                )

        if self._dbtype == "INFILE": # Make CSV files
            self._writer_TLEFile.writerow(newentryTuple)
            self._TLEFileDict[entry.file_fingerprint] = entry._tle_basename
        elif self._dbtype == "sqlite":
            try:
                self.c.execute(self.addTLEFile_query,newentryTuple)
                self.conn.commit()
            except sqlite3.IntegrityError as e:
                log.error("{}".format(e))
        else:
            try:
                self.c_addTLEFile_query.execute(self.addTLEFile_query, newentryTuple)
            except Exception as e:
                log.error("MYSQL ERROR: {}".format(e))
        return True


    def addSATCATentry(self, newentryTuple):
        """ Add an SATCAT entry to the database """
        self._satcatid = 0 # Set this as a variable in case we want to generate our own in the future

        if self._dbtype == "INFILE": # Make CSV files
            self._writer_SATCAT.writerow(newentryTuple)
#            self._SATCAT_file_fingerprintDict[entry.satcat_file_fingerprint] = _satcat_basename
        elif self._dbtype == "sqlite":
            try:
                self.c.execute(self.addSATCAT_query, newentryTuple)
                self.conn.commit()
            except sqlite3.IntegrityError as e:
                log.error("{}".format(e))
        else:
            try:
                self.c_addSATCAT_query.execute(self.addSATCAT_query, newentryTuple)
            except Exception as e:
                log.error("MYSQL ERROR: {}".format(e))
        return True


    def addUCSDBentry(self, newentryTuple):
        """ Add an UCS DB entry to the database """
        self._satcatid = 0 # Set this as a variable in case we want to generate our own in the future

        if self._dbtype == "INFILE": # Make CSV files
            self._writer_UCSDB.writerow(newentryTuple)
#            self._UCSDB_file_fingerprintDict[entry.satcat_file_fingerprint] = _satcat_basename
        elif self._dbtype == "sqlite":
            try:
                self.c.execute(self.addUCSDB_query, newentryTuple)
                self.conn.commit()
            except sqlite3.IntegrityError as e:
                log.error("{}".format(e))
        else:
            try:
                self.c_addUCSDB_query.execute(self.addUCSDB_query, newentryTuple)
            except Exception as e:
                log.error("MYSQL ERROR: {}".format(e))
        return True


    def selectObserver(self, observer_name):
        """ Look up an observer by (name/email string) in database or internal dictionary"""
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

    def getObserverNonce(self, public_address):
        """ GET OBSERVER NONCE """
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

    def getObserverJWT(self, public_address):
        """ GET OBSERVER NONCE """
        if self._dbtype == "INFILE":
            try:
                results = (self.getObserverJWT_query, [public_address])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.getObserverJWT_query, [public_address])
            results = self.c.fetchone()
        else:
            self.c_getObserverJWT_query.execute(self.getObserverJWT_query, [public_address])
            results = self.c_getObserverJWT_query.fetchone()
            self.conn.commit()
        return results

    def getObservationCount(self):
        """ GET OBSERVATION COUNT """
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

    def getCommunityObservationByYear(self):
        """ GET COMMUNITY OBSERVATION BY YEAR """
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
            results = self.c_getCommunityObservationByYear_query.fetchall()
        return results

    def getCommunityObservationByMonth(self):
        """ GET COMMUNITY OBSERVATION BY YEAR """
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
            results = self.c_getCommunityObservationByMonth_query.fetchall()
        return results
    
    def getObserverCountByID(self, public_address):
        """ GET OBSERVER COUNT BY ID """
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
            results = self.c_getObserverCountByID_query.fetchone()
        return results

    def getRecentObservations(self):
        """ GET RECENT OBSERVATIONS """
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
            results = self.c_getRecentObservations_query.fetchall()
        return results        


    def selectTLEFile(self, tle_file_fingerprint):
        """Query to see if a TLE file is already in the database."""
        if self._dbtype == "INFILE": # Manage array
            if (tle_file_fingerprint not in self._tle_file_fingerprintDict):
                results = None
            else:
                results = self._tle_file_fingerprintDict[tle_file_fingerprint]
        elif self._dbtype == "sqlite":
            self.c.execute(self.selectTLEFile_query, [tle_file_fingerprint])
            results = self.c.fetchone()
        else:
            self.c_selectTLEFile_query.execute(self.selectTLEFile_query, [tle_file_fingerprint])
            results = self.c_selectTLEFile_query.fetchone()
        return results


    def selectTLEFingerprint(self, tle_fingerprint):
        """Query to see if a specific TLE is already in the database"""
        if self._dbtype == "INFILE": # Manage array
            if (tle_fingerprint not in self._tle_fingerprintDict):
                results = None
            else:
                results = self._tle_fingerprintDict[tle_fingerprint]
        elif self._dbtype == "sqlite":
            self.c.execute(self.selectTLEFingerprint_query, [tle_fingerprint])
            results = self.c.fetchone()
        else:
            self.c_selectTLEFingerprint_query.execute(self.selectTLEFingerprint_query, [tle_fingerprint])
            results = self.c_selectTLEFingerprint_query.fetchone()
        return results

    def selectIODFingerprint(self, iod_fingerprint):
        """Query to see if a specific IOD is already in the database"""
        if self._dbtype == "INFILE": # Manage array
            if (iod_fingerprint not in self._iod_line_fingerprintDict):
                results = None
            else:
                results = self._iod_line_fingerprintDict[iod_fingerprint]
        elif self._dbtype == "sqlite":
            self.c.execute(self.selectIODFingerprint_query, [iod_fingerprint])
            results = self.c.fetchone()
        else:
            self.c_selectIODFingerprint_query.execute(self.selectIODFingerprint_query, [iod_fingerprint])
            results = self.c_selectIODFingerprint_query.fetchone()
        return results


    def selectTLEEpochBeforeDate(self, query_epoch_datetime, satellite_number):
        """Query to return the first TLE with epoch prior to specified date for a specific satellite number"""
        self.selectTLEEpochBeforeDate_query = "SELECT * FROM TLE WHERE epoch <= '{}' AND satellite_number={} ORDER BY epoch DESC LIMIT 1".format(query_epoch_datetime, satellite_number)
        self.c.execute(self.selectTLEEpochBeforeDate_query)
        return self.c.fetchone()

    def selectTLEEpochNearestDate(self, query_epoch_datetime, satellite_number):
        """Query to return the nearest TLE with epoch for a specific satellite for a specified date"""
        self.selectTLEEpochNearestDate_query = "SELECT *,ABS(TIMEDIFF(epoch,'{}')) as diff FROM TLE where satellite_number={} ORDER BY diff ASC LIMIT 1".format(query_epoch_datetime, satellite_number)
        self.c.execute(self.selectTLEEpochNearestDate_query)
        return self.c.fetchone()

    def selectTLEEpochNearestDate(self, query_epoch_datetime, satellite_number):
        """Query to return the nearest TLE with epoch for a specific satellite for a specified date"""
        self.selectTLEEpochNearestDate_query = "SELECT *,ABS(TIMEDIFF(epoch,'{}')) as diff FROM TLE where satellite_number={} ORDER BY diff ASC LIMIT 1".format(query_epoch_datetime, satellite_number)
        self.c.execute(self.selectTLEEpochNearestDate_query)
        return self.c.fetchone()

    def selectObservationHistory_JSON(self):
        # TODO Figure out from John if this is user-specific or what the history is in context of
        query_tmp = """SELECT Json_Object('
            time_submitted',ParsedIOD.obs_time,
            'object_name',celestrak_SATCAT.name,
            'right_ascension', ParsedIOD.ra,
            'declination', ParsedIOD.declination,
            'conditions', station_status.short_description)
            FROM ParsedIOD
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.norad_num 
            LEFT JOIN station_status ON ParsedIOD.station_status_code = station_status.code
            WHERE valid_position = 1
            ORDER BY obs_time DESC LIMIT 10;"""
        self.c.execute(query_tmp)
        return stringArrayToJSONArray(self.c.fetchall())

    def selectObjectsObserved_JSON(self):
        # TODO Figure out from John if this is user-specific or what the history is in context of
        query_tmp = """SELECT Json_Object(
            'object_origin', ucs_SATDB.country_owner,
            'primary_purpose', ucs_SATDB.purpose,
            'object_type', ucs_SATDB.purpose_detailed,
            'secondary_purpoase', 'Secondary purpose does not exist, the variable is also misspelled.',
            'observation_quality', ParsedIOD.station_status_code,
            'time_last_tracked',ParsedIOD.obs_time,
            'username_last_tracked',ParsedIOD.user_string) 
            FROM ParsedIOD
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number=ucs_SATDB.norad_number
            WHERE valid_position = 1
            ORDER BY obs_time DESC limit 10;"""
        self.c.execute(query_tmp)
        return stringArrayToJSONArray(self.c.fetchall())

    # /catalog/priorities
    # https://consensys-cpl.atlassian.net/browse/MVP-323
    def selectCatalog_Priorities_JSON(self):
        # TODO: No priorities in database yet, just sort by reverse obs order for something interesting/different to look at
        query_tmp = """select Json_Object(
            'object_norad_number', ParsedIOD.object_number, 
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner, 
            'object_type', ucs_SATDB.purpose, 
            'object_purpose', ucs_SATDB.purpose_detailed, 
            'time_last_tracked', ParsedIOD.obs_time,
            'address_last_tracked', Observer.eth_addr,
            'username_last_tracked',Observer.name) 
            /* Version using inner joins - which theoretically return values which aren't in ucs_SATDB */
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num
			JOIN Observer ON Station.user = Observer.id
			LEFT JOIN ucs_SATDB ON ParsedIOD.object_number = ucs_SATDB.norad_number
			LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            WHERE ParsedIOD.valid_position = 1 
            ORDER BY obs_time DESC LIMIT 100;"""

            # Original version:
            # FROM ucs_SATDB,celestrak_SATCAT,ParsedIOD,Observer,Station 
            # WHERE ParsedIOD.object_number = ucs_SATDB.norad_number
            # AND ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            # AND ParsedIOD.station_number = Station.station_num
            # AND Station.user = Observer.id
            # AND ParsedIOD.valid_position = 1 order by obs_time ASC limit 100;"""

        self.c.execute(query_tmp)
        return stringArrayToJSONArray(self.c.fetchall())

    # /catalog/undisclosed
    # https://consensys-cpl.atlassian.net/browse/MVP-324
    def selectCatalog_Undisclosed_JSON(self):
        query_tmp = """select Json_Object(
            'object_norad_number', ParsedIOD.object_number, 
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner, 
            'object_type', ucs_SATDB.purpose, 
            'object_purpose', ucs_SATDB.purpose_detailed, 
            'time_last_tracked', ParsedIOD.obs_time,
            'address_last_tracked', Observer.eth_addr,
            'username_last_tracked',Observer.name) 
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num
			JOIN ucs_SATDB ON ParsedIOD.object_number = ucs_SATDB.norad_number
			JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
			JOIN Observer ON Station.user = Observer.id
            WHERE ParsedIOD.valid_position = 1 
            AND celestrak_SATCAT.orbit_status_code = 'NEA'
            GROUP BY ParsedIOD.object_number
            ORDER BY obs_time DESC LIMIT 100;"""

            ## Previous query format
            # FROM ucs_SATDB,celestrak_SATCAT,ParsedIOD,Observer,Station 
            # WHERE ParsedIOD.object_number = ucs_SATDB.norad_number
            # AND ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            # AND ParsedIOD.station_number = Station.station_num
            # AND Station.user = Observer.id
            # AND celestrak_SATCAT.orbit_status_code = 'NEA'
            # AND ParsedIOD.valid_position = 1 order by obs_time DESC limit 100;"""

        self.c.execute(query_tmp)
        return stringArrayToJSONArray(self.c.fetchall())

    # /catalog/debris
    # https://consensys-cpl.atlassian.net/browse/MVP-325
    def selectCatalog_Debris_JSON(self):
        query_tmp = """select Json_Object(
            'object_norad_number', ParsedIOD.object_number, 
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner, 
            'object_type', ucs_SATDB.purpose, 
            'object_purpose', ucs_SATDB.purpose_detailed, 
            'time_last_tracked', ParsedIOD.obs_time,
            'address_last_tracked', Observer.eth_addr,
            'username_last_tracked',Observer.name) 
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num
            JOIN Observer ON Observer.id = Station.user
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number = ucs_SATDB.norad_number
            WHERE ParsedIOD.valid_position = 1 
            AND celestrak_SATCAT.name LIKE '%DEB%'
            GROUP BY ParsedIOD.object_number
            ORDER BY obs_time DESC LIMIT 100;"""
        self.c.execute(query_tmp)
        return stringArrayToJSONArray(self.c.fetchall())

    # /catalog/latest
    # https://consensys-cpl.atlassian.net/browse/MVP-326
    def selectCatalog_Latest_JSON(self):
        now = datetime.utcnow()
        date_delta = now - timedelta(days=365)
        launch_date_string  = date_delta.strftime("%Y-%m-%d")

        query_tmp = """select Json_Object(
            'object_norad_number', ParsedIOD.object_number, 
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner, 
            'object_type', ucs_SATDB.purpose, 
            'object_purpose', ucs_SATDB.purpose_detailed, 
            'time_last_tracked', ParsedIOD.obs_time,
            'address_last_tracked', Observer.eth_addr,
            'username_last_tracked',Observer.name) 
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num
            JOIN Observer ON Observer.id = Station.user
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number = ucs_SATDB.norad_number
            WHERE ParsedIOD.valid_position = 1 
            AND celestrak_SATCAT.launch_date > {}
            ORDER BY obs_time DESC LIMIT 100;""".format(launch_date_string)
        self.c.execute(query_tmp)
        return stringArrayToJSONArray(self.c.fetchall())

    # /catalog/all 
    # https://consensys-cpl.atlassian.net/browse/MVP-327
    def selectCatalog_All_JSON(self):
        query_tmp = """select Json_Object(
            'object_norad_number', ParsedIOD.object_number, 
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner, 
            'object_type', ucs_SATDB.purpose, 
            'object_purpose', ucs_SATDB.purpose_detailed, 
            'time_last_tracked', ParsedIOD.obs_time,
            'address_last_tracked', Observer.eth_addr,
            'username_last_tracked',Observer.name) 
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num
            JOIN Observer ON Station.user = Observer.id
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number = ucs_SATDB.norad_number
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            WHERE ParsedIOD.valid_position = 1
            ORDER BY obs_time DESC LIMIT 100;"""
        self.c.execute(query_tmp)
        return stringArrayToJSONArray(self.c.fetchall())

    # /object/info/
    # https://consensys-cpl.atlassian.net/browse/MVP-329
    def selectObjectInfo_JSON(self, norad_num):
        info_url = "https://www.heavens-above.com/SatInfo.aspx?satid={}".format(norad_num)
        quality = random.randint(1,99)

        # Get user-related info first
        query_tmp_count = """SELECT COUNT(Observer.id), Observer.eth_addr, Observer.name, ParsedIOD.obs_time
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num 
            JOIN Observer ON Observer.id = Station.user 
            WHERE ParsedIOD.object_number = {}
            GROUP BY Observer.id
            ORDER BY ParsedIOD.obs_time DESC
            LIMIT 1;""".format(norad_num)
        self.c.execute(query_tmp_count)
        try:
            (user_count, eth_addr, name, last_tracked) = self.c.fetchone()
        except:
            return None

        # Get object info and patch in user-info
        query_tmp = """select Json_Object(
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner, 
            'object_type', ucs_SATDB.purpose, 
            'object_purpose', ucs_SATDB.purpose_detailed, 
            'object_secondary_purpose', ucs_SATDB.comments,
            'year_launched', celestrak_SATCAT.launch_date,
            'time_last_tracked', ParsedIOD.obs_time,
            'number_users_tracked', '{COUNT}',
            'time_last_tracked', '{LAST_TRACKED}',
            'address_last_tracked', '{ETH_ADDR}',
            'username_last_tracked', '{NAME}',
            'observation_quality', '{QUALITY}',
            'object_background', ucs_SATDB.detailed_comments,
            'heavens_above_url', '{URL}'
            ) 
            FROM ParsedIOD 
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number = ucs_SATDB.norad_number
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            WHERE ParsedIOD.valid_position = 1 
            AND ParsedIOD.object_number = {NORAD_NUM}
            LIMIT 1;""".format(COUNT=user_count, LAST_TRACKED=last_tracked, ETH_ADDR=eth_addr, NAME=name, QUALITY=quality, URL=info_url, NORAD_NUM=norad_num)
        self.c.execute(query_tmp)
        try:
            return self.c.fetchone()
        except:
            return None

    # https://consensys-cpl.atlassian.net/browse/MVP-208
    # Create TLE endpoints
    # FIXME - This is the latest of everything in the catalog - but some will be old from McCants stuff because they were dropped from classfd.tle
    def selectTLE_Astriagraph(self):
        query_tmp = """SELECT line0, line1, line2, satellite_number
            FROM TLE 
            GROUP BY satellite_number
            ORDER BY TLE.epoch DESC;"""
        self.c.execute(query_tmp)
        result = ""
        for (line0, line1, line2, _) in self.c.fetchall():
            result = result + "{}\n{}\n{}\n".format(line0,line1,line2)
        return result

    # https://consensys-cpl.atlassian.net/browse/MVP-208
    # Create TLE endpoints
    # FIXME - This will output TLEs view route testing, but not a sorted, latest list.
    def selectTLE_single(self, norad_num):
        query_tmp = """SELECT line0, line1, line2 
            FROM TLE 
            WHERE satellite_number={}
            ORDER BY EPOCH DESC
            LIMIT 1;""".format(norad_num)
        self.c.execute(query_tmp)
        try:
            (line0, line1, line2) = self.c.fetchone()
            return "{}r\n{}\n{}\n".format(line0,line1,line2)
        except:
            return None;



    def commit_TLE_db_writes(self):
        """Process a stored query batch for all the TLEs in a file at once.

        Note that for large TLEs (50,000 entries, we might want to batch this at 1,000 per per something)
        That's not an issue for the small McCants files
        """
        if (self._dbtype == "sqlserver"):
            if(len(self._TLEentryList) > 0):
                try: 
                    self.c_addTLE_query.executemany(self.addTLE_query,self._TLEentryList)
                    self._TLEentryList = []
                except Exception as e:
                    log.error("MYSQL ERROR: {}".format(e))
        if (self._dbtype != "INFILE"):
            self.conn.commit()


    def commit_IOD_db_writes(self):
        if (self._dbtype == "sqlserver"):
            while(len(self._IODentryList) > 0):
                try: 
                    self.c_addParsedIOD.executemany(self.addParsedIOD_query,self._IODentryList)
                    self._IODentryList = []
                except Exception as e:
                    log.error("MYSQL ERROR: {}".format(e))
                    # FIXME - (Work in progress) - try to get rid of duplicate entry in a executemany list
                    if ("Duplicate Entry" in e):
                        mysql_error_tuple = e.split(' ')
                        # FIXME - This is fragile
                        duplicate_fingerprint = mysql_error_tuple[6].strip("'")
                        row = 0
                        # FIXME - Don't know if this will work for the whole tuple, or if I have to find the element
                        for entry in observerTuple:
                            if duplicate_fingerprint in entry:
                                observerTuple.remove(row)
                            row += 1

        if (self._dbtype != "INFILE"):
            self.conn.commit()


    def clean(self):
        self.conn.close()
