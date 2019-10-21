import sqlite3
import mysql.connector as mariadb
from datetime import datetime, timedelta
from hashlib import md5
from csv import writer
import pycountry
import json
import random
import re


# The following 9 lines are necessary until the trusat-orbit repo is public
import inspect
import os
import sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
tle_path = os.path.join(parentdir, "trusat-orbit")
sys.path.insert(1,tle_path)
import tle_util
import iod

import logging
log = logging.getLogger(__name__)

"""
database.py: Does database interactions for the Open Satellite Catalog
"""

def QueryRowToJSON_JSON(var):
    """ Take the results of an SQL fetchone and returns a dictionary version of the string """
    try:
        return json.loads(var[0])
    except:
        return {}

def stringArrayToJSONArray(string_array):
    """ Convert a string array into a string version of a json array. """
    json_array = []
    for item in string_array:
        json_array.append(json.loads(item[0]))
    return json.dumps(
        json_array,
        sort_keys=False,
        indent=4)

def stringArrayToJSONArray_JSON(string_array):
    """ Convert a string array into a json array. """
    json_array = []
    for item in string_array:
        json_array.append(json.loads(item[0]))
    return json_array

def QueryTupleListToList(var):
    """ Take the result of a SQL fetchall single variable query tuple list and make a regular python list """
    list = []
    for i in var:
        list.append(i[0])
    return list

def datetime_from_sqldatetime(sql_date_string):
    """ The 4 digit sub-seconds are not the standard 3 or 6, which creates problems with datetime.fromisoformat """
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    return datetime.strptime(sql_date_string, date_format)

def convert_country_names(object_observed):
    """ Convert country names into two letter abbreviation for a list """
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
    """ Convert country names into two letter abbreviation for a single object """
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

