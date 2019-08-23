import sys

if sys.version_info[0] != 3 or sys.version_info[1] < 6:
	print("This script requires Python version 3.6")
	sys.exit(1)

import os
import re
import argparse
from getpass import getpass
from eth_account import Account

import logging
log = logging.getLogger(__name__)

import database

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
    root_dir = args.root_dir
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

    # Initialize variables we want fresh for the processing loop

    # obsid = db.addParsedIOD(IOD_records, sender, submit_time)

    # sender_id = db.addObserver(acct.address, sender, 0, first_line)
    # log.debug("Creating account {} for Sender (ID) {} ({})".format(acct.address,sender,sender_id))

    query_tmp = "select id from Observer where eth_addr is NULL" 
    db.c.execute(query_tmp)
    for [id] in db.c.fetchall():
        acct = Account.create('password123')
        print("ID: {}  eth_addr: {} ".format(id,acct.address))

        query_tmp2 = "update Observer set eth_addr='{}' where id={}".format(acct.address,id)
        db.c.execute(query_tmp2)


    # if (dbtype != "INFILE"):
    #     db.commit_IOD_db_writes()