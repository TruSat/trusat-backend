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

import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(1,os.path.dirname(currentdir)) 
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

    try:
        CONFIG = os.path.abspath("../../trusat-config.yaml")
        db = database.Database(CONFIG)
    except: 
        log.error("DB Login credentials not available.")


    # Initialize variables we want fresh for the processing loop

    # obsid = db.addParsedIOD(IOD_records, sender, submit_time)

    # sender_id = db.addObserver(acct.address, sender, 0, first_line)
    # log.debug("Creating account {} for Sender (ID) {} ({})".format(acct.address,sender,sender_id))

    query_tmp = "select id from Observer where eth_addr is NULL" 
    query_tmp = "select id from Observer" 
    db.c.execute(query_tmp)
    for [id] in db.c.fetchall():
        acct = Account.create('password123')
        username = database.generateUsername()
        print("ID: {}  eth_addr: {}  username: {}".format(id,acct.address,username))

        # query_tmp2 = "update Observer set eth_addr='{}' where id={}".format(acct.address,id)

        query_tmp2 = "update Observer set name='{}' where id={}".format(username,id)
        db.c.execute(query_tmp2)


    # if (db._dbtype != "INFILE"):
    #     db.commit_IOD_db_writes()