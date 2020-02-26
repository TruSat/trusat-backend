#!/usr/bin/env python
"""
read_seesat_mbox.py

Parse MBOX-formatted files for IOD/RDE/UK-formatted satellite position observations.

Reference URL: for SeeSat-L archives:  http://mailman.satobs.org/mailman/private/seesat-l/
    Note that while the website says "Gzip'd Text" - the server decodes them, but still keeps the .gz filename
    For reasons of convenient mirroring with wget, leaving that 'wrong' extension in place.

For older hypermail formatted archives (SeeSat-L pre-2014), see read_seesat_hypermail.py

Usage Examples:
===============
    Incremental import example:
    Reprocessing MBOX archive for LOAD INFILE (CSV) import:
    python3 read_seesat_mbox.py -V --dbtype INFILE -f seesat-gzip-emails/MEMBER_ARCHIVE_ALL.txt.gz

    python3 read_seesat_mbox.py -V --fast -f seesat-gzip-emails/2019-08August.txt.gz --dbtype sqlserver --database DBNAME --user USER 

    With defaults from login.txt, resuming from the last-processed msgID
    python3 read_seesat_mbox.py --dbtype sqlserver -V --fast -f seesat-gzip-emails/2019-08August.txt.gz --message CAL65Gdet3=x2jHQSyXOGPN+EQ4LYAoa9zjYReJ+8g8kR7Mj-Ng@mail.gmail.com
"""

import os
import re
import sys 

import argparse
from mailbox import mbox
from email.header import decode_header, make_header
from email.utils import parsedate_to_datetime,parseaddr
from email import message_from_string
from csv import writer 
from datetime import datetime 
from time import time
from getpass import getpass

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


def parse_obfuscated_email(eml):
    """Simple function to re-construct an email in the form of - email at domain.com (Name)"""
    eml = eml.strip()
    find_at = eml.find(' at ')
    find_left_paren = eml.find(' (')
    find_right_paren = eml.find(')')

    email_addr = eml[0:find_at] + "@" + eml[find_at+4:find_left_paren]

    if ((find_left_paren>0) and (find_right_paren>0)):
        email_name = eml[find_left_paren+2:find_right_paren]
        if(email_name.find(' at ')>0):
            email_name = ""

    # At least get the name source of the listserv is hiding email address
    # From: seesat-l at satobs.org (Ted Molczan via Seesat-l)
    if(email_addr.find('seesat-l@satobs.org')>=0):
        # print("Parsed: {}".format(eml))
        email_addr = ""
        find_via = eml.find('via Seesat-l)')
        find_left_paren = eml.find('(')
        find_left_angle_bracket = eml.find('<')
        # Grab the email inside the parenthesis, to the left of find_via, unless it is zero-length
        if (find_left_paren > 0 and find_via > 0 and (find_via>(find_left_paren+1))):
            email_name = eml[find_left_paren+1:find_via]
        # elif find_via > 0:
        #      email_name = eml[6:find_via-1]
        # elif find_left_angle_bracket > 0:
        #      email_name = eml[6:find_left_angle_bracket-1]
        # else:
        #      email_name = eml[6:]
        else:
            email_name = "No Name"

    return(email_addr.lower(), email_name.strip())
               
def getcharsets(msg):
    charsets = set({})
    for c in msg.get_charsets():
        if c is not None:
            charsets.update([c])
    return charsets

def handleerror(errmsg, emailmsg,cs):
    print()
    print(errmsg)
    print("This error occurred while decoding with ",cs," charset.")
    print("These charsets were found in the one email.",getcharsets(emailmsg))
    print("This is the subject:",emailmsg['subject'])
    print("This is the sender:",emailmsg['From'])

# The next three functions from:
# https://stackoverflow.com/questions/7166922/extracting-the-body-of-an-email-from-mbox-file-decoding-it-to-plain-text-regard
def getbodyfromemail(msg):
    body = None
    #Walk through the parts of the email to find the text body.    
    if msg.is_multipart():    
        for part in msg.walk():

            # If part is multipart, walk through the subparts.            
            if part.is_multipart(): 

                for subpart in part.walk():
                        if subpart.get_content_type() == 'text/plain':
                            # Get the subpart payload (i.e the message body)
                            body = subpart.get_payload(decode=True) 
                            #charset = subpart.get_charset()

            # Part isn't multipart so get the email body
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                #charset = part.get_charset()

    # If this isn't a multi-part message then get the payload (i.e the message body)
    elif msg.get_content_type() == 'text/plain':
        body = msg.get_payload(decode=True) 
    # No checking done to match the charset with the correct part. 
    if (getcharsets(msg)):
        for charset in getcharsets(msg):
            try:
                body = body.decode(charset)
                print(charset)
            except UnicodeDecodeError:
                handleerror("UnicodeDecodeError: encountered.",msg,charset)
            except AttributeError:
                handleerror("AttributeError: encountered" ,msg,charset)
        return body    
    else:
        return body.decode("UTF-8")

