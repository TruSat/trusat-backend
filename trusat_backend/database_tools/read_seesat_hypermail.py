import sys

if sys.version_info[0] != 3 or sys.version_info[1] < 6:
	print("This script requires Python version 3.6")
	sys.exit(1)

import os
import re
import argparse
from getpass import getpass
from time import time
from datetime import datetime
from csv import writer 
from dateutil import parser

import logging
log = logging.getLogger(__name__)

# The following 5 lines are necessary until our modules are public
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
iod_path = os.path.join(parentdir, "../trusat-orbit")
sys.path.insert(1,iod_path) 
import iod

sys.path.insert(1,os.path.dirname(currentdir)) 
import database

# Find COSPAR (case insensitive) followed by a space and a 1-4 digit number
#cospar_format_re = re.compile('(?i)\bCOSPAR\b \d{1,4}') # pylint: disable=anomalous-backslash-in-string
cospar_format_re = re.compile('COSPAR \d{1,4}') # pylint: disable=anomalous-backslash-in-string

def find_cospar_mention(line=False):
    match = cospar_format_re.search(line)
    if match:
        return True
    else:
        return False


def get_submit_time_from_filename(filename):
    """ Return python datetime from the filename string produced by seesat_hypermail_process_filenames.py cleanup script """
    file_string = os.path.basename(filename)
    file_string = os.path.splitext(file_string)[0]

    return datetime.strptime(file_string,'%Y%m%d_%H%M%S')
 

