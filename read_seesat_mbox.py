#!/usr/bin/env python

# Consider https://github.com/maxlath/fix-utf8

import os
from mailbox import mbox
from email.header import decode_header, make_header
from email.utils import parsedate_to_datetime,parseaddr
from email import message_from_string

import logging
log = logging.getLogger(__name__)

import iod
import database

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
     """ Tool to extract user and IOD data from SeeSat mailman archives. """

     dir = '/Users/chris/Dropbox/code/preMVP/seesat-gzip-emails/'
     file = '2019-June.txt.gz'
     file = 'MEMBER_ARCHIVE_ALL.txt.gz'

     FileIODCount = 0
     FileUKCount = 0 
     FileRDECount = 0
     TotalCount_IOD = 0
     TotalCount_UK = 0
     TotalCount_RDE = 0
     message_RDE_count = 0
     UserDict = []
     TotalObsCount = 0
     dbtype = "INFILE"

     db = database.Database("opensatcat_dev",dbtype,"","","")

     filename = os.path.join(dir, file)
     for message in mbox(filename):
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
               
               submit_time = date

               if (email_address not in UserDict):
                    UserDict.append(email_address)
          
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