def main():
    """ Tool to extract user and IOD data from SeeSat-L mailman archives. """
    # Read commandline options
    conf_parser = argparse.ArgumentParser(description='Utility to initalize IOD database from email file archive')
    conf_parser.add_argument("-i", "--init", help="Initialize database datables (IF NOT EXIST)",
                            dest='init',
                            action="store_true")
    conf_parser.add_argument("--fast", help="Fast import. Skip rest of record if duplicate is found.",
                            dest='fast',
                            action="store_true")
    conf_parser.add_argument("-f", "--file", 
                            help="read from directory FILE [default ./all_emails]",
                            dest='mbox_filename',
                            default='/Users/chris/Dropbox/code/MVP/seesat-gzip-emails/MEMBER_ARCHIVE_ALL.txt.gz',
                            nargs='?',
                            const=1,                             
                            type=str,                             
                            metavar="FILE")
    conf_parser.add_argument("-m", "--message", 
                            help="Message ID to start at",
                            dest='message_resume',
                            nargs='?',
                            type=str,                             
                            metavar="MsgID")
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
    mbox_filename = args.mbox_filename
    fast = args.fast
    init = args.init
    message_resume = args.message_resume
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

    # Set up database connection or files
    CONFIG = os.path.abspath("../../trusat-config.yaml")
    db = database.Database(CONFIG)
    if (db._dbtype != "INFILE" and init):
        try:
            db.createObsTables()
        except:
            log.warning("Tables already exist or there is a big problem buddy.")

    TotalCount_IOD = 0
    TotalCount_UK  = 0
    TotalCount_RDE = 0
    TotalObsCount  = 0
    MessageCount_running = 0

    if (userinfo):
        UserDict = []
        COSPAR_Dict = []

        # Set up to write out what we learn about user records for external processing
        UserFile =  open("seesat_mbox_users.csv", 'w')
        writer_UserFile = writer(UserFile, dialect='unix')

        # Set up to write out what we learn about user records for external processing
        CosparFile = open("seesat_mbox_cospar.csv", 'w')
        writer_COSPAR_Dict = writer(CosparFile, dialect='unix')

    last_msgID = None
    for message in mbox(mbox_filename):
        MessageCount_running += 1
        # https://stackoverflow.com/questions/7331351/python-email-header-decoding-utf-8
        try:
            (email_address, name) = parse_obfuscated_email(message['From'])
        except:
            print("Could not parse email in string: '{}'".format(message['From']))
    
        email_address = str(make_header(decode_header(email_address)))
        name = str(make_header(decode_header(name)))

        try:
            date = str(parsedate_to_datetime(message['Date']))
        except:
            print("Could not parse date in string: '{}'".format(message['Date']))
            date = None

        try:
            subject = str(make_header(decode_header(message['subject'])))       # Could possibly be None.
        except:
            print("Could not parse subject in string: '{}'".format(message['subject']))
            subject = None
    
        msgID = parseaddr(message['Message-ID'])[1]

        # If set, read up to, and skip past the specified message ID before processing
        if (message_resume):
            if (message_resume in msgID):
                log.info("Resuming after message {}".format(message_resume))
                message_resume = False
                continue          
            else:
                continue
        body = getbodyfromemail(message)

        IOD_records = iod.get_obs_from_text(body)
        IOD_record_counts = iod.get_IOD_record_counts(IOD_records)

        TotalObsCount  += IOD_record_counts["total"]
        TotalCount_IOD += IOD_record_counts["IOD"]
        TotalCount_RDE += IOD_record_counts["RDE"]
        TotalCount_UK  += IOD_record_counts["UK"]

        if (len(IOD_records)):
            IODpeek = IOD_records[0]
            log.info("Found {:3d} {:3s} obs: {} {}".format(IOD_record_counts["total"], IODpeek.IODType,date,subject))
            
            try:
                date_parsed = datetime.strptime(date,"%Y-%m-%d %H:%M:%S%z")
            except ValueError:
                try:
                    date_parsed = datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
                except ValueError:
                    # FIXME: For some reason on Ubuntu, parsedate_to_datetime started returning ":" in the middle of the tz string
                    # ValueError: time data '2019-10-12 10:21:35+00:00' does not match format '%Y-%m-%d %H:%M:%S%z'
                    date = re.sub('([+-])(\d\d):(\d\d)',r'\1\2\3',date)
                    date_parsed = datetime.strptime(date,"%Y-%m-%d %H:%M:%S%z")

            if date_parsed.utcoffset():
                date_parsed = date_parsed - date_parsed.utcoffset()
                date_parsed = date_parsed.replace(tzinfo=None)
            submit_time = date_parsed.strftime('%Y-%m-%d %H:%M:%S')

            if (userinfo):
                for line in body.split('\n'):
                        if(find_cospar_mention(line)):
                            line = line.strip()
                            if (line not in COSPAR_Dict):
                                COSPAR_Dict.append(line)
                                writer_COSPAR_Dict.writerow( [IODpeek.Station, email_address, line])

                if (IODpeek.Station not in UserDict):
                        UserDict.append(IODpeek.Station)
                        writer_UserFile.writerow( [email_address, name, IODpeek.Station, "mbox"])
        
            db_obs_count = db.addParsedIOD(IOD_records, submit_time, fast)

            if (db_obs_count):
                last_msgID = msgID
                if(db._dbtype != "INFILE"):
                    db.commit_IOD_db_writes()

    print()
    if (userinfo):
        print("Processed {} observations from {} users in {} messages in {:.3f} seconds.".format(TotalObsCount, len(UserDict), MessageCount_running, time()-app_start_time))
    else:
        print("Processed {} observations in {} messages in {:.3f} seconds.".format(TotalObsCount, MessageCount_running, time()-app_start_time))
    if (TotalObsCount > 0):
        print('                                          ({:6d}) IOD records ({:4.1f} %)'.format(TotalCount_IOD,100*TotalCount_IOD/TotalObsCount))
        print('                                          ({:6d}) UK  records ({:4.1f} %)'.format(TotalCount_UK,100*TotalCount_UK/TotalObsCount))
        print('                                          ({:6d}) RDE records ({:4.1f} %)\n'.format(TotalCount_RDE, 100*TotalCount_RDE/TotalObsCount))

    if (last_msgID is not None):
        log.info("Last messageID imported from: {}\n".format(last_msgID))

if __name__ == '__main__':
    main()