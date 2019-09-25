import sqlite3
import mysql.connector as mariadb
from datetime import datetime, timedelta
from hashlib import md5
from csv import writer
import pycountry
import json


# The following 7 lines are necessary until the tle_util module is public
import inspect
import os
import sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
tle_path = os.path.join(parentdir, "trusat-tle")
sys.path.insert(1,tle_path)
import tle_util

# The following 5 lines are necessary until the iod module is public
iod_path = os.path.join(parentdir, "trusat-iod")
sys.path.insert(1,iod_path)
import iod

import logging
log = logging.getLogger(__name__)

"""
database.py: Does database interactions for the Open Satellite Catalog
"""

def QueryRowToJSON(var):
    """ TODO: Kenan to document """
    try:
        return json.dumps(
            json.loads(var[0]),
            sort_keys=False,
            indent=4)
    except:
        return b'{}'

def QueryRowToJSON_JSON(var):
    """ TODO: Kenan to document """
    return json.loads(var[0])

def stringArrayToJSONArray(string_array):
    """ TODO: Kenan to document """
    json_array = []
    for item in string_array:
        json_array.append(json.loads(item[0]))
    return json.dumps(
        json_array,
        sort_keys=False,
        indent=4)

def stringArrayToJSONArray_JSON(string_array):
    """ TODO: Kenan to document """
    json_array = []
    for item in string_array:
        json_array.append(json.loads(item[0]))
    return json_array

def datetime_from_sqldatetime(sql_date_string):
    """ The 4 digit sub-seconds are not the standard 3 or 6, which creates problems with datetime.fromisoformat """
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    return datetime.strptime(sql_date_string, date_format)

def convert_country_names(object_observed):
    """ TODO: Kenan to document """
    for observation in object_observed:
        countries_two_letters = ''
        country_count = 0
        try:
            countries = observation["object_origin"].split("/")
            for country in countries:
                c = pycountry.countries.get(name=country)
                if c == None:
                    c = pycountry.countries.get(alpha_3=country)
                    if c:
                        if country_count == 0:
                            country_count = 1
                            countries_two_letters = c.alpha_2
                        else:
                            countries_two_letters = countries_two_letters + '/' + c.alpha_2
                else:
                    if country_count == 0:
                        country_count = 1
                        countries_two_letters = c.alpha_2
                    else:
                        countries_two_letters = countries_two_letters + '/' + c.alpha_2
            observation["object_origin"] = countries_two_letters
        except:
            observation["object_origin"] = ''
    return

def convert_country_names_single(observation):
    """ TODO: Kenan to document """
    countries_two_letters = ''
    country_count = 0
    try:
        countries = observation["object_origin"].split("/")
        for country in countries:
            c = pycountry.countries.get(name=country)
            if c == None:
                c = pycountry.countries.get(alpha_3=country)
                if c:
                    if country_count == 0:
                        country_count = 1
                        countries_two_letters = c.alpha_2
                    else:
                        countries_two_letters = countries_two_letters + '/' + c.alpha_2
            else:
                if country_count == 0:
                    country_count = 1
                    countries_two_letters = c.alpha_2
                else:
                    countries_two_letters = countries_two_letters + '/' + c.alpha_2
        observation["object_origin"] = countries_two_letters
    except:
        observation["object_origin"] = ''
    return

