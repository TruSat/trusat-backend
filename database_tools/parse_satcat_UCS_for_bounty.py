#!/usr/bin/env python
# Template code for start of bounty - extracted from other source, and has not been tested in this form

from hashlib import md5
import logging
log = logging.getLogger(__name__)


def fingerprint_file(file):
    """Open, read file and calculate MD5 on its contents"""
    with open(file,'rb') as fd:
        # read contents of the file
        _file_data = fd.read()    
        # pipe contents of the file through
        file_fingerprint = md5(_file_data).hexdigest()
    return file_fingerprint


def fingerprint_line(line):
    """ Creates a unique signature from a line."""
    return md5(line.encode('utf-8')).hexdigest()


class Database:
    def __init__(self, dbname,dbtype,dbhostname,dbusername,dbpassword):
        self._dbname     = dbname
        self._dbtype     = dbtype
        self._dbhostname = dbhostname
        self._dbusername = dbusername
        self._dbpassword = dbpassword
        self.charset_string = "CHARSET=utf8 ENGINE=Aria;"
        self.increment = " AUTO_INCREMENT"

        self.conn = mariadb.connect(
            host=self._dbhostname,
            user=self._dbusername,
            passwd=self._dbpassword,
            db=self._dbname,
            charset='utf8',
            use_unicode=True
            )
        self.c = self.conn.cursor()

        self.c_addSATCAT_query = self.conn.cursor(prepared=True)
        self.c_addUCSDB_query = self.conn.cursor(prepared=True)

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


    def addSATCATentry(self, newentryTuple):
        """ Add an SATCAT entry to the database """
        self._satcatid = 0 # Set this as a variable in case we want to generate our own in the future

        try:
            self.c_addSATCAT_query.execute(self.addSATCAT_query, newentryTuple)
        except Exception as e:
            log.error("MYSQL ERROR: {}".format(e))
        return True


    def addUCSDBentry(self, newentryTuple):
        """ Add an UCS DB entry to the database """
        self._satcatid = 0 # Set this as a variable in case we want to generate our own in the future

        try:
            self.c_addUCSDB_query.execute(self.addUCSDB_query, newentryTuple)
        except Exception as e:
            log.error("MYSQL ERROR: {}".format(e))
        return True

    def fixUCSDB_from_SATCAT(self):
        """ TODO """
        pass


    def update_SATCAT(self):
        """ TODO """
        pass


    def update_UCSDB(self):
        """ TODO """
        pass


def populate_SATCATtable():
    # Set up database connection
    db = Database(dbname,dbtype,dbhostname,dbusername,dbpassword)
    db.createSATCATtable()


    satcat_file_fingerprint = fingerprint_file('data/satcat.txt')
    with open('data/satcat.txt') as file:
        entry_batch = 0 
        for line in (file):
            entry_batch += 1
            intl_desg = line[0:11].strip()
            norad_number = int(line[13:18].strip())

            multiple_name_flag = line[19].strip()
            if not multiple_name_flag:
                multiple_name_flag = 0
            else:
                multiple_name_flag = 1

            payload_flag = line[20].strip()
            if not payload_flag:
                payload_flag = 0
            else:
                payload_flag = 1

            ops_status_code = line[21].strip()
            name = line[23:47].strip()
            source = line[49:54].strip()
            launch_date = line[56:66].strip()

            decay_date = line[75:85].strip()
            if not decay_date:
                decay_date = '0000-00-00'

            try:
                orbit_period_minutes = float(line[87:94].strip())
            except ValueError:
                orbit_period_minutes = -1

            try:
                inclination_deg = float(line[96:101])
            except ValueError:
                inclination_deg = -1

            try:
                apogee = int(line[103:109])
            except ValueError:
                apogee = -1

            try:
                perigee = int(line[111:117])
            except ValueError:
                perigee = -1

            try:
                radar_crosssec = float(line[119:127])
            except ValueError:
                radar_crosssec = -1

            orbit_status_code = line[129:132].strip()

            record_fingerprint = fingerprint_line(line)

            satcat_tuple = (intl_desg, norad_number, multiple_name_flag, payload_flag, ops_status_code,
                            name, source, launch_date, decay_date, orbit_period_minutes, inclination_deg,
                            apogee, perigee, radar_crosssec, orbit_status_code, 
                            satcat_file_fingerprint, record_fingerprint)

            satcatid = db.addSATCATentry(satcat_tuple)
            print(satcat_tuple)
            if(entry_batch>100):
                db.conn.commit()
                entry_batch=0
    db.conn.commit()


def populate_UCSSATDBtable():
    # Set up database connection
    db = Database(dbname,dbtype,dbhostname,dbusername,dbpassword)
    db.createUCSSATDBtable()

    file_to_import = 'data/UCS_Satellite_Database_4-1-2019.txt'

    ucsdb_file_fingerprint = fingerprint_file(file_to_import)
    # FIXME: There still appear to be some character encoding issues around "Earth's geomagnetic field"
    with open(file_to_import, 'r', encoding='latin-1') as file: # FIXME: Doesn't work with UTF-8 type on import (it should)
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
                db.conn.commit()
                entry_batch=0
    db.conn.commit()