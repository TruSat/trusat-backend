#!/usr/bin/env python
import sys

if sys.version_info[0] != 3 or sys.version_info[1] < 6:
    print("This script requires Python version 3.6")
    sys.exit(1)

from time import time                               # For performance timing

import configparser                 # config file parsing
import argparse                     # command line parsing

import database

# The following 5 lines are necessary until our modules are public
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
database_path = os.path.join(parentdir, "trusat-tle")
sys.path.insert(1,database_path) 
import tle_util


# Main
def main():
    t0 = time()
    # Read commandline options
    conf_parser = argparse.ArgumentParser(description='Collection of utilities' +
                                                      ' to manage TLEs')
    conf_parser.add_argument("-c", "--conf_file",
                             help="Specify configuration file. [Default configuration.ini]",
                             dest='conf_file',
                             nargs='?',
                             const=1,
                             default='configuration.ini',
                             type=str,
                             metavar="FILE")
    conf_parser.add_argument("-f", "--tle",
                             help="Specify TLE file. [Default bulk.tle]",
                             dest='tle_file',
                             nargs='?',
                             type=str,
                             metavar="FILE")
    conf_parser.add_argument("--tlepath",
                             help="Specify TLE path. [Default ./tle]",
                             dest='tle_path',
                             nargs='?',
                             type=str,
                             metavar="PATH")
    conf_parser.add_argument("--update", help="update TLEs from online sources",
                             action="store_true")
    conf_parser.add_argument("-dbname", "--database", 
                             help="database to USE",
                             dest='dbname',
                             default='opensatcat_dev',                           
                             nargs='?',
                             const=1,                             
                             type=str,                             
                             metavar="NAME")
    conf_parser.add_argument("-H", "--hostname", 
                             help="database hostname",
                             dest='dbhostname',
                             default='db.consensys.space',
                             nargs='?',
                             const=1,
                             type=str,                             
                             metavar="HOSTNAME")
    conf_parser.add_argument("-u", "--user", 
                             help="database user name",
                             dest='dbusername',
                             nargs='?',
                             type=str,                             
                             metavar="USER")
    conf_parser.add_argument("-p", "--password", 
                             help="database user password",
                             dest='dbpassword',
                             nargs='?',
                             type=str,                             
                             metavar="PASSWD")
    conf_parser.add_argument("-t", "--dbtype", 
                             help="database type [INFILE, sqlserver, sqlite] \
                                   default: INFILE",
                             dest='dbtype',
                             nargs='?',
                             choices=['INFILE', 'sqlserver', 'sqlite'],
                             default='INFILE',
                             type=str,                             
                             metavar="TYPE")
    conf_parser.add_argument("-i", "--import", help="Import TLEs to database",
                             dest='importTLE',
                             action="store_true")
    conf_parser.add_argument("-q", "--quiet", help="Suppress console output",
                             dest='quiet',
                             action="store_true")
    conf_parser.add_argument("-V", "--verbose", 
                             help="increase verbosity: 0 = only warnings, 1 = info, 2 = debug. No number means info. Default is no verbosity.",
                             const=1, 
                             default=0, 
                             type=int, 
                             nargs="?")

    # Command to upload McCants files from DIR
    # python ./tle_util.py --import --dbtype sqlserver --user chris.lewicki --tlepath /Users/chris/Dropbox/code/MVP/tle/mccants_archive/elsets2019/new -V
    ## With defaults provided from login.txt:
    # python ./tle_util.py --import --tlepath /Users/chris/Dropbox/code/MVP/tle/mccants_archive/elsets2019/new -V

    # Process commandline options and parse configuration
    cfg = configparser.ConfigParser(inline_comment_prefixes=('#', ';'))
    args = conf_parser.parse_args()
    log = logging.getLogger()

    # make it print to the console.
    console = logging.StreamHandler()
    log.addHandler(console)

    conf_file = args.conf_file
    tle_file = args.tle_file
    tle_path = args.tle_path
    update = args.update
    dbname = args.dbname
    dbhostname = args.dbhostname
    dbusername = args.dbusername
    dbpassword = args.dbpassword
    dbtype = args.dbtype
    importTLE = args.importTLE
    verbose = args.verbose
    quiet = args.quiet

    if (quiet == False):
        if verbose == 0:
            log.setLevel(logging.WARN) 
        elif verbose == 1:
            log.setLevel(logging.INFO) 
        elif verbose == 2:
            log.setLevel(logging.DEBUG) 
        log.debug("Log level set to {}".format(log.level))

    if verbose:
        for arg in vars(args):
            log.debug("%s : %s",arg, getattr(args, arg))

    cfg.read([args.conf_file])
    log.info("Reading config from: {}".format(args.conf_file))

    if not (tle_path):
        try:
            tle_path = cfg.get('Common', 'tle_path')
        except KeyError:
            tle_path = "./"

    if not (tle_file):
        tle_file = os.path.join(tle_path,"bulk.tle")
    else:
        tle_file = os.path.join(tle_path,tle_file)


    if update:
        update_from_online(tle_path)

    if (importTLE):
        # Temporary database credentials hack
        try:
            with open('../login.txt', 'r') as f:
                lines = f.readlines()
                dbname = lines[0].strip()
                dbtype = lines[1].strip()
                dbhostname = lines[2].strip()
                dbusername = lines[3].strip()
                dbpassword = lines[4].strip()
        except: 
            log.error("DB Login credentials not available.")

        if (dbtype == "sqlserver"):
            if dbusername == None:
                try: 
                    dbusername = input("Username: ") 
                except Exception as error: 
                    log.warning("ERROR: password must be specified {}".format(error)) 
            if dbpassword == None:
                try: 
                    dbpassword = getpass() 
                except Exception as error: 
                    log.warning("ERROR: password must be specified {}".format(error))

        # Set up database connection or files
        db = database.Database(dbname,dbtype,dbhostname,dbusername,dbpassword)
        # TODO: Probably need an error check to ensure this was set up correctly
        if (dbtype != "INFILE"):
            try:
                db.createTLETables()
            except:
                log.warning("Tables already exist or there is a big problem buddy.")

    # Main processing loop
    t1 = time()
    log.debug(t1-t0)

    # Initialize variables we want fresh for the processing loop
    existing_files = {} # A rolling list of users that have already had addresses assigned
    TLETotalCount = 0
    runningFileCount = 0
    runningUserCount = 0

    # Traverse the directory
    # FIXME: Make this deal gracefully with a non-existent directory
    totalFileCount = sum([len(fileList) for dirName, subdirList, fileList in os.walk(tle_path)])
    totalDirCount = sum(os.path.isdir(os.path.join(tle_path, i)) for i in os.listdir(tle_path)) 

    if (quiet == False):
        print("Processing {} files in {}...".format(totalFileCount,tle_path))

    for dirName, subdirList, fileList in os.walk(tle_path):
        subdirList.sort()
        # Go through individual files from the subdirectories
        dirfileTotal = len(fileList)
        dirfileCount = 0
        for fname in sorted(fileList):
            time_start = time()
            dirfileCount += 1
            if("DS_Store" in fname):
                continue
            _file = os.path.join(dirName,fname)
            log.info("\nReading TLEs from {}".format(_file))
            TLEs = TLEFile(_file)

            # In theory, we could md5 the file directly *before* reading the TLE, but it really doesn't save much.
            # And we'd still want to check in the class, so we'd be doubling-up the MD5 checks.
            tle_file_fingerprint_array = db.selectTLEFile(TLEs.file_fingerprint)

            if(tle_file_fingerprint_array):     
                log.warning("Skipping {} TLEs in file: {} - fingerprint {} already in database.".format(len(TLEs.Satellites), fname, TLEs.file_fingerprint))   
                continue # Already have the file
            else:
                print("Processing file {}...".format(fname))
                for sat_num in TLEs.Satellites:
                    Sat = TLEs.Satellites[sat_num]

                    tle_fingerprint_array = db.selectTLEFingerprint(Sat.tle_fingerprint)
                    if(tle_fingerprint_array):     
                        log.warning("Skipping TLE in file: {} for sat {} - fingerprint {} already in database.".format(fname, sat_num, Sat.tle_fingerprint))   
                        continue # Already have the TLE
                    else:
                        db.addTLE(Sat)

                TLETotalCount += len(TLEs.Satellites)

                # Make note of file if it contained valid TLEs
                if (len(TLEs.Satellites) > 0):
                    result = db.addTLEFile(TLEs)

                # Commit the writes after we're done with the file.
                # We might also want to do this every maximum number of elements (i.e. 1000)    
                db.commit_TLE_db_writes()

            # Check to see if the file is in the DB or local file
            # But defer the database interaction until we have a need to post an observation
            # tle_file_fingerprint_array = db.selectTLEFILE(TLEs.tle_file_fingerprint)

                # if id_array:
                #     sender_id = id_array[0]
                # else:
                #     # Note that this is creating users who may have not submitted an observation
                #     acct = Account.create('password123')
                #     sender_id = db.addObserver(acct.address, sender, 0, first_line)
                #     log.debug("Creating account {} for Sender (ID)".format(acct.address,sender,sender_id))
                #     runningUserCount += 1
                # '''try:
                #     sender_id = existing_users[sender]
                # # If the user is new and does not have
                # except:
                #     acct = Account.create('password123')
                #     existing_users[sender] = acct.address'''
                # log.debug(" Sender (ID): {} ({})".format(sender,sender_id))

                # obsid = db.addParsedIOD(IOD_line, sender_id)
                # log.debug(" {} {} ({}) {}".format(obsid,sender,sender_id, IOD_line.line))

            # for sat_num in TLEs.Satellites:
            #     Sat = TLEs.Satellites[sat_num]

            # log.info("Imported {} TLE records.".format(len(TLEs.Satellites)))
            # log.info("Fingerprint of {} is {}".format(tle_file,TLEs.tle_file_fingerprint))
    if (not quiet):
        print("Imported {} TLEs from {} files in {} directories.".format(TLETotalCount,totalFileCount,totalDirCount))

    t2 = time()
    log.debug(t2-t1)

if (__name__ == '__main__'):
    main()