#!/usr/bin/env python
from hashlib import md5
import os
import sys

# The following 4 lines are necessary until our modules are public
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(1,os.path.dirname(currentdir)) 
import database

from io import StringIO
import pandas as pd
import requests

from datetime import datetime

import logging
log = logging.getLogger(__name__)

CONFIG = os.path.abspath("../../trusat-config.yaml")

# Use this as our browser, to get past UCS 403 errors
http_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def fingerprint_line(line):
    """ Creates a unique signature from a line."""
    return md5(line.encode("utf-8")).hexdigest()


def load_ucs_satdb_data():
    log.info("Fetching UCSATDB data and loading into memory...")
#    satdb_url = "https://s3.amazonaws.com/ucs-documents/nuclear-weapons/sat-database/5-9-19-update/UCS_Satellite_Database_4-1-2019.txt"
    satdb_url = "https://www.ucsusa.org/sites/default/files/2019-12/UCS-Satellite-Database-10-1-19.txt"

    # https://datascience.stackexchange.com/questions/49751/read-csv-file-directly-from-url-how-to-fix-a-403-forbidden-error
    s=requests.get(satdb_url, headers= http_headers).text
    satdb=pd.read_csv(StringIO(s), sep=";", delimiter="\t", encoding="Windows-1252")

#    satdb = pd.read_csv(satdb_url, delimiter="\t", encoding="Windows-1252")
    satdb = satdb.iloc[:, :35]
    satdb.applymap(format)
    satdb.columns = [
        "name",
        "country_registered",
        "country_owner",
        "owner_operator",
        "users",
        "purpose",
        "purpose_detailed",
        "orbit_class",
        "orbit_type",
        "GEO_longitude",
        "perigee_km",
        "apogee_km",
        "eccentricity",
        "inclination_degrees",
        "period_minutes",
        "launch_mass_kg",
        "dry_mass_kg",
        "power_watts",
        "launch_date",
        "expected_lifetime_years",
        "contractor",
        "contractor_country",
        "launch_site",
        "launch_vehicle",
        "international_designator",
        "norad_number",
        "comments",
        "detailed_comments",
        "source_1",
        "source_2",
        "source_3",
        "source_4",
        "source_5",
        "source_6",
        "source_7",
    ]
    return satdb


def load_celestrak_satcat_data():
    log.info("Fetching CELESTRAK SATCAT data and loading into memory...")
    satcat_url = "https://www.celestrak.com/pub/satcat.txt"
    satcat = pd.read_csv(
        satcat_url, engine="python", delimiter=r"\n", encoding="Windows-1252"
    )
    data = []
    for row in satcat.itertuples(index=False, name=None):
        row = [format(q) for q in parse_celestrak_row(row[0])]
        data.append(row)

    df = pd.DataFrame(
        data,
        columns=[
            "intl_desg",
            "norad_num",
            "multiple_name_flag",
            "payload_flag",
            "ops_status_code",
            "name",
            "source",
            "launch_date",
            "launch_site",
            "decay_date",
            "orbit_period_minutes",
            "inclination_deg",
            "apogee",
            "perigee",
            "radar_crosssec",
            "orbit_status_code",
        ],
    )
    df.set_index("norad_num")
    return df


def fix_discrepencies(satdb, satcat):
    log.info("Fixing discrepencies in the UCS data...")
    # discrepencies_url = "http://celestrak.com/pub/UCS-SD-Discrepancies.txt"
    for i, satdb_row in satdb.iterrows():
        norad_number = format(satdb_row.loc["norad_number"])
        try:
            satcat_row = satcat.loc[norad_number]
            satdb.loc[i, "name"] = satcat_row.loc["name"]
            satdb.loc[i, "perigee_km"] = satcat_row.loc["perigee"]
            satdb.loc[i, "apogee_km"] = satcat_row.loc["apogee"]
            satdb.loc[i, "inclination_degrees"] = satcat_row.loc["inclination_deg"]
            satdb.loc[i, "period_minutes"] = satcat_row.loc["orbit_period_minutes"]
            satdb.loc[i, "launch_date"] = satcat_row.loc["launch_date"]
            satdb.loc[i, "launch_site"] = satcat_row.loc["launch_site"]
            satdb.loc[i, "international_designator"] = satcat_row.loc["intl_desg"]

            import random

            if random.randint(1, 101) < 3:
                satdb.loc[i, "name"] = "BLAH BLAH BLAH"

        except (KeyError, ValueError):
            log.warning(
                f"""Satellite with norad number {norad_number} in satdb is not found in the Celestrak Catalog.
                    Relying on SatDB data only."""
            )

    return satdb