if __name__ == '__main__':
    # Read commandline options
    conf_parser = argparse.ArgumentParser(description='Utility to initalize IOD database from email file archive')
    conf_parser.add_argument("-d", "--dir", 
                             help="read from directory DIR [default ./all_emails]",
                             dest='root_dir',
                             default='./all_emails',
                             nargs='?',
                             const=1,                             
                             type=str,                             
                             metavar="FILE")
    conf_parser.add_argument("-q", "--quiet", help="Suppress console output",
                             dest='quiet',
                             action="store_true")
    conf_parser.add_argument("-o", "--userinfo", help="Write out additional info about users",
                             dest='userinfo',
                             action="store_true")
    conf_parser.add_argument("-V", "--verbose", 
                             help="increase verbosity: 0 = only warnings, 1 = info, 2 = debug. No number means info. Default is no verbosity.",
                             const=1, 
                             default=0, 
                             type=int, 
                             nargs="?")

    args = conf_parser.parse_args()
    # Process commandline options and parse configuration
    root_dir = args.root_dir
    verbose = args.verbose
    quiet = args.quiet
    userinfo = args.userinfo
    app_start_time = time()

    # https://stackoverflow.com/questions/14097061/easier-way-to-enable-verbose-logging
    # https://stackoverflow.com/questions/15727420/using-python-logging-in-multiple-modules
    log = logging.getLogger()

    # make it print to the console.
    console = logging.StreamHandler()
    log.addHandler(console)

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

    if (os.path.isdir(root_dir) == False):
        log.warning("Unable to open directory {}. Exiting.".format(root_dir))
        sys.exit()

    # Set up database connection or files
    CONFIG = os.path.abspath("../../trusat-config.yaml")
    db = database.Database(CONFIG)
    if (db._dbtype != "INFILE"):
        try:
            db.createObsTables()
        except:
            log.warning("Tables already exist or there is a big problem buddy.")

    # Initialize variables we want fresh for the processing loop
    existing_users = {} # A rolling list of users that have already had addresses assigned
    TotalCount_IOD = 0
    TotalCount_UK = 0 
    TotalCount_RDE = 0
    TotalObsCount = 0
    FileCount_running = 0
    UserCount_running = 0

    if (userinfo):
        UserDict = []
        COSPAR_Dict = []
        # Set up to write out what we learn about user records for external processing
        UserFile =  open("seesat_hypermail_users.csv", 'w')
        writer_UserFile = writer(UserFile, dialect='unix')

        CosparFile = open("seesat_hypermail_cospar.csv", 'w')
        writer_COSPAR_Dict = writer(CosparFile, dialect='unix')

    # Traverse the directory
    FileCount_total = sum([len(fileList) for dirName, subdirList, fileList in os.walk(root_dir)])
    DirCount_total = sum(os.path.isdir(os.path.join(root_dir, i)) for i in os.listdir(root_dir)) 

    if (quiet == False):
        print("Processing {} files in {}...".format(FileCount_total,root_dir))

    try:
        for dirName, subdirList, fileList in os.walk(root_dir):
            subdirList.sort()
            # Go through individual files from the subdirectories
            dirfileTotal = len(fileList)
            dirfileCount = 0
            for fname in sorted(fileList):
                time_start = time()
                dirfileCount += 1
                FileCount_running += 1
                if(fname == ".DS_Store"):
                    continue

                fileName = os.path.join(dirName, fname)
                with open(fileName) as fp:
                    body = fp.read()

                IOD_records = iod.get_obs_from_text(body)
                IOD_record_counts = iod.get_IOD_record_counts(IOD_records)

                TotalObsCount  += IOD_record_counts["total"]
                TotalCount_IOD += IOD_record_counts["IOD"]
                TotalCount_RDE += IOD_record_counts["RDE"]
                TotalCount_UK  += IOD_record_counts["UK"]


                if (len(IOD_records)):
                    IODpeek = IOD_records[0]
                    log.info("Found {:3} {:3} observations in file ({}/{}): {}".format(len(IOD_records), IODpeek.IODType, FileCount_running, FileCount_total, fileName))
                    # Go back into file to get observer information
                    lines = body.split('\n')

                    # Grab the first line from the list and process the header which applies to all following records
                    line = lines[0]
                    first_line = line.strip()
                    # Parse out the name of the sender
                    find_via = line.find('via Seesat')
                    find_parenthases = line.find('(')
                    find_left_angle_bracket = line.find('<')
                    if find_via > 0:
                        sender = line[6:find_via-1]
                    elif find_parenthases > 0:
                        sender = line[6:find_parenthases-1]
                    elif find_left_angle_bracket > 0:
                        sender = line[6:find_left_angle_bracket-1]
                    else:
                        sender = line[6:]
                    
                    # Remove leading/trailing whitespace, and quotes
                    sender = sender.strip()
                    sender = sender.lstrip('\"')
                    sender = sender.rstrip('\"')

                    # For now, just counting on all the filenames having this
                    # Alternatively, some of the files have it in the second line
                    submit_time = get_submit_time_from_filename(fileName)

                    if (userinfo):
                        for line in lines:
                            if(find_cospar_mention(line)):
                                line = line.strip()
                                if (line not in COSPAR_Dict):
                                    COSPAR_Dict.append(line)
                                    writer_COSPAR_Dict.writerow( [IODpeek.Station, sender, line])

                        if (IODpeek.Station not in UserDict):
                            UserDict.append(IODpeek.Station)
                            writer_UserFile.writerow( [sender, first_line, IODpeek.Station, "hypermail"])
        
                    obsid = db.addParsedIOD(IOD_records, submit_time)

                    if (db._dbtype != "INFILE"):
                        db.commit_IOD_db_writes()
                    time_end = time()
                    delta = (time_end-time_start)
                    log.debug(' File ({}/{}) in dir "{}" contained'.format(dirfileCount,dirfileTotal,dirName))
                    log.debug('                                    ({}/{}) IOD records'.format(IOD_record_counts["IOD"],TotalCount_IOD))
                    log.debug('                                    ({}/{}) UK records'.format(IOD_record_counts["UK"],TotalCount_UK))
                    log.debug('                                    ({}/{}) RDE records'.format(IOD_record_counts["RDE"],TotalCount_RDE))
                    log.debug('                                        of {} records\n'.format(TotalObsCount))
    except KeyboardInterrupt as ex:
        log.warning("Terminated by user.")

    if (quiet == False):
        if DirCount_total:
            dirCount = ("{} directories".format(DirCount_total))
        else:
            dirCount = "1 directory"
    print()
    if (userinfo):
        print("Processed {} observations from {} users in {} files in {} in {:.3f} seconds.".format(TotalObsCount, len(UserDict), FileCount_total, dirCount, time()-app_start_time))
    else:
        print("Processed {} observations in {} files in {} in {:.3f} seconds.".format(TotalObsCount, FileCount_total, dirCount, time()-app_start_time))
    print('                                          ({:6d}) IOD records ({:4.1f} %)'.format(TotalCount_IOD,100*TotalCount_IOD/TotalObsCount))
    print('                                          ({:6d}) UK  records ({:4.1f} %)'.format(TotalCount_UK,100*TotalCount_UK/TotalObsCount))
    print('                                          ({:6d}) RDE records ({:4.1f} %)\n'.format(TotalCount_RDE, 100*TotalCount_RDE/TotalObsCount))
    print()