# We haven't defined a Station class anywhere, so might as well do it here.
class Station:
    """ Class object to contain all the database details for an COSPAR Station record
    """
    def __init__(self):
        self.station_num    = None
        self.initial		= None
        self.latitude		= None
        self.longitude		= None
        self.elevation_m	= None
        self.name			= None
        self.MPC			= None
        self.details		= None
        self.preferred_format = None
        self.source_url		= None
        self.notes			= None
        self.user			= None

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
        self._IODPendingEntryFingerprintList = [] # Used for dupe-checking within an INSERT  batch
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
            self.cdict = self.conn.cursor(dictionary=True)

            # Need a cursor for each prepared statement
            # TODO: Probably don't need prepared statements for all of these
            self.c_addParsedIOD = self.conn.cursor(prepared=True)
            self.c_addStation_query = None
            self.c_addObserver_query = self.conn.cursor(prepared=True)
            self.c_selectObserver_query = self.conn.cursor(prepared=True)
            self.c_updateObserverNonce_query = self.conn.cursor(prepared=True)
            self.c_updateObserverJWT_query = self.conn.cursor(prepared=True)
            self.c_updateObserverUsername_query = self.conn.cursor(prepared=True)
            self.c_updateObserverEmail_query = self.conn.cursor(prepared=True)
            self.c_updateObserverBio_query = self.conn.cursor(prepared=True)
            self.c_updateObserverLocation_query = self.conn.cursor(prepared=True)
            self.c_updateObserverPrivate_query = self.conn.cursor(prepared=True)
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
            self.c_addTLEProcess_query = self.conn.cursor(prepared=True)
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
        self.addObserver_query = '''INSERT INTO Observer(id, eth_addr, name, reputation, reference) VALUES(?,?,?,?,?)'''
        self.selectObserver_query = '''SELECT id FROM Observer WHERE verified LIKE ? LIMIT 1'''
        self.updateObserverNonce_query = '''UPDATE Observer SET nonce=? WHERE eth_addr=?'''
        self.updateObserverJWT_query = '''UPDATE Observer SET jwt=?, password=? WHERE eth_addr=?'''
        self.updateObserverUsername_query = '''UPDATE Observer SET name=? WHERE eth_addr=?'''
        self.updateObserverEmail_query = '''UPDATE Observer SET reference=? WHERE eth_addr=?'''
        self.updateObserverLocation_query = '''UPDATE Observer SET location=? WHERE eth_addr=?'''
        self.updateObserverBio_query = '''UPDATE Observer SET bio=? WHERE eth_addr=?'''
        self.getObserverNonce_query = '''SELECT nonce FROM Observer WHERE eth_addr=?'''
        self.getObserverJWT_query = '''SELECT jwt FROM Observer WHERE eth_addr=?'''
        self.getObservationCount_query = '''SELECT object_number, COUNT(object_number) as querycount from ParsedIOD where valid_position>0 GROUP BY object_number order by querycount DESC'''
        self.getCommunityObservationByYear_query = '''SELECT YEAR(obs_time), COUNT(*) as querycount from ParsedIOD where valid_position>0 GROUP BY YEAR(obs_time) order by YEAR(obs_time) ASC'''
        self.getCommunityObservationByMonth_query = '''SELECT MONTH(obs_time), COUNT(*) as querycount from ParsedIOD where valid_position>0 GROUP BY MONTH(obs_time) order by MONTH(obs_time) ASC'''
        self.getObserverCountByID_query = '''SELECT id, COUNT(*) from Observer WHERE eth_addr=?'''
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
        # TODO: add mean_motion_radians_per_minute from the TLE class to here
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
        self.addTLEProcess_query = '''INSERT INTO TLE_process (
            object_number,
            obs_id,
            tle_source_id,
            tle_result_id,
            aspect,
            cross_track_err,
            time_err,
            position_err,
            obs_weight,
            tle_start_rms,
            tle_result_rms,
            remarks
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
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

    """ TruSat Table Schema overview:
    - ParsedIOD       - Observations from IOD, RDE or UK formats
    - Observer        - User table
    - Observer_email  - User emails
    - Station         - Observation Station details
    - station_status  - Lookup of Character-pack to status description
    - TLE             - Two Line Elements
    - TLEFILE         - File record of externally-source elements (for dupe detection or source traceability)
    - celestrak_SATCAT - Catalog description (externally sourced from Celestrak)
    - ucs_SATDB        - Catalog description (externally sourced from UCS database)
    """

    def createObsTables(self):
        """ Generate Observation tables """
        log.info("Creating Observation tables...")

        """ ParsedIOD """
        createquery = '''CREATE TABLE IF NOT EXISTS ParsedIOD (
            obs_id                      INT NOT NULL ''' + self.increment + ''',    /* Unique internal ID */
            submitted                   DATETIME,                       /* Datetime when the user submitted the observation (receipt time or time of email) */
            user_string                 TEXT,                           /* DEPRECATED email address or other identifier of user */
            object_number               MEDIUMINT(5) UNSIGNED,          /* NORAD number */
            international_designation   VARCHAR(14),                    /* International designation */
            station_number              SMALLINT(4) UNSIGNED NOT NULL,  /* Station number that made observation */
            station_status_code         CHAR(1),        /* Packed code of station status - unpacked in station_status table */
            obs_time_string             VARCHAR(27),    /* Source ascii string for observation time (for IOD.py debugging) */
            obs_time                    DATETIME(4),    /* Exact time of observation */
            time_uncertainty            FLOAT,          /* Observation uncertainty (seconds) */
            time_standard_code          TINYINT,        /* Coded time standard */
            angle_format_code           CHAR(1),        /* Packed code of angle format */
            epoch_code                  CHAR(1),        /* Packed code of angle EPOCH format */
            epoch                       SMALLINT,       /* Decoded EPOCH year */
            ra                          DOUBLE,         /* right ascension (radians) - derived from az/el by iod.py if not provided */
            declination                 DOUBLE,         /* declination of observation (radians) - 'dec' appears to be namespace collision. derived from az/el by iod.py if not provided */
            azimuth                     DOUBLE,         /* azimuth of observation (radians) - derived from ra/dec by iod.py if not provided */
            elevation                   DOUBLE,         /* elevation of observation (radians) - derived from ra/dec by iod.py if not provided */
            positional_uncertainty      DOUBLE,         /* Position uncertainy of observation (radians) */
            optical_behavior_code       CHAR(1),        /* Packed code of optical behavior */
            visual_magnitude            FLOAT,         
            visual_magnitude_high       FLOAT,
            visual_magnitude_low        FLOAT,
            magnitude_uncertainty       FLOAT,
            flash_period                FLOAT,          /* seconds */
            remarks                     TEXT,           /* Any comments right of the formatted portion of the record */
            iod_type                    VARCHAR(3),     /* Source type of Observation: IOD, RDE, UK */
            iod_string                  TEXT NOT NULL,  /* Full / original unparsed observation record */
            valid_position              BOOL,           /* Status flag pertaining to iod.py validity checks */
            message_id                  TEXT,           /* Source mail header message ID (if available) */
            obsFingerPrint              CHAR(32) NOT NULL UNIQUE,   /* Unique MD5 fingerprint of observation */
            import_timestamp            TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, /* Timestamp of DB record creation */
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
        """ Populate the NORAD object number on INSERT by looking up known International Designation """
        create_trigger_query = """CREATE TRIGGER IF NOT EXISTS add_object_number
            BEFORE INSERT ON ParsedIOD FOR EACH ROW
            BEGIN
                IF NEW.object_number = 0 THEN
                    SET NEW.object_number = (
                    SELECT celestrak_SATCAT.norad_num from celestrak_SATCAT
                    WHERE NEW.international_designation = celestrak_SATCAT.intl_desg LIMIT 1);
                END IF;
            END;"""
        try:
            self.c.execute(create_trigger_query)
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            log.warning(e)
            log.warning("You may need to set log_bin_trust_function_creators=1 in your database instance.")

        # Note we're counting on iod.py to set international designation to "?" if it's questionable
        """ Populate the International Designation on INSERT by looking up known NORAD object number """
        create_trigger_query = """CREATE TRIGGER IF NOT EXISTS add_international_designation
            BEFORE INSERT ON ParsedIOD FOR EACH ROW
            BEGIN
                IF NEW.international_designation = "?" THEN
                    SET NEW.international_designation = (
                    SELECT celestrak_SATCAT.intl_desg from celestrak_SATCAT
                    WHERE NEW.object_number = celestrak_SATCAT.norad_num LIMIT 1);
                END IF;
            END;"""
        try:
            self.c.execute(create_trigger_query)
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            log.warning(e)
            log.warning("You may need to set log_bin_trust_function_creators=1 in your database instance.")


        """ TLE_process """
        createquery = '''CREATE TABLE IF NOT EXISTS TLE_process (
            process_id                  INT NOT NULL ''' + self.increment + ''', /* Unique internal ID of observation */
            object_number               MEDIUMINT(5) UNSIGNED,  /* NORAD Num of TLE/Obs */
            obs_id                      INT NOT NULL,           /* ID of observation */
            tle_source_id               INT NOT NULL,           /* ID of starting reference TLE */
            tle_result_id               INT NOT NULL,           /* ID of TLE created with this obs_id */
            aspect                      FLOAT,                  /* degrees */
            cross_track_err             FLOAT,                  /* degrees, left of track is positive */
            time_err                    FLOAT,                  /* seconds */
            position_err                FLOAT,                  /* degrees */
            obs_weight                  FLOAT,                  /* percentage */
            tle_start_rms               FLOAT,                  /* degrees^2 - value of RMS against reference TLE */
            tle_result_rms              FLOAT,                  /* degrees^2 - value of RMS against refined TLE */
            remarks                     TEXT,                   /* Most likely for debugging notes */
            process_timestamp           TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, /* Timestamp of record creation */
            PRIMARY KEY (`process_id`),
            KEY `Process_object_number_idx` (`object_number`) USING BTREE,
            KEY `Process_obs_id_idx`        (`obs_id`)        USING BTREE,
            KEY `Process_tle_source_id_idx` (`tle_source_id`) USING BTREE,
            KEY `Process_tle_result_id_idx` (`tle_result_id`) USING BTREE
            )''' + self.charset_string
        self.c.execute(createquery)


        """ Station Table. These records are a mix of observer identity and station identity. 
        TODO: Will need to provide better separation between Observers / Stations in future releases.
        """
        createquery = """CREATE TABLE IF NOT EXISTS Station (
            station_num INT UNSIGNED NOT NULL,  /* 4 Digit COSPAR number of observation station */
            initial TINYTEXT,                   /* Observer initials */
            latitude FLOAT,                     /* WGS84 Latitude (degrees) */
            longitude FLOAT,                    /* WGS84 Longitude (degrees) */
            elevation_m SMALLINT(4),            /* Elevation above mean sea level (meters) */
            name TINYTEXT,                      /* Name field for station/observer */
            MPC TINYTEXT,                       /* Minor Planet Center observatory code (if available) */
            details TINYTEXT,                   /* Details describing the station */
            preferred_format TINYTEXT,          /* TruSat team notes on observer preferred reporting format IOD/RDE/UK */
            source_url TINYTEXT,                /* URL where confirming data can be found */
            notes TINYTEXT,                     /* TruSat team processing notes */
            user INT,                           /* Associated User table ID */
            KEY Station_station_num_idx (station_num) USING BTREE,
            KEY Station_user_idx (user) USING BTREE,
            KEY Station_user_station_idx (user, station_num)
            )""" + self.charset_string
        self.c.execute(createquery)

        """ Station Status """
        createquery = """CREATE TABLE IF NOT EXISTS station_status (
            code                ENUM('B','C','E','F','G','O','P','T') NOT NULL, /* Single character station status code */
            short_description   TINYTEXT DEFAULT NULL,      /* Terse status description */
            description         TINYTEXT DEFAULT NULL,      /* Full status description */
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
            id          INTEGER PRIMARY KEY''' + self.increment + ''', /* Internal ID  */
            eth_addr    CHAR(42),       /* Ethereum address for user */
            verified    TEXT,           /* DEPRECATED */
            reputation  INTEGER,        /* User rank value */
            reference   TEXT,           /* Internal user ref notes for SeeSat archive */
            nonce       INTEGER,
            jwt         TEXT,
            password    TEXT,
            jwt_secret  CHAR(78),
            location    TINYTEXT,       /* User-specified (publicly visible) location */
            bio         TEXT,           /* User-specified (publicly visible) bio */
            url_profile TEXT,           /* Profile URL - notionally gravitar or similar. FIXME: need to protect for exploits */
            url_image   TEXT,           /* Profile Image URL - notionally gravitar or similar. FIXME: need to protect for exploits */
            KEY `Observer_id_idx` (`id`) USING BTREE,
            KEY `Observer_eth_addr_idx` (`eth_addr`) USING BTREE,
            KEY `Observer_reputation_idx` (`reputation`) USING BTREE
            )""" + self.charset_string
        self.c.execute(createquery)
        self.conn.commit()


    def createTLETables(self):
        log.info("Creating TLE tables...")

        """ TLE """
        # TODO: add mean_motion_radians_per_minute from the TLE class to here
        createquery = '''CREATE TABLE IF NOT EXISTS TLE (
            tle_id                      INTEGER PRIMARY KEY''' + self.increment + ''', /* Internal unique record ID */
            line0                       TINYTEXT,   /* line0/name from TLE */
            line1                       TINYTEXT,   /* line1 of TLE */
            line2                       TINYTEXT,   /* line2 of TLE record */

            sat_name                    TINYTEXT,   /* Name of object (may be same as line0) */
            satellite_number            MEDIUMINT NOT NULL, /* NORAD catalog number */
            classification              CHAR(1),    /* Classification Code - TruSat generated TLEs use T */
            designation                 CHAR(24),   /* International Designator */
            epoch                       DATETIME NOT NULL,  /* FIXME: Python Datetime(?) of TLE epoch */
            mean_motion_derivative      DOUBLE, 
            mean_motion_sec_derivative  DOUBLE,
            bstar                       DOUBLE,
            ephemeris_type              TINYINT,
            element_set_number          MEDIUMINT,
            inclination                 DOUBLE NOT NULL, /* FIXME - need to rename to degrees */
            inclination_radians         DOUBLE, /* Orbit inclination (radians) */
            raan_degrees                DOUBLE, /* Right Ascension of the Ascending Node (degrees) */
            raan_radians                DOUBLE, /* Right Ascension of the Ascending Node (radians) */
            eccentricity                DOUBLE NOT NULL, /* Orbit eccentricity */
            arg_perigee_degrees         DOUBLE, /* Argument of perigee (degrees) */
            arg_perigee_radians         DOUBLE, /* Argument of perigee (radians) */
            mean_anomaly_degrees        DOUBLE, 
            mean_anomaly_radians        DOUBLE,
            mean_motion_orbits_per_day  DOUBLE,
            mean_motion_radians_per_second DOUBLE, /* FIXME - need to at mean_motion_radians_per_minute for SGP4 convenience */
            orbit_number                MEDIUMINT, /* Orbit number since launch */

            launch_piece_number         SMALLINT,  /* Derived number of launch piece (from international desg) */
            analyst_object              BOOL,      /* Flag of whether this is an uncorrelated object */
            strict_import               BOOL,      /* Whether this record was imported / created through strict_import checks */
            tle_fingerprint             CHAR(32) NOT NULL, /* MD5 fingerprint of this record */
            file_fingerprint            CHAR(32),          /* MD5 fingerprint of the file this record was imported from (optional) */
            import_timestamp            TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,   /* Timestamp of record creation */
            KEY `TLE_epoch_idx` (`epoch`) USING BTREE,
            KEY `TLE_sat_name_idx` (`sat_name`(24)) USING BTREE,
            KEY `TLE_tle_fingerprint_idx` (`tle_fingerprint`(33)) USING BTREE,
            KEY `TLE_file_fingerprint_idx` (`file_fingerprint`(33)) USING BTREE,
            KEY `TLE_norad_idx` (`satellite_number`) USING BTREE
        )''' + self.charset_string
        self.c.execute(createquery)
        self.conn.commit()

        createquery = '''CREATE TABLE IF NOT EXISTS TLEFILE (
            file_id                 INTEGER PRIMARY KEY''' + self.increment + ''', /* Unique internal record ID */
            file_fingerprint        CHAR(32) NOT NULL, /* MD5 finger print of file */
            source_filename         TINYTEXT,          /* Name of source file */
            import_timestamp        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, /* Timestamp of record creation */
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
        """ Add an IOD entry to the database         
        Input: IOD-formatted line
        """
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
                log.debug("      Offending entry:\n      {}".format(entry.line))
                if (fast_import):
                    log.warning(" ...fast import set, skipping IODs in rest of message.")
                    return False
                else:
                    continue # Already have the IOD
            elif (obsFingerPrint in self._IODPendingEntryFingerprintList):
                log.warning(" Skipping IOD - fingerprint {} already received this session and pending write to database.".format(obsFingerPrint))
                log.debug("      Offending entry:\n      {}".format(entry.line))
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
                    self._IODPendingEntryFingerprintList.append(obsFingerPrint)
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
                self.conn.commit()
            except Exception as e:
                log.error("MYSQL ERROR: {}".format(e))
        return self._new_observerid


    def addTLE(self, entry):
        """ Add an TLE entry to the database 
        Input: TruSatellite() object """
        # TODO: add mean_motion_radians_per_minute from the TLE class to here
        self._tleid = 0 # Set this as a variable in case we want to generate our own in the future
        newentryTuple = (
            entry.line0,
            entry.line1,
            entry.line2,

            entry.name,
            entry.satellite_number,
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
            entry.orbit_number,

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


    def addTruSatTLE(self, TruSatTLE, TLE_process, tle_source_id, tle_start_rms, tle_result_rms, remarks):
        """ Add an TruSat-derived TLE entry to the database, concurrently with its TLE_process records
        Perform as an atomic commit of all records, or bail.

        Inputs:
         - TruSatTLE - TruSatellite() object
         - TLE_process - Dictionary of IOD.obs_id entries and their corresponding process data

        Outputs:
         - Success/Fail
        """
        TLE_process_list = []

        # TODO: add mean_motion_radians_per_minute from the TLE class to here
        newTLETuple = (
            TruSatTLE.line0,
            TruSatTLE.line1,
            TruSatTLE.line2,

            TruSatTLE.name,
            TruSatTLE.satellite_number,
            TruSatTLE.classification,
            TruSatTLE.designation,
            TruSatTLE.epoch_string,
            TruSatTLE.mean_motion_derivative,
            TruSatTLE.mean_motion_sec_derivative,
            TruSatTLE.bstar,
            TruSatTLE.ephemeris_type,
            TruSatTLE.element_num,
            TruSatTLE.inclination_degrees,
            TruSatTLE.inclination_radians,
            TruSatTLE.raan_degrees,
            TruSatTLE.raan_radians,

            TruSatTLE.eccentricity,
            TruSatTLE.arg_perigee_degrees,
            TruSatTLE.arg_perigee_radians,
            TruSatTLE.mean_anomaly_degrees,
            TruSatTLE.mean_anomaly_radians,
            TruSatTLE.mean_motion_orbits_per_day,
            TruSatTLE.mean_motion_radians_per_second,
            TruSatTLE.orbit_number,

            TruSatTLE.launch_piece_number,
            TruSatTLE.analyst_object,
            TruSatTLE.strict,

            TruSatTLE.tle_fingerprint,
            TruSatTLE._tle_file_fingerprint
            )

        # Insert the TLE first, so that we can include the resulting tle_id as tle_result_id in the table TLE_process
        try:
            self.c_addTLE_query.execute(self.addTLE_query,newTLETuple)
            tle_result_id = self.c_addTLE_query.lastrowid
        except Exception as e:
            log.error("MYSQL ERROR: {}".format(e))
            return False

        for obs_id in TLE_process:
            TLE_process_tuple = (
                TruSatTLE.satellite_number,
                obs_id,
                tle_source_id,
                tle_result_id,
                TLE_process[obs_id]["aspect"],
                TLE_process[obs_id]["cross_track_err"],
                TLE_process[obs_id]["time_err"],
                TLE_process[obs_id]["position_err"],
                TLE_process[obs_id]["obs_weight"],
                tle_start_rms,
                tle_result_rms,
                remarks)
            TLE_process_list.append(TLE_process_tuple)

        try:
            self.c_addTLEProcess_query.executemany(self.addTLEProcess_query,TLE_process_list)
            self.conn.commit()
            return True
        except Exception as e:
            log.error("MYSQL ERROR: {}".format(e))
            return False


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

    #######################
    ### Station-related queries
    #######################
    def getStationsQuery(self, requested_station_list):
        """ For a list of station numbers, return a Dict of Station classes, keyed by Station_ID

        Log a warning if no data found for any requested station.

        Input:
            Unique list of station numbers (assumed unique)
        Output:
            Dict of Station() objects contained in station number array, keyed by Station_ID
        """
        query_tmp = "SELECT * FROM Station WHERE station_num IN ( "

        first = True
        for station in requested_station_list:
            if (first):
                query_tmp = query_tmp + " {} ".format(station)
                first = False
            else:
                query_tmp = query_tmp + ", {} ".format(station)
        query_tmp = query_tmp + ") ORDER BY station_num ASC;"

        self.cdict.execute(query_tmp)
        station_data = self.cdict.fetchall()

        # Check to see that we got the requested data, warn if we didn't
        # Note that we're assuming that the function has been called with unique items in requested_station_list
        requested_num   = len(requested_station_list)
        requested_found = len(station_data)
        if (requested_found < requested_num):
            found_station_list = []
            for station in station_data:
                if (station["station_num"] not in found_station_list):
                    found_station_list.append(station["station_num"])
            for station in requested_station_list:
                if (station not in found_station_list):
                    log.warning("Did not find data for station {}".format(station))
                    # TODO Figure out if there's something else to do here to warn the calling function of missing data

        Stations = {} # Initialize dict for station data
        for row in station_data:
            Sta = Station()

            Sta.station_num		= row["station_num"]
            Sta.initial			= row["initial"]
            Sta.latitude		= row["latitude"]
            Sta.longitude		= row["longitude"]
            Sta.elevation_m		= row["elevation_m"]
            Sta.name			= row["name"]
            Sta.MPC			    = row["MPC"]
            Sta.details			= row["details"]
            Sta.preferred_format = row["preferred_format"]
            Sta.source_url		= row["source_url"]
            Sta.notes			= row["notes"]
            Sta.user			= row["user"]

            # Add new dictionary entry for Station Num
            Stations.update( {Sta.station_num : Sta } )
        return Stations


    def getStationDictforIODs(self, IODs):
        """ Query the DB for all the stations contained in an IOD Array, and return a dictionary for
        station information to support analyses of the IODs

        Input: an array of IOD class variables

        Output: Dict of Station() objects contained in IOD array, indexed by Station_ID key
        """
        needed_stations = []

        # Create unique list of stations contained in IOD array
        for iod in IODs:
            if (iod.Station not in needed_stations):
                needed_stations.append(iod.Station)

        # TODO: Figure out if there's error checking here for less station data than we asked for
        Stations = self.getStationsQuery(needed_stations)
        return Stations

    #######################
    ### Observer-related queries
    #######################
    def updateObserverNonce(self, nonce, public_address):
        """ TODO: Kenan to document """

        if self._dbtype == "INFILE":
            try:
                results = (self.updateObserverNonce_query, [nonce, public_address])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.updateObserverNonce_query, [nonce, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverNonce_query.execute(self.updateObserverNonce_query, [nonce, public_address])
            self.conn.commit()
        return True

    def updateObserverJWT(self, jwt, password, public_address):
        """ TODO: Kenan to document """
        if self._dbtype == "INFILE":
            try:
                results = (self.updateObserverJWT_query, [jwt, password, public_address])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.updateObserverJWT_query, [jwt, password, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverJWT_query.execute(self.updateObserverJWT_query, [jwt, password, public_address])
            self.conn.commit()
        return True

    def updateObserverUsername(self, username, public_address):
        """ TODO: Kenan to document """
        if self._dbtype == "INFILE":
            try:
                results = (self.updateObserverUsername_query, [username, public_address])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.updateObserverUsername_query, [username, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverUsername_query.execute(self.updateObserverUsername_query, [username, public_address])
            self.conn.commit()

    def updateObserverEmail(self, email, public_address):
        """ TODO: Kenan to document """
        if self._dbtype == "INFILE":
            try:
                results = (self.updateObserverEmail_query, [email, public_address])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.updateObserverEmail_query, [email, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverEmail_query.execute(self.updateObserverEmail_query, [email, public_address])
            self.conn.commit()
        return True

    def updateObserverBio(self, bio, public_address):
        """ TODO: Kenan to document """
        if self._dbtype == "INFILE":
            try:
                results = (self.updateObserverBio_query, [bio, public_address])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.updateObserverBio_query, [bio, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverBio_query.execute(self.updateObserverBio_query, [bio, public_address])
            self.conn.commit()
        return True

    def updateObserverLocation(self, location, public_address):
        """ TODO: Kenan to document """
        if self._dbtype == "INFILE":
            try:
                results = (self.updateObserverLocation_query, [location, public_address])
            except KeyError:
                results = None
        elif self._dbtype == "sqlite":
            self.c.execute(self.updateObserverLocation_query, [location, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverLocation_query.execute(self.updateObserverLocation_query, [location, public_address])
            self.conn.commit()
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
        """ TODO: Kenan to document """
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
        """ TODO: Kenan to document """
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

    def getObserverFromJWT(self, jwt):
        """ TODO: Kenan to document """
        query_tmp = '''SELECT eth_addr FROM Observer WHERE jwt="{JWT}"'''.format(JWT=jwt)
        self.c.execute(query_tmp)
        return self.c.fetchone()[0]

    #######################
    ### IOD-related queries
    #######################
    def cdictQueryToObsObj(self, fetch):
        """ Transfer the cdict.fetchall() results of a Obs query to tle_util IOD() object array (all variables)

        Input: Fetch results from the cdict cursor

        Output: Array of IOD() objects
        """
        Observations = []

        for row in fetch:
            OBS = iod.IOD()

            # FIXME: Fix inconsistency between DB table and IOD Class variable names.  DB table is probably better
            OBS.AngleFormatCode = row["angle_format_code"]
            OBS.AZ = row["azimuth"]
            OBS.DEC = row["declination"]
            OBS.EL = row["elevation"]
            OBS.Epoch = row["epoch"]
            OBS.EpochCode = row["epoch_code"]
            OBS.FlashPeriod = row["flash_period"]
            OBS.import_timestamp = row["import_timestamp"]
            OBS.InternationalDesignation = row["international_designation"]
            OBS.iod_string = row["iod_string"]
            OBS.IODType = row["iod_type"]
            OBS.MagnitudeUncertainty = row["magnitude_uncertainty"]
            OBS.message_id = row["message_id"]
            OBS.ObjectNumber = row["object_number"]
            OBS.obs_id = row["obs_id"]
            OBS.obs_time = row["obs_time"]
            OBS.obs_time_string = row["obs_time_string"]
            OBS.obsFingerPrint = row["obsFingerPrint"]
            OBS.OpticalCode = row["optical_behavior_code"]
            OBS.PositionUncertainty = row["positional_uncertainty"]
            OBS.RA = row["ra"]
            OBS.Remarks = row["remarks"]
            OBS.Station = row["station_number"]
            OBS.StationStatusCode = row["station_status_code"]
            OBS.submitted = row["submitted"]
            OBS.TimeStandardCode = row["time_standard_code"]
            OBS.TimeUncertainty = row["time_uncertainty"]
            OBS.UserString = row["user_string"]
            OBS.ValidPosition = row["valid_position"]
            OBS.VisualMagnitude = row["visual_magnitude"]
            OBS.VisualMagnitude_high = row["visual_magnitude_high"]
            OBS.VisualMagnitude_low = row["visual_magnitude_low"]

            Observations.append(OBS)
        return Observations

    def selectIODListat(self, obs_id):
        """ Get a list of observation IDs starting at the specified obs_id

        Returns an array of IOD objects
        """
        query_tmp = """SELECT * FROM ParsedIOD
                WHERE valid_position=1
                AND obs_id >= {OBS_ID}
                ORDER BY obs_id ASC
                LIMIT 10;""".format(OBS_ID=obs_id)
        self.cdict.execute(query_tmp)
        rows = self.cdict.fetchall()
        return self.cdictQueryToObsObj(rows)

    def selectIODlist(self,obs_id_list):
        """ Given the list of specified object IDs, returns an array of corresponding IOD objects """

        query_tmp = """SELECT * FROM ParsedIOD WHERE
            valid_position=1
            AND obs_id IN ( """

        first = True
        for id in obs_id_list:
            if (first):
                query_tmp = query_tmp + " {} ".format(id)
                first = False
            else:
                query_tmp = query_tmp + ", {} ".format(id)
        query_tmp = query_tmp + ") ORDER BY obs_time ASC;"

        self.cdict.execute(query_tmp)
        rows = self.cdict.fetchall()
        return self.cdictQueryToObsObj(rows)


    def getObservationCount(self):
        """ TODO: Kenan to document """
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
        """ TODO: Kenan to document """
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
        """ TODO: Kenan to document """
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
        """ TODO: Kenan to document """
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
        """ TODO: Kenan to document """
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


    def selectObservationHistory_JSON(self, fetch_row_count=10, offset_row_count=0):
        """ Provide a full observation history of objects starting with most recent valid observations

            Inputs: (None)
            Output: JSON object with observation summary
        """
        query_tmp = """SELECT Json_Object(
            'time_submitted',date_format(ParsedIOD.obs_time, '%M %d, %Y'),
            'object_name',celestrak_SATCAT.name,
            'right_ascension', ParsedIOD.ra,
            'declination', ParsedIOD.declination,
            'conditions', station_status.short_description)
            FROM ParsedIOD
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.norad_num
            LEFT JOIN station_status ON ParsedIOD.station_status_code = station_status.code
            WHERE valid_position = 1
            ORDER BY obs_time DESC
            LIMIT {OFFSET},{FETCH};""".format(
                OFFSET=offset_row_count,
                FETCH=fetch_row_count)
        self.c.execute(query_tmp)
        return stringArrayToJSONArray(self.c.fetchall())

    def selectObjectHistoryByMonth_JSON(self, norad_number, year, month):
        """ For a particular object, provide a navigation structure of its full observatio history

            Inputs: NORAD number of interest, year, month
            Output: JSON object with observation summary

            Note (Chris) - not sure this is being used currently
        """
        query_tmp = """SELECT Json_Object(
            'observation_time', UNIX_TIMESTAMP(ParsedIOD.obs_time),
            'username', user_string,
            'user_address', 'FILLER',
            'user_location', station_number,
            'observation_quality', station_status_code,
            'observation_time_difference', '1.42',
            'observation_weight', '5')
            FROM ParsedIOD
            WHERE object_number={NORAD_NUMBER}
            AND Year(obs_time)={YEAR}
            AND Month(obs_time)={MONTH}
            ORDER BY obs_time DESC""".format(
                    NORAD_NUMBER=norad_number,
                    YEAR=year,
                    MONTH=month)
        self.c.execute(query_tmp)
        return stringArrayToJSONArray_JSON(self.c.fetchall())

    # Supports user profile https://consensys-cpl.atlassian.net/browse/MVP-311
    # /object/history https://consensys-cpl.atlassian.net/browse/MVP-334
    def selectObjectHistory_summary(self, norad_num):
        """ Given a NORAD number, provide a summary structure of its observations by day, month, year

            Inputs: norad_num
            Output: SQL query rows

            Note (Chris): not sure this is being used, currently
        """
        quality = 99 # !TODO
        query_tmp = """SELECT
            YEAR(obs_time) as observation_year,
            MONTH(obs_time) as observation_month,
            DAYOFMONTH(obs_time) as observation_day
            FROM ParsedIOD
            WHERE object_number = {NORAD_NUM}
            AND valid_position=1
            GROUP BY observation_year, observation_month, observation_day
            ORDER BY observation_year DESC, observation_month ASC, observation_day ASC;""".format(
                NORAD_NUM=norad_num)
        self.c.execute(query_tmp)
        try:
            return self.c.fetchall()
        except:
            return None

    def commit_IOD_db_writes(self):
        """ Commit pending INSERTS to database.  Requested by external function after batch processes, 
        ideally after 1000 record updates or so."""
        if (self._dbtype == "sqlserver"):
            while(len(self._IODentryList) > 0):
                try:
                    self.c_addParsedIOD.executemany(self.addParsedIOD_query,self._IODentryList)
                    self._IODentryList = []
                    self._IODPendingEntryFingerprintList = []
                except Exception as e:
                    log.error("MYSQL ERROR: {}".format(e))
                    # FIXME - (Work in progress) - try to get rid of duplicate entry in a executemany list
                    # This is sensitive to when a user includes a duplicate entry in the same email

                    ## This is the MySQL error when you try and insert a duplicate fingerprint:
                    # mysql.connector.errors.IntegrityError: 1062 (23000): Duplicate entry '584eca1489bbbb05de3aacbbffc59a83' for key 'ParsedIOD_obsFingerPrint_idx'

                    # if ("Duplicate Entry" in e):  # This line doesn't work because "argument of type 'IntegrityError' is not iterable"
                    #     mysql_error_tuple = e.split(' ')
                    #     # FIXME - This is fragile
                    #     duplicate_fingerprint = mysql_error_tuple[6].strip("'")
                    #     row = 0
                    #     # FIXME - Don't know if this will work for the whole tuple, or if I have to find the element
                    #     for entry in observerTuple:
                    #         if duplicate_fingerprint in entry:
                    #             observerTuple.remove(row)
                    #         row += 1

        elif (self._dbtype != "INFILE"):
            self.conn.commit()

    #######################
    ### TLE-related queries
    #######################
    def cdictQueryToTruSatelliteObj(self, fetch):
        """ Transfer the cdict.fetchall() results of a TLE query to tle_util TruSatellite() object array (all variables)

        Input: Fetch results from the cdict cursor

        Output: Array of TruSatellite() objects
        """
        TLEs = []

        for row in fetch:
            TLE = tle_util.TruSatellite()

            TLE.tle_id			 = row["tle_id"]
            TLE.line0 = TLE.name = row["line0"]
            TLE.line1			 = row["line1"]
            TLE.line2			 = row["line2"]

            TLE.sat_name			            = row["sat_name"]
            TLE.satellite_number	            = row["satellite_number"]
            TLE.classification		            = row["classification"]
            TLE.designation			            = row["designation"]
            TLE.epoch_datetime	                = row["epoch"]
            TLE.mean_motion_derivative		    = row["mean_motion_derivative"]
            TLE.mean_motion_sec_derivative	    = row["mean_motion_sec_derivative"]
            TLE.bstar			                = row["bstar"]
            TLE.ephemeris_type	                = row["ephemeris_type"]
            TLE.element_set_number	            = row["element_set_number"]
            TLE.inclination_degrees             = row["inclination"] # FIXME: This is an inconsistency in the database schema
            TLE.inclination_radians	            = row["inclination_radians"]
            TLE.raan_degrees		            = row["raan_degrees"]
            TLE.raan_radians		            = row["raan_radians"]
            TLE.eccentricity		            = row["eccentricity"]
            TLE.arg_perigee_degrees	            = row["arg_perigee_degrees"]
            TLE.arg_perigee_radians	            = row["arg_perigee_radians"]
            TLE.mean_anomaly_degrees            = row["mean_anomaly_degrees"]
            TLE.mean_anomaly_radians            = row["mean_anomaly_radians"]
            TLE.mean_motion_orbits_per_day      = row["mean_motion_orbits_per_day"]
            # TODO: add mean_motion_radians_per_minute from the TLE class to here

            TLE.mean_motion_radians_per_second  = row["mean_motion_radians_per_second"]
            TLE.orbit_number			        = row["orbit_number"]

            TLE.launch_piece_number	= row["launch_piece_number"]
            TLE.analyst_object		= row["analyst_object"]
            TLE.strict_import		= row["strict_import"]
            TLE.tle_fingerprint		= row["tle_fingerprint"]
            TLE._tle_file_fingerprint = row["file_fingerprint"]
            TLE.import_timestamp	= row["import_timestamp"]

            TLE.derived_values()

            TLEs.append(TLE)
        return TLEs


    def selectTLEFile(self, tle_file_fingerprint):
        """ Query to see if a TLE file is already in the database based on its fingerprint. """
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
        """ Query to see if a specific TLE is already in the database based on its fingerprint. """
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

    def selectTLEEpochBeforeDate(self, query_epoch_datetime, satellite_number):
        """ Query to return the first TLE with epoch *prior* to specified date for a specific satellite number

        Returns TruSatellite() object
        """
        query_tmp = """SELECT * FROM TLE
            WHERE epoch <= '{}'
            AND satellite_number={}
            ORDER BY epoch DESC
            LIMIT 1""".format(query_epoch_datetime, satellite_number)
        self.cdict.execute(query_tmp)
        row = [self.cdict.fetchone()]   # Put single result into an array
        return self.cdictQueryToTruSatelliteObj(row)[0]  # Unpack the array to the object, for just one result

    def selectTLEEpochNearestDate(self, query_epoch_datetime, satellite_number):
        """ Query to return the *nearest* TLE with epoch for a specific satellite for a specified date

        Could be before or after the provided date.
        Returns TruSatellite() object
        """
        query_tmp = """SELECT *,ABS(TIMEDIFF(epoch,'{}')) as diff FROM TLE
            WHERE satellite_number={}
            ORDER BY diff ASC
            LIMIT 1""".format(query_epoch_datetime, satellite_number)
        self.c.execute(query_tmp)
        row = [self.cdict.fetchone()]    # Put single result into an array
        return self.cdictQueryToTruSatelliteObj(row)[0]  # Unpack the array to the object, for just one result

    # FIXME - This is the latest of everything in the catalog - but some will be old from McCants stuff because they were dropped from classfd.tle
    def selectTLE_Astriagraph(self):
        """ Create a list of TLEs appropriate for Astriagraph to plot.

        Not currently used.
        """

        query_tmp = """SELECT line0, line1, line2, satellite_number
            FROM TLE
            GROUP BY satellite_number
            ORDER BY TLE.epoch DESC;"""
        self.c.execute(query_tmp)
        result = ""
        for (line0, line1, line2, _) in self.c.fetchall():
            result = result + "{}\n{}\n{}\n".format(line0,line1,line2)
        return result

    # https://consensys-cpl.atlassian.net/browse/MVP-285
    def selectTLE_all(self):
        """ Create a full list of TLEs for all unique objects in the database.
        """

        query_tmp = """SELECT line0, line1, line2, satellite_number
            FROM TLE
            GROUP BY satellite_number
            ORDER BY satellite_number ASC;"""
        self.c.execute(query_tmp)
        result = ""
        for (line0, line1, line2, _) in self.c.fetchall():
            result = result + "{}\n{}\n{}\n".format(line0,line1,line2)
        return result


    # https://consensys-cpl.atlassian.net/browse/MVP-286
    def selectTLE_priorities(self):
        """ Create list of priority TLEs
        """
        # TODO: Replace with real priority sort. https://consensys-cpl.atlassian.net/browse/MVP-389
        # In the meantime, return TLEs older than 30 days
        query_tmp = """SELECT line0, line1, line2, satellite_number
            FROM TLE
            WHERE DATEDIFF(NOW(),epoch) > 30
            GROUP BY satellite_number
            ORDER BY TLE.epoch DESC;"""
        self.c.execute(query_tmp)
        result = ""
        for (line0, line1, line2, _) in self.c.fetchall():
            result = result + "{}\n{}\n{}\n".format(line0,line1,line2)
        return result

    # https://consensys-cpl.atlassian.net/browse/MVP-287
    def selectTLE_high_confidence(self):
        """ Create list of high confidence TLEs
        """
        # TODO: Replace with real confidence sort. https://consensys-cpl.atlassian.net/browse/MVP-390
        # In the meantime, return TLEs younger than 30 days, newest first
        query_tmp = """SELECT line0, line1, line2, satellite_number
            FROM TLE
            WHERE DATEDIFF(NOW(),epoch) < 30
            GROUP BY satellite_number
            ORDER BY TLE.epoch ASC;"""
        self.c.execute(query_tmp)
        result = ""
        for (line0, line1, line2, _) in self.c.fetchall():
            result = result + "{}\n{}\n{}\n".format(line0,line1,line2)
        return result

    # https://consensys-cpl.atlassian.net/browse/MVP-385
    def selectTLE_single(self, norad_num):
        """ Provide the most recent TLE for a given NORAD number """

        query_tmp = """SELECT line0, line1, line2
            FROM TLE
            WHERE satellite_number={NORAD_NUM}
            ORDER BY EPOCH DESC
            LIMIT 1;""".format(NORAD_NUM=norad_num)
        self.c.execute(query_tmp)
        try:
            (line0, line1, line2) = self.c.fetchone()
            return "{}r\n{}\n{}\n".format(line0,line1,line2)
        except Exception as e:
            print(e)
            return None

    def commit_TLE_db_writes(self):
        """Process a stored query batch for all the TLEs in a file at once.

        Note that for large TLE files (50,000 entries, we might want to batch this at 1,000 per per something)
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


    def selectUserStations_JSON(self, eth_addr):
        """ Create a list of observation Stations for a given ETH address
        TODO: Return number of observations for each station along with list
        PRIVACY: Should only be returned to the logged-in wallet owner.
        """

        query_tmp = """SELECT Json_Object(
            'station_number', Station.station_num,
            'station_observation_count', '1', /* FIXME:  Add a station observation count to this list */
            'station_initials', Station.initial,
            'station_latitude', Station.latitude,
            'station_longitude', Station.longitude,
            'station_elevation_m', Station.elevation_m,
            'station_name', Station.name,
            'station_details', Station.details)
            FROM Station
            JOIN Observer ON Observer.id = Station.user
            WHERE Observer.eth_addr = '{ETH_ADDR}'
            ORDER BY Station.station_num ASC;""".format(
                ETH_ADDR=eth_addr)
        try:
            self.c.execute(query_tmp)
            return stringArrayToJSONArray(self.c.fetchall())
        except:
            return None


    def selectProfileInfo_JSON(self, eth_addr):
        """ Return profile info for a given user ETH address, including:
        - Number objects tracked by user
        - Total observation count by user
        - Summary user stats
        """

        # TODO: Replace fake data with real data https://consensys-cpl.atlassian.net/browse/MVP-388
        avg_obs_quality = 99 # !TODO # FIXME: Replace with real data:

        # Get unique list of observed objects for this user
        # TODO: Seems like there's a way to get a count in the query instead of counting the result in python
        query_tmp_num_obj_tracked = """SELECT ParsedIOD.object_number
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num
            JOIN Observer ON Observer.id = Station.user
            WHERE Observer.eth_addr = '{ETH_ADDR}'
            GROUP BY ParsedIOD.object_number;""".format(ETH_ADDR=eth_addr)
        self.c.execute(query_tmp_num_obj_tracked)
        try:
            obj_tracked = self.c.fetchall()
            num_obj_tracked = len(obj_tracked)
        except:
            num_obj_tracked = 0

        # Get count of observations for this user
        query_tmp_obs_count = """SELECT COUNT(ParsedIOD.object_number) as obs_count
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num
            JOIN Observer ON Observer.id = Station.user
            WHERE Observer.eth_addr = '{ETH_ADDR}';""".format(ETH_ADDR=eth_addr)
        self.c.execute(query_tmp_obs_count)
        try:
            [(obs_count)] = self.c.fetchone()
        except:
            obs_count = 0

        query_tmp = """SELECT Json_Object(
            'user_name', Observer.name,
            'email', Observer.reference,
            'user_address', Observer.eth_addr,
            'user_location', Observer.location,
            'number_objects_tracked', '{NUM_OBJ_TRACKED}',
            'observation_count', '{OBS_COUNT}',
            'average_observation_quality', '{AVG_OBS_QUALITY}',
            'user_bio', Observer.bio,
            'user_image', Observer.url_image)
            FROM Observer
            WHERE Observer.eth_addr = '{ETH_ADDR}'
            LIMIT 1;""".format(
                NUM_OBJ_TRACKED=num_obj_tracked,
                OBS_COUNT=obs_count,
                AVG_OBS_QUALITY=avg_obs_quality,
                ETH_ADDR=eth_addr)
        self.c.execute(query_tmp)
        return QueryRowToJSON(self.c.fetchone())

    # Supports user profile https://consensys-cpl.atlassian.net/browse/MVP-311
    # Notes about endpoint https://consensys-cpl.atlassian.net/browse/MVP-328
    def selectUserObservationHistory_JSON(self, eth_addr, fetch_row_count=10, offset_row_count=0):
        """ Return the observation history for a particular ETH addresses, starting with most 
        recent observations.
        """
        # TODO: Replace fake data with real data https://consensys-cpl.atlassian.net/browse/MVP-388
        quality = 99 # !TODO
        time_difference = 3 # !TODO
        obs_weight = 0.123456 # !TODO

        query_tmp = """SELECT Json_Object(
            'observation_time',date_format(ParsedIOD.obs_time, '%M %d, %Y'),
            'object_name',celestrak_SATCAT.name,
            'station_number', Obs.station_num,
            'object_norad_number', ParsedIOD.object_number,
            'observation_quality', '{QUALITY}',
            'observation_time_difference', '{TIME_DIFF}',
            'observation_weight', '{OBS_WEIGHT}',
            'observation_iod', ParsedIOD.iod_string
            )
            FROM ParsedIOD
            JOIN (SELECT
                    Station.station_num as station_num,
                    Station.user as station_user,
                    Observer.id as obs_id,
                    Observer.eth_addr as eth_addr,
                    Observer.name as user_name
                    FROM Station,Observer
                    WHERE Station.user = Observer.id
                    AND Observer.eth_addr = '{ETH_ADDR}'
                    LIMIT 1) Obs ON ParsedIOD.station_number = Obs.station_num
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.norad_num
            LEFT JOIN station_status ON ParsedIOD.station_status_code = station_status.code
            WHERE valid_position = 1
            ORDER BY obs_time DESC
            LIMIT {OFFSET},{FETCH};""".format(
                QUALITY=quality,
                TIME_DIFF=time_difference,
                OBS_WEIGHT=obs_weight,
                ETH_ADDR=eth_addr,
                OFFSET=offset_row_count,
                FETCH=fetch_row_count)
        self.c.execute(query_tmp)
        return stringArrayToJSONArray_JSON(self.c.fetchall())

    def selectUserObjectsObserved_JSON(self, eth_addr, fetch_row_count=10, offset_row_count=0):
        """ For a given ETH address, return list of objects they have observed along with context detail.
        """
        # FIXME: Fancier query logic needed to get the last eth_addr to track in the summary of a selected-users observations.
        query_tmp = """SELECT Json_Object(
            'object_origin', ucs_SATDB.country_owner,
            'object_type', ucs_SATDB.purpose,
            'object_primary_purpose', ucs_SATDB.purpose_detailed,
            'object_secondary_purpose', 'Michael to define type, primary and secondary purpose',
            'observation_quality', ParsedIOD.station_status_code,
            'object_name',celestrak_SATCAT.name,
            'object_norad_number', ParsedIOD.object_number,
            'time_last_tracked',date_format(ParsedIOD.obs_time, '%M %d, %Y'),
            'username_last_tracked', Obs.user_name,
            'address_last_tracked', Obs.eth_addr)
            FROM ParsedIOD
            JOIN (SELECT
                    Station.station_num as station_num,
                    Station.user as station_user,
                    Observer.id as obs_id,
                    Observer.eth_addr as eth_addr,
                    Observer.name as user_name
                    FROM Station,Observer
                    WHERE Station.user = Observer.id
                    AND Observer.eth_addr = '{ETH_ADDR}'
                    LIMIT 1) Obs ON ParsedIOD.station_number = Obs.station_num
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number=ucs_SATDB.norad_number
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            WHERE valid_position = 1
            ORDER BY obs_time DESC
            LIMIT {OFFSET},{FETCH};""".format(
                ETH_ADDR=eth_addr,
                OFFSET=offset_row_count,
                FETCH=fetch_row_count)
        self.c.execute(query_tmp)
        object_observed = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(object_observed)
        return object_observed

    # https://consensys-cpl.atlassian.net/browse/MVP-311
    # /profile endpoint for a logged-in user
    def selectUserProfile(self, eth_addr):
        """ Return nested Object of data related to user profile
        Note (from Chris) not sure if this is used by backend...
        """
        user_profile_info = self.selectProfileInfo_JSON(eth_addr)
        user_stations = self.selectUserStations_JSON(eth_addr)
        user_objects_observered = self.selectUserObjectsObserved_JSON(eth_addr)
        user_observation_history = self.selectUserObservationHistory_JSON(eth_addr)

        json_dict = {}
        json_dict["user_profile_info"] = user_profile_info
        json_dict["user_stations"] = user_stations
        json_dict["user_objects_observered"] = user_objects_observered
        json_dict["user_observation_history"] = user_observation_history

        return json.dumps(
            json_dict,
            sort_keys=False,
            indent=4)


    def selectObjectsObserved_JSON(self, fetch_row_count=10, offset_row_count=0):
        """ Return list of (global) observed objects, ordered from most recent
        """
        query_tmp = """SELECT Json_Object(
            'object_origin', ucs_SATDB.country_owner,
            'primary_purpose', ucs_SATDB.purpose,
            'object_type', ucs_SATDB.purpose_detailed,
            'secondary_purpose', 'Secondary purpose does not exist, the variable is also misspelled.',
            'observation_quality', ParsedIOD.station_status_code,
            'time_last_tracked',date_format(ParsedIOD.obs_time, '%M %d, %Y'),
            'username_last_tracked',ParsedIOD.user_string)
            FROM ParsedIOD
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number=ucs_SATDB.norad_number
            WHERE valid_position = 1
            ORDER BY obs_time DESC
            LIMIT {OFFSET},{FETCH};""".format(
                OFFSET=offset_row_count,
                FETCH=fetch_row_count)
        self.c.execute(query_tmp)
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)


    # /catalog/priorities
    # https://consensys-cpl.atlassian.net/browse/MVP-323
    # FIXME: Optimization - this query is slow, because of the Join to Observer not using the index
    def selectCatalog_Priorities_JSON(self, fetch_row_count=100, offset_row_count=0):
        """ Return list of catalog objects in priority observation order
        """

        quality = 99 # !TODO
        quality = 99 # !TODO # make it deterministic
        # TODO: No priorities in database yet, just sort by reverse obs order for something interesting/different to look at
        # https://consensys-cpl.atlassian.net/browse/MVP-389
        query_tmp = """select Json_Object(
            'object_norad_number', ParsedIOD.object_number,
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner,
            'object_type', ucs_SATDB.purpose,
            'object_primary_purpose', ucs_SATDB.purpose_detailed,
            'object_secondary_purpose', ucs_SATDB.comments,
            'object_observation_quality', '{QUALITY}',
            'time_last_tracked', date_format(ParsedIOD.obs_time, '%M %d, %Y'),
            'address_last_tracked', Obs.eth_addr,
            'username_last_tracked',Obs.user_name)
            FROM ParsedIOD
            JOIN (SELECT
                    Station.station_num as station_num,
                    Station.user as station_user,
                    Observer.id as obs_id,
                    Observer.eth_addr as eth_addr,
                    Observer.name as user_name
                    FROM Station,Observer
                    WHERE Station.user = Observer.id
                    LIMIT 1) Obs ON ParsedIOD.station_number = Obs.station_num
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number = ucs_SATDB.norad_number
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            WHERE ParsedIOD.valid_position = 1
            ORDER BY obs_time DESC
            LIMIT {OFFSET},{FETCH};""".format(
                OFFSET=offset_row_count,
                FETCH=fetch_row_count,
                QUALITY=quality)

        self.c.execute(query_tmp)
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)

    # /catalog/undisclosed
    # https://consensys-cpl.atlassian.net/browse/MVP-324
    def selectCatalog_Undisclosed_JSON(self, fetch_row_count=100, offset_row_count=0):
        """ Create list of Classified TLEs - those that have 'NEA' (no elements available) status via Celestrak
        """
        quality = 99 # !TODO
        query_tmp = """select Json_Object(
            'object_norad_number', ParsedIOD.object_number,
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner,
            'object_type', ucs_SATDB.purpose,
            'object_primary_purpose', ucs_SATDB.purpose_detailed,
            'object_secondary_purpose', ucs_SATDB.comments,
            'object_observation_quality', '{QUALITY}',
            'time_last_tracked', date_format(ParsedIOD.obs_time, '%M %d, %Y'),
            'address_last_tracked', Obs.eth_addr,
            'username_last_tracked',Obs.user_name)
            FROM ParsedIOD
            JOIN (SELECT
                    Station.station_num as station_num,
                    Station.user as station_user,
                    Observer.id as obs_id,
                    Observer.eth_addr as eth_addr,
                    Observer.name as user_name
                    FROM Station,Observer
                    WHERE Station.user = Observer.id
                    LIMIT 1) Obs ON ParsedIOD.station_number = Obs.station_num
            JOIN ucs_SATDB ON ParsedIOD.object_number = ucs_SATDB.norad_number
            JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            WHERE ParsedIOD.valid_position = 1
            AND celestrak_SATCAT.orbit_status_code = 'NEA'
            GROUP BY ParsedIOD.object_number
            ORDER BY obs_time DESC
            LIMIT {OFFSET},{FETCH};""".format(
                OFFSET=offset_row_count,
                FETCH=fetch_row_count,
                QUALITY=quality)

        self.c.execute(query_tmp)
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)

    # /catalog/debris
    # https://consensys-cpl.atlassian.net/browse/MVP-325
    def selectCatalog_Debris_JSON(self, fetch_row_count=100, offset_row_count=0):
        """ Create list of Debris objects.  Most catalog items have DEB in the tital.  
        There are probably some exceptions """
        quality = 99 # !TODO
        query_tmp = """select Json_Object(
            'object_norad_number', ParsedIOD.object_number,
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner,
            'object_primary_purpose', ucs_SATDB.purpose_detailed,
            'object_secondary_purpose', ucs_SATDB.comments,
            'object_observation_quality', '{QUALITY}',
            'time_last_tracked', date_format(ParsedIOD.obs_time, '%M %d, %Y'),
            'address_last_tracked', Obs.eth_addr,
            'username_last_tracked',Obs.user_name)
            FROM ParsedIOD
            JOIN (SELECT
                    Station.station_num as station_num,
                    Station.user as station_user,
                    Observer.id as obs_id,
                    Observer.eth_addr as eth_addr,
                    Observer.name as user_name
                    FROM Station,Observer
                    WHERE Station.user = Observer.id
                    LIMIT 1) Obs ON ParsedIOD.station_number = Obs.station_num
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number = ucs_SATDB.norad_number
            WHERE ParsedIOD.valid_position = 1
            AND celestrak_SATCAT.name LIKE '%DEB%'
            GROUP BY ParsedIOD.object_number
            ORDER BY obs_time DESC
            LIMIT {OFFSET},{FETCH};""".format(
                OFFSET=offset_row_count,
                FETCH=fetch_row_count,
                QUALITY=quality)
        self.c.execute(query_tmp)
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)

    # /catalog/latest
    # https://consensys-cpl.atlassian.net/browse/MVP-326
    def selectCatalog_Latest_JSON(self, fetch_row_count=100, offset_row_count=0):
        """ Provide a list of the most recently launched objects (last 12 months) """
        quality = 99 # !TODO
        now = datetime.utcnow()
        date_delta = now - timedelta(days=365)
        launch_date_string  = date_delta.strftime("%Y-%m-%d")

        query_tmp = """select Json_Object(
            'object_norad_number', ParsedIOD.object_number,
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner,
            'object_type', ucs_SATDB.purpose,
            'object_primary_purpose', ucs_SATDB.purpose_detailed,
            'object_secondary_purpose', ucs_SATDB.comments,
            'object_observation_quality', '{QUALITY}',
            'time_last_tracked', date_format(ParsedIOD.obs_time, '%M %d, %Y'),
            'address_last_tracked', Obs.eth_addr,
            'username_last_tracked',Obs.user_name)
            FROM ParsedIOD
            JOIN (SELECT
                    Station.station_num as station_num,
                    Station.user as station_user,
                    Observer.id as obs_id,
                    Observer.eth_addr as eth_addr,
                    Observer.name as user_name
                    FROM Station,Observer
                    WHERE Station.user = Observer.id
                    LIMIT 1) Obs ON ParsedIOD.station_number = Obs.station_num
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number = ucs_SATDB.norad_number
            WHERE ParsedIOD.valid_position = 1
            AND celestrak_SATCAT.launch_date > {LAUNCH_DATE}
            ORDER BY obs_time DESC
            LIMIT {OFFSET},{FETCH};""".format(
                LAUNCH_DATE=launch_date_string,
                OFFSET=offset_row_count,
                FETCH=fetch_row_count,
                QUALITY=quality)

        self.c.execute(query_tmp)
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)

    # /catalog/all
    # https://consensys-cpl.atlassian.net/browse/MVP-327
    def selectCatalog_All_JSON(self, fetch_row_count=100, offset_row_count=0):
        """ Return a full list of all objects in the DB which have been observed, 
        ordered by the time they were last tracked.  Should contain only one entry per umique object.
        """
        quality = 99 # !TODO
        query_tmp = """SELECT Json_Object(
            'object_norad_number', IODs.object_number,
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner,
            'object_type', ucs_SATDB.purpose,
            'object_primary_purpose', ucs_SATDB.purpose_detailed,
            'object_secondary_purpose', ucs_SATDB.comments,
            'object_observation_quality', '%(QUALITY)s',
            'time_last_tracked', date_format(IODs.obs_time, '%M %d, %Y'),
            'address_last_tracked', Obs.eth_addr,
            'username_last_tracked',Obs.user_name)
            FROM
            (SELECT object_number, obs_time, station_number
            		FROM ParsedIOD
            		WHERE ParsedIOD.valid_position = 1
            		ORDER BY obs_time DESC
                    LIMIT %(OFFSET)s,%(FETCH)s) AS IODs
            JOIN (SELECT
                    Station.station_num as station_num,
                    Station.user as station_user,
                    Observer.id as obs_id,
                    Observer.eth_addr as eth_addr,
                    Observer.name as user_name
                    FROM Station,Observer
                    WHERE Station.user = Observer.id) Obs ON IODs.station_number = Obs.station_num
            LEFT JOIN ucs_SATDB ON IODs.object_number = ucs_SATDB.norad_number
            LEFT JOIN celestrak_SATCAT ON IODs.object_number = celestrak_SATCAT.sat_cat_id;"""
        
        # !TODO: here and everywhere, use bind variables rather than string formatting, for security and performance:
        # mysql connector uses the pyformat paramstyle (https://www.python.org/dev/peps/pep-0249/#paramstyle), so this looks something like:
        # self.c.execute("SELECT ... WHERE my_column = %(name)s", {"name": value}) 
        self.c.execute(query_tmp,
          { 'OFFSET': offset_row_count,
            'FETCH':fetch_row_count,
            'QUALITY': quality })
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)

    # /object/info/
    # https://consensys-cpl.atlassian.net/browse/MVP-379
    def selectObjectInfo_JSON(self, norad_num):
        """ Provide on Object containing valid-URLs for external sources of additional information 
        for a given NORAD number.  Currently only returns a single option (Heavens Above), and it is a
        TODO to add other options.
        """
        info_url = "https://www.heavens-above.com/SatInfo.aspx?satid={}".format(norad_num)
        quality = 99 # !TODO

        # Get user-related info first
        query_tmp_count = """SELECT COUNT(Observer.id), Observer.eth_addr, Observer.name,date_format(ParsedIOD.obs_time, '%M %d, %Y')
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
        except Exception as e:
            print(e)
            return None

        # Get object info and patch in user-info
        query_tmp = """select Json_Object(
            'object_name', celestrak_SATCAT.name,
            'object_origin', ucs_SATDB.country_owner,
            'object_type', ucs_SATDB.purpose,
            'object_purpose', ucs_SATDB.purpose_detailed,
            'object_secondary_purpose', ucs_SATDB.comments,
            'year_launched', YEAR(celestrak_SATCAT.launch_date),
            'time_last_tracked', date_format(ParsedIOD.obs_time, '%M %d, %Y'),
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
            observations = QueryRowToJSON_JSON(self.c.fetchone())
            convert_country_names_single(observations)
            return json.dumps(observations)
        except Exception as e:
            print(e)
            return None

    # /objectUserSightings
    # https://consensys-cpl.atlassian.net/browse/MVP-381
    def selectObjectUserSightings_JSON(self, norad_num, eth_addr, fetch_row_count=100, offset_row_count=0):
        """ For a given object and user ETH address, return a detailed list of their observation 
        history for that object, with most recent observations first.
        """
        # TODO: Replace fake data with real data https://consensys-cpl.atlassian.net/browse/MVP-388
        quality = 99 # !TODO
        time_difference = 3 # !TODO
        obs_weight = 0.123456 # !TODO

        query_tmp = """SELECT Json_Object(
            'observation_time', date_format(obs_time, '%M %d, %Y'),
            'object_origin', celestrak_SATCAT.source,
            'user_location', Obs.location,
            'username', Obs.user_name,
            'user_address', Obs.eth_addr,
            'observation_quality', '{QUALITY}',
            'observation_time_difference', '{TIME_DIFF}',
            'observation_weight', '{OBS_WEIGHT}')
            FROM ParsedIOD
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            JOIN (SELECT
                    Station.station_num as station_num,
                    Station.user as station_user,
                    Observer.id as obs_id,
                    Observer.eth_addr as eth_addr,
                    Observer.name as user_name,
                    Observer.location as location
                    FROM Station,Observer
                    WHERE Station.user = Observer.id
                    AND Observer.eth_addr = '{ETH_ADDR}'
                    LIMIT 1) Obs ON ParsedIOD.station_number = Obs.station_num
            WHERE ParsedIOD.object_number = {NORAD_NUM}
            ORDER BY obs_time DESC
            LIMIT {OFFSET},{FETCH};""".format(
                QUALITY=quality,
                TIME_DIFF=time_difference,
                OBS_WEIGHT=obs_weight,
                NORAD_NUM=norad_num,
                ETH_ADDR=eth_addr,
                OFFSET=offset_row_count,
                FETCH=fetch_row_count
                )
        self.c.execute(query_tmp)
        try:
            observations = stringArrayToJSONArray_JSON(self.c.fetchall())
            convert_country_names(observations)
            return json.dumps(observations)
        except:
            return None

    # /object/influence
    # https://consensys-cpl.atlassian.net/browse/MVP-380
    def selectObjectInfluence_JSON(self, norad_num, fetch_row_count=100, offset_row_count=0):
        """ For a given NORAD object, return detailed observation information (by all users)
        for the object, with the most recent observations first.

        In the roadmap, this should probably narrow to only the selected (most recent?) TLE
        """
        # TODO: Replace fake data with real data https://consensys-cpl.atlassian.net/browse/MVP-388
        quality = 99 # !TODO
        time_difference = 3 # !TODO
        obs_weight = 0.123456 # !TODO

        query_tmp = """SELECT Json_Object(
            'observation_time', date_format(obs_time, '%M %d, %Y'),
            'object_origin', celestrak_SATCAT.source,
            'user_location', Obs.location,
            'username', Obs.user_name,
            'observation_quality', '{QUALITY}',
            'observation_time_difference', '{TIME_DIFF}',
            'observation_weight', '{OBS_WEIGHT}',
            'user_address', Obs.eth_addr)
            FROM ParsedIOD
            LEFT JOIN celestrak_SATCAT ON ParsedIOD.object_number = celestrak_SATCAT.sat_cat_id
            JOIN (SELECT
                    Station.station_num as station_num,
                    Station.user as station_user,
                    Observer.id as obs_id,
                    Observer.eth_addr as eth_addr,
                    Observer.name as user_name,
                    Observer.location as location
                    FROM Station,Observer
                    WHERE Station.user = Observer.id
                    LIMIT 1) Obs ON ParsedIOD.station_number = Obs.station_num
            WHERE ParsedIOD.object_number = {NORAD_NUM}
            ORDER BY obs_time DESC
            LIMIT {OFFSET},{FETCH};""".format(
                QUALITY=quality,
                TIME_DIFF=time_difference,
                OBS_WEIGHT=obs_weight,
                NORAD_NUM=norad_num,
                OFFSET=offset_row_count,
                FETCH=fetch_row_count
                )
        self.c.execute(query_tmp)
        try:
            observations = stringArrayToJSONArray_JSON(self.c.fetchall())
            convert_country_names(observations)
            return json.dumps(observations)
        except:
            return None

    # https://consensys-cpl.atlassian.net/browse/MVP-393
    # /findObject endpoint
    def selectFindObject(self, partial_string):
        """ Facilitate a search of objects contained in the database, by NORAD number or name.
        Provide a partial result of matches to allow the user to choose their specific object of interest.
        """
        if (type(partial_string) == int):
            query_tmp = """SELECT DISTINCT Json_Object(
                'norad_number', norad_num,
                'name', name)
                FROM celestrak_SATCAT
                WHERE norad_num LIKE '{PARTIAL}%'
                ORDER by norad_num ASC;
                """.format(
                    PARTIAL=partial_string)
        else:
            query_tmp = """SELECT DISTINCT Json_Object(
                'norad_number', norad_num,
                'name', name)
                FROM celestrak_SATCAT
                WHERE name LIKE '{PARTIAL}%'
                ORDER by name ASC;
                """.format(
                    PARTIAL=partial_string)
        print(query_tmp)
        self.c.execute(query_tmp)
        try:
            return stringArrayToJSONArray(self.c.fetchall())
        except:
            return None



    def clean(self):
        self.conn.close()
