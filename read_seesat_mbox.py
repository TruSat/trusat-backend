#!/usr/bin/env python

# Consider https://github.com/maxlath/fix-utf8

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

import logging
log = logging.getLogger(__name__)

import database

# The following 5 lines are necessary until our modules are public
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
iod_path = os.path.join(parentdir, "sathunt-iod")
sys.path.insert(1,iod_path) 
import iod

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
     """ Tool to extract user and IOD data from SeeSat mailman archives. 
     
     http://mailman.satobs.org/mailman/private/seesat-l/
     Note that while the website says "Gzip'd Text" - the server decodes them, but still keeps the .gz filename
     For reasons of convenient mirroring with wget, leaving that wrong extension in place.
     """
     # Read commandline options
     conf_parser = argparse.ArgumentParser(description='Utility to initalize IOD database from email file archive')
     conf_parser.add_argument("-f", "--file", 
                              help="read from directory FILE [default ./all_emails]",
                              dest='mbox_filename',
                              default='/Users/chris/Dropbox/code/MVP/seesat-gzip-emails/MEMBER_ARCHIVE_ALL.txt.gz',
                              nargs='?',
                              const=1,                             
                              type=str,                             
                              metavar="FILE")
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
                              default='opensatcat.cvpypmmxjtv1.us-east-2.rds.amazonaws.com',
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
                              help="database type [INFILE, sqlserver, sqlite] default: INFILE",
                              dest='dbtype',
                              nargs='?',
                              choices=['INFILE', 'sqlserver', 'sqlite'],
                              default='INFILE',
                              type=str,                             
                              metavar="TYPE")
     conf_parser.add_argument("-q", "--quiet", help="Suppress console output",
                              dest='quiet',
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
     dbname = args.dbname
     dbhostname = args.dbhostname
     dbusername = args.dbusername
     dbpassword = args.dbpassword
     dbtype = args.dbtype
     verbose = args.verbose
     quiet = args.quiet

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

     if (dbtype == "sqlserver"):
          if dbusername == None:
               try: 
                    dbusername = input("Username: ") 
               except Exception as error: 
                    log.warning('ERROR: password must be specified {}'.format(error))
          if dbpassword == None:
               try: 
                    dbpassword = getpass() 
               except Exception as error: 
                    log.warning('ERROR: password must be specified {}'.format(error))

     # Set up database connection or files
     db = database.Database(dbname,dbtype,dbhostname,dbusername,dbpassword)
     if (dbtype != "INFILE"):
          try:
               db.createObsTables()
          except:
               log.warning("Tables already exist or there is a big problem buddy.")

     FileIODCount = 0
     FileUKCount = 0 
     FileRDECount = 0
     TotalCount_IOD = 0
     TotalCount_UK = 0
     TotalCount_RDE = 0
     message_RDE_count = 0
     UserDict = []
     COSPAR_Dict = []
     TotalObsCount = 0

     db = database.Database(dbname,dbtype,dbhostname,dbusername,dbpassword)

     # Set up to write out what we learn about user records for external processing
     UserFile =  open("seesat_mbox_users.csv", 'w')
     writer_UserFile = writer(UserFile, dialect='unix')

     # Set up to write out what we learn about user records for external processing
     CosparFile = open("seesat_mbox_cospar.csv", 'w')
     writer_COSPAR_Dict = writer(CosparFile, dialect='unix')
 
     for message in mbox(mbox_filename):
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

          try:
               subject = str(make_header(decode_header(message['subject'])))       # Could possibly be None.
          except:
               print("Could not parse subject in string: '{}'".format(message['subject']))
     
          msgID = parseaddr(message['Message-ID'])[1]

          body = getbodyfromemail(message)

          fileIODCount = 0
          fileUKCount = 0
          fileRDEcount = 0

          # Start with most numerous records, move to least
          # Assume there's only one record type per file
          IOD_records = []
          try:
               IOD_records = iod.get_iod_records(body)
               fileIODCount = len(IOD_records)
               TotalCount_IOD += fileIODCount
               TotalObsCount += fileIODCount
          except:
               pass

          if not (len(IOD_records)):
               try: 
                    IOD_records = iod.get_uk_records(body)
                    fileUKCount = len(IOD_records)
                    TotalCount_UK += fileUKCount
                    TotalObsCount += fileUKCount
               except:
                    pass

          if not (len(IOD_records)):
               try: 
                    IOD_records = iod.get_rde_records(body)
                    fileRDEcount = len(IOD_records)
                    TotalCount_RDE += fileRDEcount
                    TotalObsCount += fileRDEcount
               except:
                    pass

          if (len(IOD_records)):
               IODpeek = IOD_records[0]
               log.info("Found {} {} observations in message".format(len(IOD_records), IODpeek.IODType))
               
               try:
                    date_parsed = datetime.strptime(date,"%Y-%m-%d %H:%M:%S%z")
               except:
                    date_parsed = datetime.strptime(date,"%Y-%m-%d %H:%M:%S")

               if date_parsed.utcoffset():
                    date_parsed = date_parsed - date_parsed.utcoffset()
                    date_parsed = date_parsed.replace(tzinfo=None)
               submit_time = date_parsed.strftime('%Y-%m-%d %H:%M:%S')

               for line in body.split('\n'):
                    if(find_cospar_mention(line)):
                        line = line.strip()
                        if (line not in COSPAR_Dict):
                            COSPAR_Dict.append(line)
                            writer_COSPAR_Dict.writerow( [IODpeek.Station, email_address, line])

               if (IODpeek.Station not in UserDict):
                    UserDict.append(IODpeek.Station)
                    writer_UserFile.writerow( [email_address, name, IODpeek.Station, "mbox"])
          
               obsid = db.addParsedIOD(IOD_records, email_address, submit_time)

               if (dbtype != "INFILE"):
                    db.commit_IOD_db_writes()
#               log.debug(' File ({}/{}) in dir "{}" contained'.format(dirfileCount,dirfileTotal,dirName))
               # log.debug('                                    ({}/{}) IOD records'.format(fileIODCount,TotalCount_IOD))
               # log.debug('                                    ({}/{}) UK records'.format(fileUKCount,TotalCount_UK))
               # log.debug('                                    ({}/{}) RDE records'.format(fileRDEcount,TotalCount_RDE))
               # log.debug('                                        of {} records\n'.format(TotalObsCount))

     # if DirCount_total:
     #      dirCount = ("{} directories".format(DirCount_total))
     # else:
     #      dirCount = "1 directory"

     # print("Processed {} observations from {} users.".format(TotalObsCount, len(UserDict)))
     # print('                                          ({}) IOD records ({:4.2f} %)'.format(TotalCount_IOD,100*TotalCount_IOD/TotalObsCount))
     # print('                                          ({}) UK records ({:4.2f} %)'.format(TotalCount_UK,100*TotalCount_UK/TotalObsCount))
     # print('                                          ({}) RDE records ({:4.2f} %)\n'.format(TotalCount_RDE, 100*TotalCount_RDE/TotalObsCount))
     # print("Elapsed time: {:.3f} seconds.".format(time()-app_start_time))

if __name__ == '__main__':
    main()