def format(val):
    if pd.isna(val):
        return None

    if type(val).__module__ == "numpy":
        val = val.item()

    if type(val) is int or type(val) is float:
        return val

    val = val.strip()

    try:
        return int(val.replace(",", ""))
    except:
        pass

    try:
        return float(val.replace(",", ""))
    except:
        pass

    try:
        return datetime.strptime(val, "%m/%d/%y").date()
    except:
        pass

    try:
        return datetime.strptime(val, "%m/%d/%Y").date()
    except:
        pass

    try:
        return datetime.strptime(val, "%Y/%m/%d").date()
    except:
        pass

    if not val or val == "N/A":
        return None

    return val


def update_ucs_satdb_raw_table(Database, df):
    log.info("Updating the ucs_satdb_raw table...")

    total_rows = 0
    data_batch = []
    for row in df.itertuples(index=False, name=None):
        record_fingerprint = fingerprint_line("".join(str(e) for e in row))
        savable = [format(i) for i in row] + [record_fingerprint]

        data_batch.append(savable)
        total_rows = total_rows + 1

    if len(data_batch) > 0:
        db.add_ucs_satdb_raw_batch(data_batch)


def update_ucs_satdb_table(Database, df):
    log.info("Updating the (corrected) ucs_satdb table...")

    total_rows = 0
    data_batch = []
    for row in df.itertuples(index=False, name=None):
        record_fingerprint = fingerprint_line("".join(str(e) for e in row))
        savable = [format(i) for i in row] + [record_fingerprint]

        data_batch.append(savable)
        total_rows = total_rows + 1

    if len(data_batch) > 0:
        db.add_ucs_satdb_batch(data_batch)


def parse_celestrak_row(line):
    intl_desg = line[0:11]
    norad_number = line[13:18]

    multiple_name_flag = line[19]
    if not multiple_name_flag:
        multiple_name_flag = 0
    else:
        multiple_name_flag = 1

    payload_flag = line[20]
    if not payload_flag:
        payload_flag = 0
    else:
        payload_flag = 1

    ops_status_code = line[21]
    name = line[23:47]
    source = line[49:54]
    launch_date = line[56:66]
    launch_site = line[69:73]
    decay_date = line[75:85]
    orbit_period_minutes = line[87:94]
    inclination_deg = line[96:101]
    apogee = line[103:109]
    perigee = line[111:117]
    radar_crosssec = line[119:127]
    orbit_status_code = line[129:132]

    satcat_tuple = (
        intl_desg,
        norad_number,
        multiple_name_flag,
        payload_flag,
        ops_status_code,
        name,
        source,
        launch_date,
        launch_site,
        decay_date,
        orbit_period_minutes,
        inclination_deg,
        apogee,
        perigee,
        radar_crosssec,
        orbit_status_code,
    )
    return satcat_tuple


def update_celestrak_satcat_table(Database, df):
    log.info("Updating the celestrak_satcat table...")

    data_batch = []
    for row in df.itertuples(index=False, name=None):
        record_fingerprint = fingerprint_line("".join(str(e) for e in row))
        savable = [format(i) for i in row] + [record_fingerprint]

        data_batch.append(savable)

    if len(data_batch) > 0:
        db.add_celestrak_satcat_batch(data_batch)

# make it print to the console.
console = logging.StreamHandler()
log.addHandler(console)
log.setLevel(logging.DEBUG)

db = database.Database(CONFIG)
db.create_celestrak_satcat_table()
db.create_ucs_satdb_raw_table()
db.create_ucs_satdb_table()

satdb = load_ucs_satdb_data()
satcat = load_celestrak_satcat_data()

update_ucs_satdb_raw_table(db, satdb)
update_celestrak_satcat_table(db, satcat)

satdb = fix_discrepencies(satdb, satcat)

update_ucs_satdb_table(db, satdb)

log.info("Script Complete")
sys.exit(0)