def generateUsername():
    EXCLUDE = [
        'General', 'Our Dwarves', 'Our Moons', 'Exoplanets',
        'Stars', 'wiki', 'Crux', 'Greek letters'
    ]
    regex = re.compile('[^a-zA-Z]') # to remove non-letter characters
    # create list of all keywords from text file
    f = open('./database_tools/keywords.txt', 'r').read()
    _keywords = f.split('\n')
    keywords = []

    for k in _keywords:
        sample = regex.sub('', k)
        if sample in EXCLUDE or k in EXCLUDE:
            continue
        if sample != '':
            keywords.append(sample)

    # generate unique username
    total_keywords = len(keywords) - 1
    _username = []
    while True:
        x = random.randint(0,total_keywords)
        if keywords[x] not in _username:
            _username.append(keywords[x])
        if len(_username) == 2:
            break

    username = ''.join(_username)
    return username


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
        dbusername - username for sqlserver
        dbpassword - password for sqlserver
    """
    def __init__(self, dbname=None,dbtype="sqlserver",dbhostname=None,dbusername=None,dbpassword=None):

        dbname = dbname or os.getenv('TRUSAT_DATABASE_NAME', None)
        dbhostname = dbhostname or os.getenv('TRUSAT_DATABASE_HOST', None)
        dbusername = dbusername or os.getenv('TRUSAT_DATABASE_USER', None)
        dbpassword = dbpassword or os.getenv('TRUSAT_DATABASE_PASSWORD', "")

        dbname or print("No database name specified")
        dbhostname or print("No database host specified")
        dbusername or print("No database user specified")

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
            self.c_addObserverEmail_query = self.conn.cursor(prepared=True)
            self.c_selectObserver_query = self.conn.cursor(prepared=True)
            self.c_updateObserverNonceBytes_query = self.conn.cursor(prepared=True)
            self.c_updateObserverJWT_query = self.conn.cursor(prepared=True)
            self.c_updateObserverUsername_query = self.conn.cursor(prepared=True)
            self.c_updateObserverEmail_query = self.conn.cursor(prepared=True)
            self.c_updateObserverBio_query = self.conn.cursor(prepared=True)
            self.c_updateObserverLocation_query = self.conn.cursor(prepared=True)
            self.c_updateObserverPrivate_query = self.conn.cursor(prepared=True)
            self.c_updateObserverPassword_query = self.conn.cursor(prepared=True)
            self.c_updateObserverAddress_query = self.conn.cursor(prepared=True)
            self.c_getObserverNonceBytes_query = self.conn.cursor(prepared=True)
            self.c_getObserverJWT_query = self.conn.cursor(prepared=True)
            self.c_getObserverCountByID_query = self.conn.cursor(prepared=True)
            self.c_selectTLEFile_query = self.conn.cursor(prepared=True)
            self.c_selectTLEFingerprint_query = self.conn.cursor(prepared=True)
            self.c_selectIODFingerprint_query = self.conn.cursor(prepared=True)
            self.c_addTLE_query = self.conn.cursor(prepared=True)
            self.c_addTLEFile_query = self.conn.cursor(prepared=True)
            self.c_addTLEProcess_query = self.conn.cursor(prepared=True)
            self.c_addSATCAT_query = self.conn.cursor(prepared=True)
            self.c_addUCSDB_query = self.conn.cursor(prepared=True)
            self.c_selectObserverID_query = self.conn.cursor(prepared=True)
            self.c_selectObserverAddressFromEmail_query = self.conn.cursor(prepared=True)
            self.c_selectEmailFromObserverAddress_query = self.conn.cursor(prepared=True)
            self.c_selectObserverPasswordFromAddress_query = self.conn.cursor(prepared=True)
            self.c_selectObserverAddressFromPassword_query = self.conn.cursor(prepared=True)
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
        self.addObserverEmail_query = '''INSERT INTO Observer_email(user_id, email) VALUES(?,?)'''
        self.selectObserver_query = '''SELECT id FROM Observer WHERE verified LIKE ? LIMIT 1'''
        self.updateObserverNonceBytes_query = '''UPDATE Observer SET nonce_bytes=? WHERE eth_addr=?'''
        self.updateObserverJWT_query = '''UPDATE Observer SET jwt=?, jwt_secret=? WHERE eth_addr=?'''
        self.updateObserverUsername_query = '''UPDATE Observer SET name=? WHERE eth_addr=?'''
        self.updateObserverEmail_query = '''UPDATE Observer_email INNER JOIN Observer ON Observer_email.user_id=Observer.id SET Observer_email.email=? WHERE Observer.eth_addr=?'''
        self.updateObserverLocation_query = '''UPDATE Observer SET location=? WHERE eth_addr=?'''
        self.updateObserverBio_query = '''UPDATE Observer SET bio=? WHERE eth_addr=?'''
        self.updateObserverPassword_query = '''UPDATE Observer SET password=? WHERE eth_addr=?'''
        self.updateObserverAddress_query = '''UPDATE Observer SET eth_addr=? WHERE eth_addr=?'''
        self.getObserverNonceBytes_query = '''SELECT nonce_bytes FROM Observer WHERE eth_addr=?'''
        self.getObserverJWT_query = '''SELECT jwt FROM Observer WHERE eth_addr=?'''
        self.getObserverCountByID_query = '''SELECT id, COUNT(*) from Observer WHERE eth_addr=?'''
        self.selectObserverAddressFromEmail_query = '''SELECT Observer.eth_addr FROM Observer INNER JOIN Observer_email ON Observer.id=Observer_email.user_id WHERE Observer_email.email=? LIMIT 1'''
        self.selectEmailFromObserverAddress_query = '''SELECT Observer_email.email FROM Observer_email INNER JOIN Observer ON Observer_email.user_id=Observer.id WHERE Observer.eth_addr=? LIMIT 1'''
        self.selectObserverPasswordFromAddress_query = '''SELECT password FROM Observer WHERE eth_addr=? LIMIT 1'''
        self.selectObserverAddressFromPassword_query = '''SELECT eth_addr FROM Observer WHERE password=? LIMIT 1'''
        self.selectTLEFile_query = '''SELECT file_fingerprint FROM TLEFILE WHERE file_fingerprint LIKE ? LIMIT 1'''
        self.selectTLEFingerprint_query = '''SELECT tle_fingerprint FROM TLE WHERE tle_fingerprint LIKE ? LIMIT 1'''
        self.selectIODFingerprint_query = '''SELECT obsFingerPrint FROM ParsedIOD WHERE obsFingerPrint LIKE ? LIMIT 1'''
        # !TODO: there may be more than one IOD for a given {object, observation time}. Limit to 1, perhaps arbitrarily if we have no way of discriminating.
        self.selectLatestTLEPerObject = """
            select TLE.line0, TLE.line1, TLE.line2,  TLE.satellite_number, TLE.epoch from
              (SELECT max(epoch) as epoch, satellite_number
              FROM TLE
              GROUP BY satellite_number) as latest_tles
            left join TLE on (TLE.satellite_number = latest_tles.satellite_number and TLE.epoch = latest_tles.epoch)"""

        self.selectCatalogQueryPrefix = """
            WITH catalog as (
              WITH latest_obs_times as (SELECT object_number, max(obs_time) max_obs_time
                            FROM ParsedIOD
                            WHERE ParsedIOD.valid_position = 1
                            and object_number is not null
                            group by object_number)
                -- There can be multiple obs_ids per {object_number, obs_time}, so we GROUP BY object_number again to ensure only one match
                ,latest_obs_ids as (SELECT P.obs_id, P.object_number, P.obs_time, P.station_number obs_station_number
                            FROM latest_obs_times L
                            LEFT JOIN ParsedIOD P on (L.object_number = P.object_number and L.max_obs_time = P.obs_time)
                            group by object_number)
                -- There can theoretically be multiple users per station, so we GROUP BY object_number again to ensure only one match
                ,latest_obs_with_users as (SELECT L.*, S.user obs_user
                              FROM latest_obs_ids L
                              LEFT JOIN Station S on (S.station_num = L.obs_station_number)
                              group by object_number)
                ,obj_with_categories as (
							    SELECT LU.*, U.comments obj_comments, U.purpose obj_purpose, U.purpose_detailed obj_purpose_detailed,
								U.country_owner obj_country_owner, SatCat.name obj_name, SatCat.launch_date obj_launch_date, SatCat.orbit_status_code,
								C.obj_no, C.sub_category, C.description as CT_description, C.obj_categories
							  FROM latest_obs_with_users LU
                              LEFT JOIN ucs_SATDB U ON (LU.object_number = U.norad_number)
                              LEFT JOIN celestrak_SATCAT SatCat ON (LU.object_number = SatCat.sat_cat_id)
                              LEFT JOIN (
                              		SELECT obj_no, sub_category, description, GROUP_CONCAT(sub_category SEPARATOR ', ') as obj_categories
                              		FROM categories
                              		GROUP BY obj_no
                              	) AS C ON LU.object_number = C.obj_no
                              )
              SELECT
                IODs.*,
                Obs.eth_addr obs_eth_addr, Obs.name obs_user_name,
                CONCAT_WS(' — ',CT_description, obj_categories, obj_purpose_detailed, obj_comments) as obj_merged_description
                                  FROM obj_with_categories as IODs
              LEFT JOIN Observer Obs on (IODs.obs_user = Obs.id)
			  )
        """
        self.selectCatalogJsonObject = """
          Json_Object(
              'object_norad_number', object_number,
              'object_name', obj_name,
              'object_origin', obj_country_owner,
              'object_type', obj_purpose,
              'object_primary_purpose', obj_purpose_detailed,
              'object_secondary_purpose', obj_comments,
              'object_merged_description', obj_merged_description,
              'object_observation_quality', %(QUALITY)s,
              'object_launch_date', obj_launch_date,
              'time_last_tracked', date_format(obs_time, '%M %d, %Y'),
              'address_last_tracked', obs_eth_addr,
              'username_last_tracked',obs_user_name)
        """
        self.addParsedIOD_query = '''INSERT INTO ParsedIOD (
            submitted,
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
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
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
            tle_file_fingerprint
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
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
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
            object_number               MEDIUMINT(5) UNSIGNED,          /* NORAD number */
            international_designation   VARCHAR(14),                    /* International designation */
            station_number              SMALLINT(4) UNSIGNED NOT NULL,  /* Station number that made observation */
            station_status_code         CHAR(1),        /* Packed code of station status - unpacked in station_status table */
            obs_time_string             VARCHAR(27),    /* Source ascii string for observation time (for IOD.py debugging) */
            obs_time                    DATETIME(6),    /* Exact time of observation */
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
            epoch                       DATETIME(6) NOT NULL,  /* FIXME: Python Datetime of TLE epoch. Rename to epoch_datetime for clarity */
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
            tle_file_fingerprint        CHAR(32),          /* MD5 fingerprint of the file this record was imported from (optional) */
            import_timestamp            TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,   /* Timestamp of record creation */
            KEY `TLE_epoch_idx` (`epoch`) USING BTREE,
            KEY `TLE_sat_name_idx` (`sat_name`(24)) USING BTREE,
            UNIQUE KEY `TLE_tle_fingerprint_idx` (`tle_fingerprint`(33)) USING BTREE,
            KEY `TLE_tle_file_fingerprint_idx` (`tle_file_fingerprint`(33)) USING BTREE,
            KEY `TLE_norad_idx` (`satellite_number`) USING BTREE
        )''' + self.charset_string
        self.c.execute(createquery)
        self.conn.commit()

        createquery = '''CREATE TABLE IF NOT EXISTS TLEFILE (
            file_id                 INTEGER PRIMARY KEY''' + self.increment + ''', /* Unique internal record ID */
            file_fingerprint        CHAR(32) NOT NULL, /* MD5 finger print of file */
            source_filename         TINYTEXT,          /* Name of source file */
            import_timestamp        TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, /* Timestamp of record creation */
            UNIQUE KEY `TLEFILE_file_fingerprint_33_idx` (`file_fingerprint`(33)) USING BTREE
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


    def addParsedIOD(self, entryList, submit_time, fast_import = False):
        """ Add an IOD entry to the database
        Input: IOD-formatted line
        """
        iteration = 0
        error_messages = []
        for entry in entryList:
            # Create fingerprint string from the time and position data only
            # Should uniquely identify the observation
            # Note that this will have uniqueness problems with people who report time but not position (roll call posts)
            iteration += 1
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
                error_messages.append("Observation on line: {} has already submitted.".format(iteration))
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
                    try:
                        self._IODentryList.append(newentryTuple)
                        self._IODPendingEntryFingerprintList.append(obsFingerPrint)
                    except Exception as e:
                        log.error("{}".format(e))
        return (len(self._IODentryList), error_messages)
        # return self.c_addParsedIOD.lastrowid

    def addObserverParsedIOD(self, text_block):
        """ Add observations to database.
        Take in a text block and parses then submits observations to the database.

        Input:
            text_block - Block of text that will be checked for observation format then submit
                those observations to the database.

        Output:
            Tuple(
                success - Integer stating how many successful submissions were added to the database.
                error_messages - array of strings describing any problematic lines submitted.
            )
        """
        success = 0
        error_messages = []
        removed_iods = {}
        it = 0
        parsed_iod = []
        multiple = text_block
        try:
            parsed_iod = iod.parse_iod_lines(multiple)
            if len(parsed_iod):
                for item in multiple.split('\n'):
                    temp_iod = iod.parse_iod_lines(item)
                    it += 1
                    if temp_iod:
                        removed_iods[it] = False
                    else:
                        error_messages.append("Observation on line {} did not match IOD format.".format(it))
                        removed_iods[it] = True
        except:
            print("Not IOD")
        if not parsed_iod:
            try:
                parsed_iod = iod.parse_uk_lines(multiple)
                if len(parsed_iod):
                    for item in multiple.split('\n'):
                        temp_iod = iod.parse_uk_lines(item)
                        it += 1
                        if temp_iod:
                            removed_iods[it] = False
                        else:
                            error_messages.append("Observation on line {} did not match UK format.".format(it))
                            removed_iods[it] = True
            except:
                print("Not UK")
        if not parsed_iod:
            try:
                parsed_iod = iod.parse_rde_record(multiple)
                if len(parsed_iod):
                    rde_multiple = multiple.split('\n')
                    for i in range(0, len(parsed_iod)-2):
                        temp_iod = iod.parse_rde_record("{}\n{}\n{}".format(rde_multiple[i], rde_multiple[i+1], rde_multiple[i+2]))
                        it += 1
                        if temp_iod:
                            i += 2
                            removed_iods[it] = False
                            removed_iods[it+1] = False
                            removed_iods[it+2] = False
                            it += 2
                        else:
                            error_messages.append("Observation on line {} did not match RDE format.".format(it))
                            removed_iods[it] = True
                    #check each line as starting point and roll through parsing
                    #After all this chaos, go ahead and try to add it to the db
            except:
                print("Not RDE")
        submission_time = datetime.now()
        it = 0
        try:
            #one at a time, line up the items in parsed_iod so they can be checked against the original array of observations, otherwise the numbers returned back won't be aligned with the original lines
            for entry in parsed_iod:
                it += 1
                individual_entry = []
                individual_entry.append(entry)
                entry_value = self.addParsedIOD(individual_entry, submission_time)
                print(entry_value[0])
                success = entry_value[0]
                while removed_iods[it] == True:
                    it += 1
                if entry_value[0] == 0:
                    error_messages.append("Observation on line {} has already been submitted.".format(it))
        except Exception as e:
            error_messages.append("Could not determine observation format.")
            print(e)
        if success > 0:
            self.commit_IOD_db_writes()
        return (success, error_messages)

    def addObserver(self,
            eth_addr,
            verification,
            reputation,
            first_line):

        username = generateUsername()

        self._new_observerid += 1

        observerTuple = (
            self._new_observerid, # Use the AUTO_INCREMENT-ed value
            eth_addr,
            username,
            reputation,
            first_line
            )

        observerEmailTuple = (
            self._new_observerid,
            verification
            )

        if self._dbtype == "INFILE": # Make CSV files
            self._writer_Observer.writerow(observerTuple)
            self.c.execute(self.addObserverEmail_query, observerEmailTuple)
            self._observerDict[verification] = self._new_observerid
        elif self._dbtype == "sqlite":
            try:
                self.c.execute(self.addObserver_query,observerTuple)
                self.c_addObserverEmail_query.execute(self.addObserverEmail_query, observerEmailTuple)
                self.conn.commit()
            except sqlite3.IntegrityError as e:
                log.error("{}".format(e))
        else:
            try:
                self.c_addObserver_query.execute(self.addObserver_query, observerTuple)
                self.c_addObserverEmail_query.execute(self.addObserverEmail_query, observerEmailTuple)
                self.conn.commit()
            except Exception as e:
                log.error("MYSQL ERROR: {}".format(e))
        return self._new_observerid

    def addObserverEmail(self, user_id, email):
        try:
            self.c_addObserverEmail_query.execute(self.addObserverEmail_query, [user_id, email])
            self.conn.commit()
            return user_id
        except Exception as e:
            log.error("MYSQL ERROR: {}".format(e))
            return None


    def addTLE(self, entry):
        """ Ready a TLE entry for INSERT into the database.

        For a "sqlserver" database, the INSERT is not performed. This must be done by calling
        write_TLEs_to_db() or commit_TLE_db_writes()

        Input: TruSatellite() object
        """
        # TODO: add mean_motion_radians_per_minute from the TLE class to here
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
            entry.tle_file_fingerprint
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


    def addTruSatTLE(self, TruSatTLE, TLE_process, tle_source_id, tle_start_rms, tle_result_rms, remarks, satellite_number=False, tle_result_id=False):
        """ Add an TruSat-derived TLE entry to the database, concurrently with its TLE_process records
        Perform as an atomic commit of all records, or bail.

        Inputs:
         - TruSatTLE - TruSatellite() object
         - TLE_process - Dictionary of IOD.obs_id entries and their corresponding process data

        Outputs:
         - Success/Fail

        Set TruSatTLE = False to update process table from existing TLEs (testing)
        """
        TLE_process_list = []

        if (TruSatTLE):
            # TODO: add mean_motion_radians_per_minute from the TLE class to here
            satellite_number = TruSatTLE.satellite_number
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
                TruSatTLE.tle_file_fingerprint
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
                satellite_number,
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
                entry.tle_file_fingerprint,
                entry._tle_basename
                )

        if self._dbtype == "INFILE": # Make CSV files
            self._writer_TLEFile.writerow(newentryTuple)
            self._TLEFileDict[entry.tle_file_fingerprint] = entry._tle_basename
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
        query_tuple = ()
        query_tmp = "SELECT * FROM Station WHERE station_num IN ( "

        first = True
        for station in requested_station_list:
            if (first):
                query_tmp = query_tmp + " %s "
                query_tuple += (station,)
                first = False
            else:
                query_tmp = query_tmp + ", %s "
                query_tuple += (station,)
        query_tmp = query_tmp + ") ORDER BY station_num ASC;"

        self.cdict.execute(query_tmp, query_tuple)
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

    def updateObserverNonceBytes(self, nonce, public_address):
        """ Update the nonce of a user based on their public address.
        The nonce is used to check that a user can sign a message with a random number to verify ownership
        of the specified public address.

        Input:
            nonce - random number smaller than 255 bytes
            public_address - address the user is claiming to own
        """

        if self._dbtype == "sqlite":
            self.c.execute(self.updateObserverNonceBytes_query, [nonce, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverNonceBytes_query.execute(self.updateObserverNonceBytes_query, [nonce, public_address])
            self.conn.commit()
        return True

    def updateObserverJWT(self, jwt, password, public_address):
        """ Update the JWT for a user who owns the provided public address.
        The JWT provides a method to verify user without a signed message with every interaction.

        Input:
            jwt - JSON Web Tokens used to verify login
            public_address - address of the user who is assigned the JWT
        """
        if self._dbtype == "sqlite":
            self.c.execute(self.updateObserverJWT_query, [jwt, password, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverJWT_query.execute(self.updateObserverJWT_query, [jwt, password, public_address])
            self.conn.commit()
        return True

    def updateObserverUsername(self, username, public_address):
        """ Update the name of the user who owns the provided public address. """
        if self._dbtype == "sqlite":
            self.c.execute(self.updateObserverUsername_query, [username, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverUsername_query.execute(self.updateObserverUsername_query, [username, public_address])
            self.conn.commit()

    def updateObserverEmail(self, email, public_address):
        """ Update the email of the user who owns the provided public address. """
        if self._dbtype == "sqlite":
            self.c.execute(self.updateObserverEmail_query, [email, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverEmail_query.execute(self.updateObserverEmail_query, [email, public_address])
            self.conn.commit()
        return True

    def updateObserverBio(self, bio, public_address):
        """ Update the bio of the user who owns the provided public address. """
        if self._dbtype == "sqlite":
            self.c.execute(self.updateObserverBio_query, [bio, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverBio_query.execute(self.updateObserverBio_query, [bio, public_address])
            self.conn.commit()
        return True

    def updateObserverLocation(self, location, public_address):
        """ Update the location of the user who owns the provided public address. """
        if self._dbtype == "sqlite":
            self.c.execute(self.updateObserverLocation_query, [location, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverLocation_query.execute(self.updateObserverLocation_query, [location, public_address])
            self.conn.commit()
        return True

    def updateObserverPassword(self, password, public_address):
        """ Update the password of the user who owns the provided public address.
        The password is used to verify the owner of an email address by being a secret only
        known to the user, server, and email associated with the server.
        """
        if self._dbtype == "sqlite:":
            self.c.execute(self.updateObserverPassword_query, [password, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverPassword_query.execute(self.updateObserverPassword_query, [password, public_address])
            self.conn.commit()
        return True

    def updateObserverAddress(self, new_address, public_address):
        """ Update the public address of the user who owns the provided public address.
        This is account recovery for an ethereum address where the user can no longer access
        their private key.
        """
        if self._dbtype == "sqlite":
            self.c.execute(self.updateObserverAddress_query, [new_address, public_address])
            results = self.c.fetchone()
        else:
            self.c_updateObserverAddress_query.execute(self.updateObserverAddress_query, [new_address, public_address])
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

    def selectObserverAddressFromEmail(self, email):
        """ Select the public address for a user with the provided email. """
        if self._dbtype == "sqlite":
            self.c.execute(self.selectObserverAddressFromEmail_query, [email])
            results = self.c.fetchone()
        else:
            self.c_selectObserverAddressFromEmail_query.execute(self.selectObserverAddressFromEmail_query, [email])
            try:
                results = self.c_selectObserverAddressFromEmail_query.fetchone()[0]
            except:
                return None
        return results

    def selectEmailFromObserverAddress(self, addr):
        """ Select the email for a user with the provided public address. """
        if self._dbtype == "sqlite":
            self.c.execute(self.selectEmailFromObserverAddress_query, [addr])
            results = self.c.fetchone()
        else:
            self.c_selectEmailFromObserverAddress_query.execute(self.selectEmailFromObserverAddress_query, [addr])
            try:
                results = self.c_selectEmailFromObserverAddress_query.fetchone()[0]
            except:
                return None
            return results

    def selectObserverPasswordFromAddress(self, address):
        """ Select the password for a user with the provided address sent to their email. """
        if self._dbtype == "sqlite":
            self.c.execute(self.selectObserverPasswordFromAddress_query, [address])
            results = self.c.fetchone()
        else:
            self.c_selectObserverPasswordFromAddress_query.execute(self.selectObserverPasswordFromAddress_query, [address])
            try:
                results = self.c_selectObserverPasswordFromAddress_query.fetchone()[0]
            except Exception as e:
                print(e)
                return None
        return results

    def selectObserverAddressFromPassword(self, password):
        """ Select the address for a user with the provided password sent to their email. """
        if self._dbtype == "sqlite":
            self.c.execute(self.selectObserverAddressFromPassword_query, [password])
            results = self.c.fetchone()
        else:
            self.c_selectObserverAddressFromPassword_query.execute(self.selectObserverAddressFromPassword_query, [password])
            try:
                results = self.c_selectObserverAddressFromPassword_query.fetchone()[0]
            except Exception as e:
                print(e)
                return None
        return results

    def getObserverNonceBytes(self, public_address):
        """ Select observer nonce for a user with the provided public address. """
        """ GET OBSERVER NONCE """
        if self._dbtype == "sqlite":
            self.c.execute(self.getObserverNonceBytes_query, [public_address])
            results = self.c.fetchone()
        else:
            self.c_getObserverNonceBytes_query.execute(self.getObserverNonceBytes_query, [public_address])
            results = self.c_getObserverNonceBytes_query.fetchone()
        return results[0].decode('utf-8').strip('\x00')

    def getObserverJWT(self, public_address):
        """ Select observer JWT for a user with the provided public address. """
        if self._dbtype == "sqlite":
            self.c.execute(self.getObserverJWT_query, [public_address])
            results = self.c.fetchone()
        else:
            self.c_getObserverJWT_query.execute(self.getObserverJWT_query, [public_address])
            results = self.c_getObserverJWT_query.fetchone()
            self.conn.commit()
        return results

    def getObserverFromJWT(self, jwt):
        """ Select public address for a user with the provided JWT. """
        query_tmp = '''SELECT eth_addr FROM Observer WHERE jwt="%(JWT)s"'''
        self.c.execute(query_tmp, {'JWT': jwt})
        try:
            return self.c.fetchone()[0]
        except:
            return None

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
                AND obs_id >= %(OBS_ID)s
                ORDER BY obs_id ASC
                LIMIT 10;"""
        self.cdict.execute(query_tmp, {'OBS_ID': obs_id})
        rows = self.cdict.fetchall()
        return self.cdictQueryToObsObj(rows)

    def selectIODlist(self,obs_id_list):
        """ Given the list of specified object IDs, returns an array of corresponding IOD objects """

        query_tuple = ()
        query_tmp = """SELECT * FROM ParsedIOD WHERE
            valid_position=1
            AND obs_id IN ( """

        first = True
        for id in obs_id_list:
            if (first):
                query_tmp = query_tmp + " %s "
                query_tuple += (id,)
                first = False
            else:
                query_tmp = query_tmp + ", %s "
                query_tuple += (id,)
        query_tmp = query_tmp + ") ORDER BY obs_time ASC;"

        self.cdict.execute(query_tmp, query_tuple)
        rows = self.cdict.fetchall()
        return self.cdictQueryToObsObj(rows)


    def selectIODlistSubmitRange(self,noradNumber,startTime,endTime):
        """ For the given object, start and end times, return a list of Observeration objects """

        query_tmp = """SELECT * FROM ParsedIOD
                WHERE valid_position=1
                AND object_number = %(noradNumber)s
                AND submitted >= %(startTime)s
                AND submitted <= %(endTime)s
                AND obs_id NOT IN (SELECT DISTINCT obs_id FROM TLE_process where object_number=%(noradNumber)s)
                AND station_number IN (SELECT DISTINCT station_num FROM Station)
                ORDER BY obs_time ASC;"""

        queryParams = {
          'noradNumber' : noradNumber,
          'startTime': startTime,
          'endTime': endTime
          }

        self.cdict.execute(query_tmp, queryParams)
        rows = self.cdict.fetchall()
        if (len(rows)>0):
            return self.cdictQueryToObsObj(rows)
        else:
            return False

    def getObserverCountByID(self, public_address):
        """ Get number of users with public address to determine if ethereum address has been used. """
        """ GET OBSERVER COUNT BY ID """
        if self._dbtype == "sqlite":
            self.c.execute(self.getObserverCountByID_query, [public_address])
            results = self.c.fetchone()
        else:
            self.c_getObserverCountByID_query.execute(self.getObserverCountByID_query, [public_address])
            results = self.c_getObserverCountByID_query.fetchone()
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

    def findObservationCluster(
      self,
      noradNumber,
      maxMinutesBetweenObservations = 15,
      minObservationCount = 2,
      minObserverCount = 1,
      minSecondsBetweenObservations = 0,
      startDate = datetime(1957,10,4,19,28,34,0)):
        """ Find a cluster of IODs for a particlar object, for use in calculating TLEs.

            Searches for a qualifying time window that satisfies the criteria defined by function parameters.

            When a qualifying time window is found (i.e. containing a qualifying set of observations & observers),
            this query returns the IDs of ALL observations within that time window.

            If more than one qualifying time window is found, the window with the chronologically earliest start is used.

            If more than one qualifying window with the chronologically earliest start is found, the longest such window is used.

            Parameters
            ----------
            noradNumber : int
                The NORAD number of the object we are interested in. Only observations of this object are considered.
            maxMinutesBetweenObservations: int
                The duration in minutes of time window. Must be >= 1
            minObservationCount: int
                The minimum number of observations within the time window. Must be >= `minObserverCount`
            minObserverCount: int
                The minimum number of distinct observers within the time window. Must be 1 <= `minObserverCount` <= `minObservationCount`
            minSecondsBetweenObservations: int
                The minimum time in seconds between qualifying observations within the time window. Must be 0 <= `minSecondsBetweenObservations` < 60 `maxMinutesBetweenObservations`
            startDate : datetime
                All observtions with times that are before or equal to this value are ignored.

            Returns
            -------
            list (int)
                All observation IDs relating to the specified object within the qualifying time window.
        """
        assert (noradNumber is not None), "No NORAD number supplied"
        assert (maxMinutesBetweenObservations >= 1), "maxMinutes must be positive"
        assert (minSecondsBetweenObservations >= 0 and minSecondsBetweenObservations < maxMinutesBetweenObservations * 60), "Invalid minSecondsBetweenObservations"
        assert (minObserverCount >= 1), "minObserverCount must be positive"
        assert (minObservationCount >= 1), "minObservationCount must be positive"

        # FIXME: Shouldn't be necessary, but we may have some incoming date-parsing problems skewing the results by milliseconds
        plus1sec = timedelta(seconds=1)
        startDate += plus1sec

        query = """
            WITH TIME_WINDOW AS (
                WITH OBS_USER AS (
                    SELECT IOD.obs_id, IOD.object_number, IOD.obs_time, Station.user
                    FROM ParsedIOD AS IOD
                    left join Station on (IOD.station_number = Station.station_num)
                    WHERE IOD.object_number = %(noradNumber)s
                              and IOD.obs_time > %(startDate)s)
                SELECT obs_time as result_window_start,
                       addtime(obs_time, sec_to_time(%(maxMinutesBetweenObservations)s * 60)) as result_window_end
                FROM OBS_USER as LAST_OBS_USER
                where (
                  SELECT count(distinct OTHER_OBS_USERS.user)
                  from OBS_USER as OTHER_OBS_USERS
                      where
                          OTHER_OBS_USERS.user != LAST_OBS_USER.user and
                          OTHER_OBS_USERS.obs_time between addtime(LAST_OBS_USER.obs_time,
                                                                   sec_to_time(%(minSecondsBetweenObservations)s))
                                                   and     addtime(LAST_OBS_USER.obs_time,
                                                                   sec_to_time(%(maxMinutesBetweenObservations)s * 60)))
                  >= %(minOtherObservers)s
                and (
                  SELECT count(OTHER_OBS.obs_time)
                  from OBS_USER as OTHER_OBS
                      where
                        OTHER_OBS.obs_id != LAST_OBS_USER.obs_id and
                        OTHER_OBS.obs_time between addtime(LAST_OBS_USER.obs_time,
                                                          sec_to_time(%(minSecondsBetweenObservations)s))
                                               and     addtime(LAST_OBS_USER.obs_time,
                                                          sec_to_time(%(maxMinutesBetweenObservations)s * 60)))
                  >= %(minOtherObservations)s
                order by LAST_OBS_USER.obs_time
                LIMIT 1)
            SELECT obs_id from ParsedIOD
            WHERE object_number = %(noradNumber)s
            AND valid_position = 1
            AND obs_time between (SELECT result_window_start from TIME_WINDOW) and (select result_window_end from TIME_WINDOW);"""

        queryParams = {
          'noradNumber': noradNumber,
          'startDate': startDate,
          'minSecondsBetweenObservations': minSecondsBetweenObservations,
          'maxMinutesBetweenObservations': maxMinutesBetweenObservations,
          # We take a count *excluding* the first observation/user, because it may or may not incuded in the time window
          # Excluding it always means we don't have to cope with both the included and excluded case
          'minOtherObservations': minObservationCount - 1,
          'minOtherObservers': minObserverCount - 1
          }

        self.c.execute(query, queryParams)
        return QueryTupleListToList(self.c.fetchall())

    def findIODsNotUsedInTTLEs(self):
        """ Find IODs that have not yet been used to construct any TruSat TLEs (TTLEs), and index them by their object number
            for easy processing.

            IODs are considered to have been used to construct a TruSat TLE even if their allocated weight was zero, so this
            search is really finding IODs that have not yet undergone any TTLE processing.

            Such IODs / objects are candidates for processing an incremental TLE update.

            Returns
            -------
            dict with an integer key and a non-empty list of integers as a value.
                Key: NORAD number of the object
                Value: the list of obs_ids for this object that have not yet been used for any TTLE processing.

        """
        query = """
            select object_number, obs_id from ParsedIOD P
            where valid_position = 1
            AND object_number is not null
            AND not exists (
                select null
                from TLE_process
                where P.obs_id = TLE_process.obs_id)
            ORDER BY object_number, obs_id;"""
        self.c.execute(query)
        results = self.c.fetchall()

        retVal = {}
        for (key, value) in results:
            if key in retVal:
                retVal[key].append(value)
            else:
                retVal[key] = [value]

        return retVal


    def findObjectsWithIODsNotUsedInTTLEs(self):
        query = """
            SELECT DISTINCT object_number from ParsedIOD
            WHERE valid_position=1
            AND object_number in (SELECT DISTINCT satellite_number from TLE) /* We have a TLE */
            AND obs_id NOT IN (SELECT DISTINCT obs_id FROM TLE_process)      /* It has not been processed */
            ORDER BY object_number ASC;"""
        self.c.execute(query)
        results = self.c.fetchall()
        if results:
            return QueryTupleListToList(results)
        else:
            return False


    def findObjectsWithIODsButNoTLEs(self):
        """ Find the objects that have IODs but no TLEs. Such objects are candidates for a rebuild of TLE history.

            Returns
            -------
            list of one-element (int) tuples
                The NORAD numbers of all objects for which we are aware of one or more IODs but zero TLEs.
        """
        query = """
            SELECT DISTINCT object_number FROM ParsedIOD
            WHERE valid_position = 1
            AND NOT EXISTS (
                SELECT null
                FROM TLE
                WHERE TLE.satellite_number = ParsedIOD.object_number)
            ORDER BY obs_time DESC;"""

        self.c.execute(query)
        return self.c.fetchall()

    def findObjectsWithIODsNewerThanTLE(self):
        """ Find the objects that have IODs that have one or more IODs newer than their most recent TLE.
            Such objects are candidates for an incremental update of their TLE.

            Returns
            -------
            list of one-element (int) tuples
                The NORAD numbers of all objects for which we are aware of IODs newer than their TLE.
        """

        query = """
            WITH most_recent_iods AS (SELECT max(obs_time) AS iod_time, object_number FROM ParsedIOD
                                      WHERE valid_position = 1
                                      GROUP BY object_number),
                most_recent_tles AS (SELECT satellite_number, max(epoch) AS tle_time FROM TLE
                                      GROUP BY satellite_number)
              SELECT object_number
              FROM most_recent_iods
              INNER JOIN most_recent_tles
                ON (most_recent_iods.object_number = most_recent_tles.satellite_number)
              WHERE iod_time > (tle_time + INTERVAL 1 SECOND)
              AND object_number < 70000 /* Skip analyst objects for now */
              ORDER BY object_number;"""

        self.c.execute(query)
        return QueryTupleListToList(self.c.fetchall())

    def findIODsNewerThanPenultimateTLE(self, noradNumber):
        """ For a particular object, find all the IODs newer than the penultimate (second most recent) TLE.
            Such IODs are required input when making an an incremental to the object's TLE.

            If only one TLE exists, we find all IODs newer than that TLE.

            If no TLEs exist, we return zero rows.

            If no IODs newer than the selected TLE exist, we return zero rows.

            Use the result of `findIODsWithoutTLEs` to differentiate between these last two cases.

            Parameters
            ----------
            noradNumber : int
                The NORAD number of the object we are interested in. Only observations of this object are considered.

            Returns
            -------
            list of one-element (int) tuples
                The NORAD numbers of all objects for which we are aware of one or more IODs but zero TLEs.
        """
        query = """
            WITH most_recent_two_tles AS (
              SELECT epoch FROM TLE
              WHERE satellite_number = %(noradNumber)s
              ORDER BY epoch desc
              LIMIT 2)
            SELECT obs_id
            FROM ParsedIOD
            WHERE object_number = %(noradNumber)s
            AND valid_position = 1
            AND obs_time > (SELECT * FROM most_recent_two_tles
                    ORDER BY epoch
                    LIMIT 1);"""

        self.c.execute(query, {'noradNumber': noradNumber})
        return QueryTupleListToList(self.c.fetchall())


    def findDateNewestTTLE(self, noradNumber):
        """ For a particular object, return datetime of the most recent TTLE.
            Such dates are required when resuming the bulk TLE processing from a manual start.

            If no TLEs exist, we return FALSE.

            Parameters
            ----------
            noradNumber : int
                The NORAD number of the object we are interested in. Only observations of this object are considered.

            Returns
            -------
            python datetime
                The datetime of the resulting TTLE
        """
        query = """
            SELECT epoch
            FROM TLE
            WHERE satellite_number = %(noradNumber)s
            AND classification = 'T'
            ORDER BY epoch DESC
            LIMIT 1;"""

        self.cdict.execute(query, {'noradNumber': noradNumber})
        row = [self.cdict.fetchone()]
        if (row[0] is not None):
            TTLEepoch = row[0]["epoch"]
            return TTLEepoch
        else:
            return False


    # FIXME: This can be templated off findDateNewestTTLE
    def findDateNewestTLE(self, noradNumber):
        """ For a particular object, return datetime of the most recent TTLE.
            Such dates are required when resuming the bulk TLE processing from a manual start.

            If no TLEs exist, we return FALSE.

            Parameters
            ----------
            noradNumber : int
                The NORAD number of the object we are interested in. Only observations of this object are considered.

            Returns
            -------
            python datetime
                The datetime of the resulting TTLE
        """
        query = """
            SELECT epoch
            FROM TLE
            WHERE satellite_number = %(noradNumber)s
            ORDER BY epoch DESC
            LIMIT 1;"""

        self.cdict.execute(query, {'noradNumber': noradNumber})
        row = [self.cdict.fetchone()]
        if (row[0] is not None):
            TLEepoch = row[0]["epoch"]
            return TLEepoch
        else:
            return False


    def findFirstIODandTLE(self, noradNumber):
        """ For testing.  For a particular object, find the (submitted) date of the first observation, and the first TLE after it.
        Using submitted time instead of obs_time as the TLEs get created in the order the observations are submitted/received.

        Return TLE as TruSatellite() object.
        We can assume the first range starts at zero time, and use the epoch of the TLE as the end of the next range.
        """

        # Get submitted time of next obs_id NOT in TLE_process
        query_tmp = """SELECT submitted FROM ParsedIOD
            WHERE object_number=%(SATELLITE_NUMBER)s
            AND obs_id NOT IN (SELECT DISTINCT obs_id FROM TLE_process where object_number=%(SATELLITE_NUMBER)s)
            AND station_number IN (SELECT DISTINCT station_num from Station)
            ORDER BY submitted ASC
            LIMIT 1"""
        query_parameters = {'SATELLITE_NUMBER': noradNumber}
        self.cdict.execute(query_tmp, query_parameters)
        row = [self.cdict.fetchone()][0]    # Put single result into an array
        earliest_submitted = row["submitted"]

        query_tmp = """SELECT * FROM TLE
            WHERE satellite_number=%(SATELLITE_NUMBER)s
            AND epoch > %(EPOCH)s
            ORDER BY epoch ASC
            LIMIT 1"""
        query_parameters = {'SATELLITE_NUMBER': noradNumber,
                            'EPOCH': earliest_submitted}
        self.cdict.execute(query_tmp, query_parameters)
        row = [self.cdict.fetchone()]    # Put single result into an array
        return self.cdictQueryToTruSatelliteObj(row)[0]  # Unpack the array to the object, for just one result


    def findNextUnprocessedTLE(self,noradNumber,epoch):
        """ For testing.  For a particular object, the next TLE by epoch time.
        Consult TLE process where there might be multiple TLEs for a given epoch.

        Return TLE as TruSatellite() object."""
        query_tmp = """SELECT * FROM TLE
            WHERE satellite_number=%(SATELLITE_NUMBER)s
            AND epoch > %(EPOCH)s
            AND tle_id NOT IN (SELECT DISTINCT tle_result_id from TLE_process)
            ORDER BY epoch ASC
            LIMIT 1"""
        query_parameters = {'SATELLITE_NUMBER': noradNumber,
                            'EPOCH': epoch}
        self.cdict.execute(query_tmp, query_parameters)
        row = [self.cdict.fetchone()]    # Put single result into an array
        if row[0] is not None:
            return self.cdictQueryToTruSatelliteObj(row)[0]  # Unpack the array to the object, for just one result
        else:
            return False


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
            LIMIT %(OFFSET)s,%(FETCH)s;"""
        query_parameters = {
            'OFFSET': offset_row_count,
            'FETCH': fetch_row_count}
        self.c.execute(query_tmp, query_parameters)
        return stringArrayToJSONArray(self.c.fetchall())


    def selectUserObservationStats(self, user_id):
        """ Selects the complete user observation history with all information necessary
        to review/revise user rank / weight """
        query_tmp = """
          WITH user AS (
            SELECT id
            FROM Observer
          )
          , user_stations AS (
            SELECT U.id user_id, S.station_num
            FROM user U
            LEFT JOIN Station S on (U.id = S.user)
          )
          , user_observations AS (
            SELECT
             US.user_id user_id,
             P.obs_id obs_id,
			 P.submitted submitted,
			 P.obs_time obs_time,
			 P.object_number object_number,
			 P.station_number station_number,
			 P.time_uncertainty time_uncertainty,
             TP.process_id as process_id,
             TP.tle_source_id as tle_source_id,
             TP.tle_result_id as tle_result_id,
             TP.aspect as aspect,
             TP.cross_track_err as cross_track_err,
             TP.time_err as time_err,
             TP.position_err as position_err,
             TP.obs_weight as obs_weight,
             TP.tle_start_rms as tle_start_rms,
             TP.tle_result_rms as tle_result_rms,
             (TP.tle_result_rms - TP.position_err) as rms_diff
            FROM user_stations US
            LEFT JOIN ParsedIOD P on (US.station_num = P.station_number)
            JOIN TLE_process TP on (TP.obs_id = P.obs_id)
            ORDER BY P.obs_time DESC
          )
			SELECT *
			FROM user_observations Obs
			WHERE user_id = %(USER_ID)s
            ORDER BY user_id, obs_time ASC;"""
        query_parameters = {'USER_ID': user_id}
        self.c.execute(query_tmp, query_parameters)
        try:
            return self.c.fetchall()
        except:
            return None


    def selectObjectHistoryByMonth_JSON(self, norad_number, year):
        """ For a particular object, provide a navigation structure of its full observation history

            Inputs: NORAD number of interest, year
            Output: JSON object with observation summary

            Note (Chris) - not sure this is being used currently
        """
        query_tmp = """SELECT Json_Object(
            'id', ParsedIOD.obs_id,
            'observation_time', UNIX_TIMESTAMP(ParsedIOD.obs_time),
            'observation_quality', TLE_process.tle_start_rms,
            'observation_time_difference', TLE_process.time_err,
            'observation_position_error', TLE_process.position_err,
            'observation_cross_track_error', TLE_process.cross_track_err,
            'observation_weight', TLE_process.obs_weight
            )
            FROM ParsedIOD
            LEFT JOIN TLE_process ON ParsedIOD.obs_id = TLE_process.obs_id
            WHERE ParsedIOD.object_number=%(NORAD_NUMBER)s
            AND Year(obs_time)=%(YEAR)s
            ORDER BY obs_time DESC"""
        query_parameters = {
                'NORAD_NUMBER': norad_number,
                'YEAR': year}
        self.c.execute(query_tmp, query_parameters)
        history_by_month = stringArrayToJSONArray_JSON(self.c.fetchall())
        for entry in history_by_month:
            try:
                user_information_query = '''SELECT station_number
                FROM ParsedIOD
                WHERE obs_id=%(ID)s'''
                query_parameters = {'ID': entry["id"]}
                entry.pop('id', None)
                self.c.execute(user_information_query, query_parameters)
                station_number = self.c.fetchone()[0]
                user_information_query = '''SELECT Observer.name, Observer.eth_addr, Observer.location
                FROM Observer
                INNER JOIN Station
                ON Station.user=Observer.id
                WHERE Station.station_num=%(STATION_NUMBER)s'''
                query_parameters = {'STATION_NUMBER': station_number}
                self.c.execute(user_information_query, query_parameters)
                (username, address, location) = self.c.fetchone()
                entry['username'] = username
                entry['user_address'] = address
                if location == None:
                    entry['user_location'] = ''
                else:
                    entry['user_location'] = location
            except Exception as e:
                print(e)
        return history_by_month

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
            WHERE object_number = %(NORAD_NUM)s
            AND valid_position=1
            GROUP BY observation_year, observation_month, observation_day
            ORDER BY observation_year DESC, observation_month ASC, observation_day ASC;"""
        query_parameters = {
            'NORAD_NUM': norad_num}
        self.c.execute(query_tmp, query_parameters)
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
            TLE.line0            = row["line0"]
            TLE.line1			 = row["line1"]
            TLE.line2			 = row["line2"]

            TLE.sat_name = TLE.name	            = row["sat_name"]
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
            TLE.tle_file_fingerprint = row["tle_file_fingerprint"]
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


    # FIXME: Make this function prefer TruSatellite TLEs
    def selectTLEEpochBeforeDate(self, query_epoch_datetime, satellite_number):
        """ Query to return the first TLE with epoch *prior* to specified date for a specific satellite number

        Returns TruSatellite() object
        """

        query_tmp = """SELECT * FROM TLE
            WHERE epoch <= %(EPOCH_DATETIME)s
            AND satellite_number=%(SATELLITE_NUMBER)s
            ORDER BY epoch DESC
            LIMIT 1"""
        query_parameters = {'EPOCH_DATETIME': query_epoch_datetime,
            'SATELLITE_NUMBER': satellite_number}
        self.cdict.execute(query_tmp, query_parameters)
        row = [self.cdict.fetchone()]   # Put single result into an array
        return self.cdictQueryToTruSatelliteObj(row)[0]  # Unpack the array to the object, for just one result


    # FIXME: Make this function prefer TruSatellite TLEs
    def selectTLEEpochNearestDate(self, query_epoch_datetime, satellite_number):
        """ Query to return the *nearest* TLE with epoch for a specific satellite for a specified date

        Could be before or after the provided date.
        Returns TruSatellite() object
        """
        # query_epoch_datetime_string = query_epoch_datetime.isoformat(timespec='microseconds')

        query_tmp = """SELECT *,ABS(TIMEDIFF(epoch,%(EPOCH_DATETIME)s)) as diff FROM TLE
            WHERE satellite_number=%(SATELLITE_NUMBER)s
            ORDER BY diff ASC
            LIMIT 1"""
        query_parameters = {'EPOCH_DATETIME': query_epoch_datetime,
            'SATELLITE_NUMBER': satellite_number}
        self.cdict.execute(query_tmp, query_parameters)
        row = [self.cdict.fetchone()]    # Put single result into an array
        return self.cdictQueryToTruSatelliteObj(row)[0]  # Unpack the array to the object, for just one result


    def selectTLEid(self, tle_id):
        """ Query to return the specific tle_id requested

        Returns TruSatellite() object
        """
        query_tmp = """SELECT * FROM TLE
            WHERE tle_id=%(TLE_ID)s
            LIMIT 1"""
        query_parameters = {'TLE_ID': tle_id}
        self.cdict.execute(query_tmp, query_parameters)
        row = [self.cdict.fetchone()]    # Put single result into an array
        return self.cdictQueryToTruSatelliteObj(row)[0]  # Unpack the array to the object, for just one result


    def selectTLEid(self, tle_id):
        """ Query to return the specific tle_id requested

        Returns TruSatellite() object
        """
        query_tmp = """SELECT * FROM TLE
            WHERE tle_id=%(TLE_ID)s
            LIMIT 1"""
        query_parameters = {'TLE_ID': tle_id}
        self.cdict.execute(query_tmp, query_parameters)
        row = [self.cdict.fetchone()]    # Put single result into an array
        return self.cdictQueryToTruSatelliteObj(row)[0]  # Unpack the array to the object, for just one result


    # FIXME - This is the latest of everything in the catalog - but some will be old from McCants stuff because they were dropped from classfd.tle
    def selectTLE_Astriagraph(self):
        """ Create a list of TLEs appropriate for Astriagraph to plot.

        Not currently used.
        """

        query_tmp = self.selectLatestTLEPerObject + """
            ORDER BY TLE.satellite_number;"""
        self.c.execute(query_tmp)
        result = ""
        for (line0, line1, line2, _, _) in self.c.fetchall():
            if line0 is not None and line1 is not None and line2 is not None:
                result = result + "{}\n{}\n{}\n".format(line0,line1,line2)
        return result

    # https://consensys-cpl.atlassian.net/browse/MVP-285
    def selectTLE_all(self):
        """ Create a full list of TLEs for all unique objects in the database.
        """

        query_tmp = self.selectLatestTLEPerObject + """
  		    AND DATEDIFF(NOW(),TLE.epoch) <= 365
            ORDER BY TLE.satellite_number;"""
        self.c.execute(query_tmp)
        result = ""
        for (line0, line1, line2, _, _) in self.c.fetchall():
            if line0 is not None and line1 is not None and line2 is not None:
                result = result + "{}\n{}\n{}\n".format(line0,line1,line2)
        return result


    # https://consensys-cpl.atlassian.net/browse/MVP-286
    def selectTLE_priorities(self):
        """ Create list of priority TLEs
        """
        # TODO: Replace with real priority sort. https://consensys-cpl.atlassian.net/browse/MVP-389
        # In the meantime, return TLEs older than 30 days, oldest first
        query_tmp = self.selectLatestTLEPerObject + """
            WHERE DATEDIFF(NOW(),TLE.epoch) > 30
  		    AND DATEDIFF(NOW(),TLE.epoch) <= 365
            ORDER BY TLE.epoch DESC;"""
        self.c.execute(query_tmp)
        result = ""
        for (line0, line1, line2, _, _) in self.c.fetchall():
            if line0 is not None and line1 is not None and line2 is not None:
                result = result + "{}\n{}\n{}\n".format(line0,line1,line2)
        return result

    # https://consensys-cpl.atlassian.net/browse/MVP-287
    def selectTLE_high_confidence(self):
        """ Create list of high confidence TLEs
        """
        # TODO: Replace with real confidence sort. https://consensys-cpl.atlassian.net/browse/MVP-390
        # In the meantime, return TLEs younger than 30 days, newest first
        query_tmp = self.selectLatestTLEPerObject + """
            WHERE DATEDIFF(NOW(),TLE.epoch) < 30
            ORDER BY TLE.epoch DESC;"""
        self.c.execute(query_tmp)
        result = ""
        for (line0, line1, line2, _, _) in self.c.fetchall():
            if line0 is not None and line1 is not None and line2 is not None:
                result = result + "{}\n{}\n{}\n".format(line0,line1,line2)
        return result

    # https://consensys-cpl.atlassian.net/browse/MVP-385
    def selectTLE_single(self, norad_num):
        """ Provide the most recent TLE for a given NORAD number """

        query_tmp = """SELECT line0, line1, line2
            FROM TLE
            WHERE satellite_number=%(NORAD_NUM)s
            ORDER BY EPOCH DESC
            LIMIT 1;"""
        query_parameters = {'NORAD_NUM': norad_num}
        self.c.execute(query_tmp, query_parameters)
        try:
            (line0, line1, line2) = self.c.fetchone()
            return "{}r\n{}\n{}\n".format(line0,line1,line2)
        except Exception as e:
            print(e)
            return None

    def write_TLEs_to_db(self):
        """Process a stored query batch for all the TLEs in _TLEentryList.

        Does not commit the transaction. Useful for testing where we do not want to commit changes.

        Returns cursor.lastrowid after all inserts have completed, i.e. the ID of the most
        recently inserted TLE.
        """
        assert(self._dbtype == "sqlserver")
        if(len(self._TLEentryList) > 0):
            try:
                self.c_addTLE_query.executemany(self.addTLE_query,self._TLEentryList)
                self._TLEentryList = []
            except Exception as e:
                log.error("MYSQL ERROR: {}".format(e))
        return self.c_addTLE_query.lastrowid

    def commit_TLE_db_writes(self):
        """Process a stored query batch for all the TLEs in a file at once.

        Note that for large TLE files (50,000 entries, we might want to batch this at 1,000 per per something)
        That's not an issue for the small McCants files
        """
        if (self._dbtype == "sqlserver"):
            self.write_TLEs_to_db()
        if (self._dbtype != "INFILE"):
            self.conn.commit()

    def get_TLE(self, TLE_ID):
        """Returns a TruSatellite with the specified TLE_ID, or None if no such TLE exists.
        """
        assert(self._dbtype == "sqlserver")
        query = """SELECT * FROM TLE WHERE tle_id = %(TLE_ID)s;"""
        queryParams = {'TLE_ID': TLE_ID}

        self.cdict.execute(query, queryParams)
        rows = self.cdict.fetchall()
        if len(rows) > 0:
            return self.cdictQueryToTruSatelliteObj(rows)[0]
        else:
            return None

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
            WHERE Observer.eth_addr = %(ETH_ADDR)s
            ORDER BY Station.station_num ASC;"""
        query_parameters = {'ETH_ADDR': eth_addr}
        try:
            self.c.execute(query_tmp, query_parameters)
            return stringArrayToJSONArray(self.c.fetchall())
        except:
            return None

    def selectUserStationNumbers_JSON(self, eth_addr):
        query_tmp = """SELECT Json_Object(
            'station_number', Station.station_num)
            FROM Station
            JOIN Observer ON Observer.id = Station.user
            WHERE Observer.eth_addr = %(ETH_ADDR)s
            ORDER BY Station.station_num ASC;"""
        query_parameters = {'ETH_ADDR': eth_addr}
        try:
            self.c.execute(query_tmp, query_parameters)
            return stringArrayToJSONArray_JSON(self.c.fetchall())
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
        query_tmp_num_obj_tracked = """SELECT COUNT(DISTINCT(ParsedIOD.object_number))
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num
            JOIN Observer ON Observer.id = Station.user
            WHERE Observer.eth_addr = %(ETH_ADDR)s;"""
        query_parameters = {'ETH_ADDR': eth_addr}
        self.c.execute(query_tmp_num_obj_tracked, query_parameters)
        try:
            obj_tracked = self.c.fetchone()
            (num_obj_tracked,) = obj_tracked
        except Exception as e:
            print("number of objects fail")
            print(e)
            num_obj_tracked = 0

        # Get count of observations for this user
        query_tmp_obs_count = """SELECT COUNT(ParsedIOD.object_number) as obs_count
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num
            JOIN Observer ON Observer.id = Station.user
            WHERE Observer.eth_addr = %(ETH_ADDR)s;"""
        query_parameters = {'ETH_ADDR': eth_addr}
        self.c.execute(query_tmp_obs_count, query_parameters)
        try:
            [(obs_count)] = self.c.fetchone()
        except Exception as e:
            print("object count failed")
            print(e)
            obs_count = 0

        query_tmp_first_obs = """SELECT date_format(ParsedIOD.obs_time, '%M %d, %Y')
            FROM ParsedIOD
            JOIN Station ON ParsedIOD.station_number = Station.station_num
            JOIN Observer ON Observer.id = Station.user
            WHERE Observer.eth_addr = %(ETH_ADDR)s
            ORDER BY obs_time ASC LIMIT 1;"""
        query_parameters = {'ETH_ADDR': eth_addr}
        self.c.execute(query_tmp_first_obs, query_parameters)
        try:
            [(user_first_observation)] = self.c.fetchone()
        except Exception as e:
            print("first object failed")
            print(e)
            user_first_observation = ''

        query_tmp_email = """SELECT Observer_email.email
            FROM Observer_email
            INNER JOIN Observer
            ON Observer_email.user_id=Observer.id
            WHERE Observer.eth_addr=%(ETH_ADDR)s LIMIT 1"""
        query_parameters = {'ETH_ADDR': eth_addr}
        self.c.execute(query_tmp_email, query_parameters)
        try:
            email = self.c.fetchone()[0]
        except Exception as e:
            print(e)
            email = ''

        query_tmp = """SELECT Json_Object(
            'user_name', Observer.name,
            'email', %(EMAIL)s,
            'user_address', Observer.eth_addr,
            'user_location', Observer.location,
            'number_objects_tracked', %(NUM_OBJ_TRACKED)s,
            'observation_count', %(OBS_COUNT)s,
            'user_first_observation', %(USER_FIRST_OBS)s,
            'average_observation_quality', %(AVG_OBS_QUALITY)s,
            'user_bio', Observer.bio,
            'user_image', Observer.url_image)
            FROM Observer
            WHERE Observer.eth_addr = %(ETH_ADDR)s
            LIMIT 1;"""
        query_parameters = {
                'EMAIL': email,
                'NUM_OBJ_TRACKED': num_obj_tracked,
                'OBS_COUNT': obs_count,
                'USER_FIRST_OBS': user_first_observation,
                'AVG_OBS_QUALITY': avg_obs_quality,
                'ETH_ADDR': eth_addr}
        self.c.execute(query_tmp, query_parameters)
        return QueryRowToJSON_JSON(self.c.fetchone())

    # Supports user profile https://consensys-cpl.atlassian.net/browse/MVP-311
    # Notes about endpoint https://consensys-cpl.atlassian.net/browse/MVP-328
    def selectUserObservationHistory_JSON(self, eth_addr, fetch_row_count=100, offset_row_count=0):
        """ Return the observation history for a particular ETH addresses, starting with most
        recent observations.
        """
        # TODO (work in progress): Replace fake data with real data https://consensys-cpl.atlassian.net/browse/MVP-388
        # Need to remove observation_quality when John is done with front-end implementation

        query = """
          WITH user AS (
            SELECT id
            FROM Observer
            WHERE eth_addr = %(ETH_ADDR)s
          )
          , user_stations AS (
            SELECT U.id user_id, S.station_num
            FROM user U
            LEFT JOIN Station S on (U.id = S.user)
          )
          , user_observations AS (
            SELECT US.*, P.*
            FROM user_stations US
            LEFT JOIN ParsedIOD P on (US.station_num = P.station_number)
            WHERE valid_position = 1
            order by P.obs_time DESC
            LIMIT %(OFFSET)s,%(FETCH)s
          )
          SELECT Json_Object(
            'observation_time',date_format(Obs.obs_time, '%M %d, %Y'),
            'object_name',celestrak_SATCAT.name,
            'station_number', Obs.station_num,
            'object_norad_number', Obs.object_number,
            'observation_quality', TLE_process.tle_start_rms,
            'observation_time_difference', TLE_process.time_err,
            'observation_weight', TLE_process.obs_weight,
            'observation_position_error', TLE_process.position_err,
            'observation_cross_track_error', TLE_process.cross_track_err,
            'observation_iod', Obs.iod_string
            )
          FROM user_observations Obs
          LEFT JOIN celestrak_SATCAT ON Obs.object_number = celestrak_SATCAT.norad_num
          LEFT JOIN station_status ON Obs.station_status_code = station_status.code
          LEFT JOIN TLE_process ON Obs.obs_id = TLE_process.obs_id;
        """
        queryParams = {
            'ETH_ADDR': eth_addr,
            'OFFSET': offset_row_count,
            'FETCH': fetch_row_count
        }
        self.c.execute(query, queryParams)
        return stringArrayToJSONArray_JSON(self.c.fetchall())

    def selectUserObjectsObserved_JSON(self, eth_addr, fetch_row_count=100, offset_row_count=0):
        #!TODO: seems odd that we don't return the time at which the user in question last tracked this object.
        """ For a given ETH address, return list of objects they have observed along with context detail.

            Some of the info returned (notably observation_quality) refers to the observation made by the selected user.

            Some of the info returned (notably username_last_tracked, time_last_tracked, address_last_tracked) refers
            to the most recent observation of the same object by any user.
        """
        query = """
          -- Our user's ID
          WITH user AS (
            SELECT id, name
            FROM Observer
            WHERE eth_addr = %(ETH_ADDR)s
          )
          -- Our user's stations
          , user_stations AS (
            SELECT U.id user_id, U.name user_name, S.station_num
            FROM user U
            LEFT JOIN Station S on (U.id = S.user)
          )
          -- The objects our user has viewed, and the times they last viewed them
          , user_objects AS (
            SELECT US.user_id, US.station_num, US.user_name, P.object_number, max(P.obs_time) as user_obs_time
            FROM user_stations US
            LEFT JOIN ParsedIOD P on (US.station_num = P.station_number)
            WHERE valid_position = 1
            GROUP BY US.user_id, US.station_num, US.user_name, P.object_number
            order by user_obs_time DESC
            LIMIT %(OFFSET)s,%(FETCH)s
          )
          -- The objects our user has viewed, and the times they last viewed them
          , user_objects_with_station_status_code AS (
            SELECT obj.*, P.station_status_code
            FROM user_objects obj
            LEFT JOIN ParsedIOD P on (obj.object_number = P.object_number AND obj.user_obs_time = P.obs_time AND obj.station_num = P.station_number)
            WHERE valid_position = 1
            GROUP BY obj.user_id, obj.station_num, obj.user_name, obj.object_number, obj.user_obs_time, P.station_status_code
          )
          -- The times that *anyone* last viewed these objects
          , last_observations AS (
            SELECT UO.user_id, UO.user_name, UO.object_number, UO.user_obs_time, UO.station_status_code, P.station_number, max(obs_time) last_obs_time
            FROM user_objects_with_station_status_code UO
            LEFT JOIN ParsedIOD P on (UO.object_number = P.object_number)
            WHERE valid_position = 1
            GROUP BY UO.user_id, UO.user_name, UO.object_number, UO.user_obs_time, UO.station_status_code, P.object_number
          )
          -- The observer who last viewed these objects (if multiple, we pick one arbitrarily)
          , last_observers AS (
            SELECT LO.*, Observer.name last_observer_name, Observer.eth_addr last_observer_eth_addr
            FROM last_observations LO
            LEFT JOIN ParsedIOD P on (LO.object_number = P.object_number and LO.last_obs_time = P.obs_time)
            LEFT JOIN Station on (P.station_number = Station.station_num)
            LEFT JOIN Observer on (Station.user = Observer.id)
            WHERE valid_position = 1
            GROUP BY LO.user_id, LO.user_name, LO.object_number, LO.user_obs_time, LO.station_status_code, LO.station_number, LO.last_obs_time, P.station_number
          )
          SELECT Json_Object(
            'object_origin', ucs_SATDB.country_owner,
            'object_type', ucs_SATDB.purpose,
            'object_primary_purpose', ucs_SATDB.purpose_detailed,
            'object_secondary_purpose', ucs_SATDB.comments,
            'observation_quality', station_status.short_description,
            'object_name',celestrak_SATCAT.name,
            'object_norad_number', Obs.object_number,
            'time_last_tracked',date_format(Obs.last_obs_time, '%M %d, %Y'),
            'username_last_tracked', Obs.last_observer_name,
            'address_last_tracked', Obs.last_observer_eth_addr
          )
          FROM last_observers Obs
          LEFT JOIN ucs_SATDB ON Obs.object_number=ucs_SATDB.norad_number
          LEFT JOIN celestrak_SATCAT ON Obs.object_number = celestrak_SATCAT.norad_num
          LEFT JOIN station_status ON Obs.station_status_code = station_status.code
          ORDER BY user_obs_time DESC;
        """
        queryParams = {
            'ETH_ADDR': eth_addr,
            'OFFSET': offset_row_count,
            'FETCH': fetch_row_count
            }
        # self.c.execute(query_tmp, query_parameters)
        self.c.execute(query, queryParams)
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


    # FIXME: DEPRECATED It doesn't look like this function is used at all in server.py or internally in database.py
    def selectObjectsObserved_JSON(self, fetch_row_count=10, offset_row_count=0):
        """ Return list of (global) observed objects, ordered from most recent
        """
        query_tmp = """SELECT Json_Object(
            'object_origin', ucs_SATDB.country_owner,
            'primary_purpose', ucs_SATDB.purpose,
            'object_type', ucs_SATDB.purpose_detailed,
            'secondary_purpose', 'Secondary purpose does not exist, the variable is also misspelled.',
            'observation_quality', ParsedIOD.station_status_code,
            'time_last_tracked',date_format(ParsedIOD.obs_time, '%M %d, %Y') )
            FROM ParsedIOD
            LEFT JOIN ucs_SATDB ON ParsedIOD.object_number=ucs_SATDB.norad_number
            WHERE valid_position = 1
            ORDER BY obs_time DESC
            LIMIT %(OFFSET)s,%(FETCH)s;"""
        query_parameters = {
                'OFFSET': offset_row_count,
                'FETCH': fetch_row_count}
        self.c.execute(query_tmp, query_parameters)
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)


    # /catalog/priorities
    # https://consensys-cpl.atlassian.net/browse/MVP-323
    def selectCatalog_Priorities_JSON(self, fetch_row_count=100, offset_row_count=0):
        """ Create list of 'Priority'' objects. For now, this just means those that have been tracked least recently.
            Returns all (or fetch_row_count) objects.
            Ordered by the time they were last tracked (least recent first)."""
        quality = 99 # !TODO
        # !TODO: return only objects for which we also know a (TruSat?) TLE, once we have a critical mass of such objects
        # TODO: No priorities in database yet, just sort by reverse obs order for something interesting/different to look at
        # https://consensys-cpl.atlassian.net/browse/MVP-389
        query = (
          self.selectCatalogQueryPrefix +
          "SELECT" + self.selectCatalogJsonObject + """
          FROM catalog
          WHERE datediff(now(),obs_time) >= 30
		  AND datediff(now(),obs_time) <= 365
          ORDER BY obs_time DESC
          LIMIT %(OFFSET)s,%(FETCH)s;""")
        queryParams = {
          'OFFSET': offset_row_count,
          'FETCH': fetch_row_count,
          'QUALITY': quality
          }
        self.c.execute(query, params=queryParams)
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)

    # /catalog/undisclosed
    # https://consensys-cpl.atlassian.net/browse/MVP-324
    def selectCatalog_Undisclosed_JSON(self, fetch_row_count=100, offset_row_count=0):
        """ Create list of Classified objects.
            Returns all (or fetch_row_count) objects that have 'NEA' (no elements available) status in Celestrak.
            Ordered by the time they were last tracked (most recent first)."""
        # !TODO: return only objects for which we also know a (TruSat?) TLE, once we have a critical mass of such objects
        quality = 99 # !TODO
        query = (
          self.selectCatalogQueryPrefix +
          "SELECT" + self.selectCatalogJsonObject + """
          FROM catalog
          WHERE orbit_status_code = 'NEA'
          ORDER BY obs_time DESC
          LIMIT %(OFFSET)s,%(FETCH)s;""")
        queryParams = {
          'OFFSET': offset_row_count,
          'FETCH': fetch_row_count,
          'QUALITY': quality
          }
        self.c.execute(query, params=queryParams)
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)

    # /catalog/debris
    # https://consensys-cpl.atlassian.net/browse/MVP-325
    def selectCatalog_Debris_JSON(self, fetch_row_count=100, offset_row_count=0):
        """ Create list of Debris objects.
            Returns all (or fetch_row_count) objects that have 'DEB' in their object name.
            Ordered by the time they were last tracked (most recent first).
            This heuristic may be too simple and we may miss some debris."""
         # !TODO: return only objects for which we also know a (TruSat?) TLE, once we have a critical mass of such objects
        quality = 99 # !TODO
        query = (
          self.selectCatalogQueryPrefix +
          "SELECT" + self.selectCatalogJsonObject + """
          FROM catalog
          WHERE obj_name LIKE '%DEB%'
          ORDER BY obs_time DESC
          LIMIT %(OFFSET)s,%(FETCH)s;""")
        queryParams = {
          'OFFSET': offset_row_count,
          'FETCH': fetch_row_count,
          'QUALITY': quality
          }
        self.c.execute(query, params=queryParams)
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)

    # /catalog/latest
    # https://consensys-cpl.atlassian.net/browse/MVP-326
    def selectCatalog_Latest_JSON(self, fetch_row_count=100, offset_row_count=0):
        """ Provide a list of the most recently launched objects that have been observed.
            Returns all (or fetch_row_count) objects with a launch date.
            Ordered by launch date, newest first. """
        # !TODO: return only objects for which we also know a (TruSat?) TLE, once we have a critical mass of such objects
        quality = 99 # !TODO
        query = (
          self.selectCatalogQueryPrefix +
          "SELECT" + self.selectCatalogJsonObject + """
          FROM catalog
          WHERE obj_launch_date IS NOT NULL
          ORDER BY obj_launch_date DESC
          LIMIT %(OFFSET)s,%(FETCH)s;""")

        queryParams = {
          'OFFSET': offset_row_count,
          'FETCH': fetch_row_count,
          'QUALITY': quality
          }
        self.c.execute(query, params=queryParams)
        observations = stringArrayToJSONArray_JSON(self.c.fetchall())
        convert_country_names(observations)
        return json.dumps(observations)

    # /catalog/all
    # https://consensys-cpl.atlassian.net/browse/MVP-327
    def selectCatalog_All_JSON(self, fetch_row_count=100, offset_row_count=0):
        """ Return a full list of all observed objects in the DB.
            Returns all (or fetch_row_count) objects that have been observed.
            Ordered by the time they were last tracked (most recent first).
            Should contain only one entry per unique object.
        """
        # !TODO: return only objects for which we also know a (TruSat?) TLE, once we have a critical mass of such objects
        quality = 99 # !TODO
        query = (
          self.selectCatalogQueryPrefix +
          "SELECT" + self.selectCatalogJsonObject + """
          FROM catalog
		  WHERE datediff(now(),obs_time) <= 365
          ORDER BY obs_time DESC
          LIMIT %(OFFSET)s,%(FETCH)s;""")
        queryParams = {
          'OFFSET': offset_row_count,
          'FETCH': fetch_row_count,
          'QUALITY': quality
          }
        self.c.execute(query, params=queryParams)

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

        query = """
            WITH obj_info as (
              WITH latest_obs_times as (SELECT object_number, max(obs_time) max_obs_time, count(distinct(station_number)) user_count
                            FROM ParsedIOD
                            WHERE ParsedIOD.valid_position = 1
                            and object_number = %(NORAD_NUM)s)
                -- There can be multiple obs_ids per {object_number, obs_time}, so we GROUP BY object_number again to ensure only one match
                ,latest_obs_ids as (SELECT P.obs_id, P.object_number, P.obs_time, P.station_number obs_station_number, L.user_count
                            FROM latest_obs_times L
                            LEFT JOIN ParsedIOD P on (L.object_number = P.object_number and L.max_obs_time = P.obs_time)
                            group by object_number)
                -- There can theoretically be multiple users per station, so we GROUP BY object_number again to ensure only one match
                ,latest_obs_with_users as (SELECT L.*, S.user obs_user
                              FROM latest_obs_ids L
                              LEFT JOIN Station S on (S.station_num = L.obs_station_number)
                              group by object_number)
              SELECT
                IODs.*,
                Obs.eth_addr obs_eth_addr, Obs.name obs_user_name,
                    U.comments obj_comments, U.detailed_comments obj_detailed_comments, U.purpose obj_purpose, U.purpose_detailed obj_purpose_detailed, U.country_owner obj_country_owner,
                    SatCat.name obj_name, SatCat.launch_date obj_launch_date, SatCat.orbit_status_code
              FROM latest_obs_with_users as IODs
              LEFT JOIN Observer Obs on (IODs.obs_user = Obs.id)
              LEFT JOIN ucs_SATDB U ON (IODs.object_number = U.norad_number)
              LEFT JOIN celestrak_SATCAT SatCat ON (IODs.object_number = SatCat.sat_cat_id)

            )
            select Json_Object(
              'object_name', obj_name,
              'object_origin', obj_country_owner,
              'object_type', obj_purpose,
              'object_purpose', obj_purpose_detailed,
              'object_secondary_purpose', obj_comments,
              'year_launched', YEAR(obj_launch_date),
              'time_last_tracked', date_format(obs_time, '%M %d, %Y'),
              'number_users_tracked', user_count,
              'time_last_tracked', obs_time,
              'address_last_tracked', obs_eth_addr,
              'username_last_tracked', obs_user_name,
              'observation_quality', %(QUALITY)s,
              'object_background', obj_detailed_comments,
              'heavens_above_url', %(INFO_URL)s
            )
            FROM obj_info;"""

        queryParams = {
          'NORAD_NUM': norad_num,
          'QUALITY': quality,
          'INFO_URL': "https://www.heavens-above.com/SatInfo.aspx?satid={}".format(norad_num)
          }
        self.c.execute(query, queryParams)
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
        # TODO (work in progress): Replace fake data with real data https://consensys-cpl.atlassian.net/browse/MVP-388
        # Remove observation_quality when front-end changes are implemented

        # Note - query variable inconsistency: user_observations IODs insted of Obs
        query = """
          WITH user AS (
            SELECT id user_id, location, name user_name, eth_addr
            FROM Observer
            WHERE eth_addr = %(ETH_ADDR)s
          )
          , user_stations AS (
            SELECT U.*, S.station_num
            FROM user U
            LEFT JOIN Station S on (U.user_id = S.user)
          )
          , user_observations AS (
            SELECT US.*, P.*
            FROM user_stations US
            LEFT JOIN ParsedIOD P on (US.station_num = P.station_number)
            WHERE P.valid_position = 1
            AND P.object_number = %(NORAD_NUM)s
            order by P.obs_time DESC
            LIMIT %(OFFSET)s,%(FETCH)s
          )
          SELECT Json_Object(
            'observation_time', date_format(IODs.obs_time, '%M %d, %Y'),
            'object_origin', celestrak_SATCAT.source,
            'user_location', IODs.location,
            'username', IODs.user_name,
            'user_address', IODs.eth_addr,
            'observation_quality', TLE_process.tle_start_rms,
            'observation_time_difference', TLE_process.time_err,
            'observation_position_error', TLE_process.position_err,
            'observation_cross_track_error', TLE_process.cross_track_err,
            'observation_weight', TLE_process.obs_weight
            )
          FROM user_observations IODs
          LEFT JOIN celestrak_SATCAT ON IODs.object_number = celestrak_SATCAT.norad_num
          LEFT JOIN station_status ON IODs.station_status_code = station_status.code
          LEFT JOIN TLE_process ON IODs.obs_id = TLE_process.obs_id;
        """
        queryParams = {
            'NORAD_NUM': norad_num,
            'ETH_ADDR': eth_addr,
            'OFFSET': offset_row_count,
            'FETCH': fetch_row_count
        }
        self.c.execute(query, queryParams)
        try:
            observations = stringArrayToJSONArray_JSON(self.c.fetchall())
            convert_country_names(observations)
            return observations
        except:
            return None

    # /object/influence
    # https://consensys-cpl.atlassian.net/browse/MVP-380
    def selectObjectInfluence_JSON(self, norad_num, fetch_row_count=100, offset_row_count=0):
        """ For a given NORAD object, return detailed observation information (by all users)
        for the object, with the most recent observations first.

        In the roadmap, this should probably narrow to only the selected (most recent?) TLE
        """
        # TODO (work in progress): Replace fake data with real data https://consensys-cpl.atlassian.net/browse/MVP-388
        # Need to remove observation_quality when John is done with front-end implementation

        # TODO: inadvertantly limits to single station?
        query_tmp = """
        WITH P_influence AS (
            WITH latest_tle_id AS (
                SELECT tle_id from TLE_process TP
                JOIN TLE T ON (TP.tle_result_id = T.tle_id)
                WHERE TP.object_number = %(NORAD_NUM)s
                ORDER by T.epoch DESC LIMIT 2)
            , latest_obs_ids AS (
                SELECT TP2.obs_id tp_obs_id FROM TLE_process TP2, latest_tle_id
                WHERE TP2.tle_result_id = latest_tle_id.tle_id)
            SELECT P1.* FROM ParsedIOD P1, latest_obs_ids
            WHERE P1.obs_id = latest_obs_ids.tp_obs_id
        )
        SELECT Json_Object(
            'observation_time', date_format(obs_time, '%M %d, %Y'),
            'object_origin', celestrak_SATCAT.source,
            'user_location', Obs.location,
            'username', Obs.user_name,
            'observation_quality', TLE_process.tle_start_rms,
            'observation_time_difference', TLE_process.time_err,
            'observation_position_error', TLE_process.position_err,
            'observation_cross_track_error', TLE_process.cross_track_err,
            'observation_weight', TLE_process.obs_weight,
            'user_address', Obs.eth_addr)
            FROM P_influence P
            LEFT JOIN celestrak_SATCAT ON P.object_number = celestrak_SATCAT.sat_cat_id
            JOIN (SELECT
                    Station.station_num as station_num,
                    Station.user as station_user,
                    Observer.id as obs_id,
                    Observer.eth_addr as eth_addr,
                    Observer.name as user_name,
                    Observer.location as location
                    FROM Station,Observer
                    WHERE Station.user = Observer.id)
                    Obs ON P.station_number = Obs.station_num
            LEFT JOIN TLE_process ON P.obs_id = TLE_process.obs_id
            ORDER BY P.obs_time DESC
            LIMIT %(OFFSET)s,%(FETCH)s;"""
        query_parameters = {
            'NORAD_NUM': norad_num,
            'OFFSET': offset_row_count,
            'FETCH': fetch_row_count
        }
        self.c.execute(query_tmp, query_parameters)
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
        query_parameters = {'PARTIAL': partial_string}
        if (type(partial_string) == int):
            query_tmp = """SELECT DISTINCT Json_Object(
                'norad_number', norad_num,
                'name', name)
                FROM celestrak_SATCAT
                WHERE norad_num LIKE %(PARTIAL)s%
                ORDER by norad_num ASC;
                """
        else:
            query_tmp = """SELECT DISTINCT Json_Object(
                'norad_number', norad_num,
                'name', name)
                FROM celestrak_SATCAT
                WHERE name LIKE %(PARTIAL)s%
                ORDER by name ASC;
                """
        print(query_tmp)
        self.c.execute(query_tmp, query_parameters)
        try:
            return stringArrayToJSONArray(self.c.fetchall())
        except:
            return None



    def clean(self):
        self.conn.close()
