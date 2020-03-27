import os
import sys
import re
import jwt
import sha3
import time
import json
import base64
import numpy
import secrets
import requests
import database
import google_email


from jwt import encode, decode
from eth_account import Account
from eth_account.messages import defunct_hash_message, encode_defunct
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from coinaddr import validate
from datetime import datetime, timedelta
from base64 import urlsafe_b64decode


from flask import Flask, abort, Response, jsonify, after_this_request, session, request, make_response, g, send_from_directory
from flask_cors import CORS
from flask_caching import Cache
from flask_wtf.csrf import CSRFProtect



# ALL ENV VAR:
# - MAILGUN_API_KEY
# - MAILGUN_EMAIL_ADDRESS
# - WEBSITE_ORIGINS
# - SECRET_KEY
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY', False)
MAILGUN_EMAIL_ADDRESS = os.getenv('MAILGUN_EMAIL_ADDRESS', False)
WEBSITE_ORIGINS = os.getenv('WEBSITE_ORIGINS', False)
if WEBSITE_ORIGINS is not False:
    WEBSITE_ORIGINS = WEBSITE_ORIGINS.split(',')
SECRET_KEY = os.getenv('SECRET_KEY', False)
if SECRET_KEY is not False:
    SECRET_KEY = base64.b64decode(bytes(SECRET_KEY, 'utf-8'))
else:
    SECRET_KEY = b'ucCWKF7iqBqLNVoa6dS5Bc+mYYTecgcPg3Uv9nPP043hcdLPaE/UhBqqAChdytGifzeKzFl2bT4aN0B5xqEtEvB4CnkJIorgmnVhlrH3m663Fq7Uish32rH57AIeAtlZGo7L0OhYbNRPKewvlK0YfzUQt/I1Iaf/Duxa7SZ19c3cVgkzC9g4fKrhbE2TUXRnjpdFQY2I30SRwt3RYmRQRO2hSvstpIHtn5k3hFu71aQmS2ILFoyijksWyAC0eh4fgxJPmvfaGfexxiyHgAkv9bdWVzcdNeitld/glGJk7G4NquccJFozPqY3UqMg+ZLJzz36abe3gT5Yv/WAxNZlCQ=='


config = {
    "JSON_SORT_KEYS": False,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "SECRET_KEY": SECRET_KEY
}


app = Flask(__name__, static_folder="trusat-frontend/build/static", template_folder="trusat-frontend/build")
app.config.from_mapping(config)
cache = Cache(app)
if WEBSITE_ORIGINS is not False:
    cors = CORS(app, support_credentials=True, origins=WEBSITE_ORIGINS)
else:
    cors = CORS(app, support_credentials=True)
#csrf = CSRFProtect(app)


with app.app_context():
    # An ordered title and path for al catalogs the backend has implemented
    g.celestrakCategories = { "data": [
        {
        "groupHeader": { "title": "Featured", "path": "featured" },
        "groupCategories": [
            { "title": "100 Brightest", "path": "visual" },
            { "title": "Starlink", "path": "starlink" },
            {
            "title": "OneWeb",
            "path": "one-web"
            },
            {
            "title": "Active Sats",
            "path": "active"
            },
            {
            "title": "Analyst sats",
            "path": "analyst"
            }
        ]
        },
        {
        "groupHeader": {
            "title": "Weather & Earth Resources",
            "path": "weather-earth"
        },
        "groupCategories": [
            { "title": "Weather", "path": "weather" },
            { "title": "NOAA", "path": "noaa" },
            {
            "title": "GOES",
            "path": "goes"
            },
            {
            "title": "Earth Resources",
            "path": "resource"
            },
            {
            "title": "Search & Rescue (SARSAT)",
            "path": "sarsat"
            },
            {
            "title": "Disaster Monitoring",
            "path": "disaster-monitoring"
            },
            {
            "title": "Tracking and Data Relay",
            "path": "tracking-and-data-relay"
            },
            {
            "title": "Tracking and Data Relay Satellite System (TDRSS)",
            "path": "tdrss"
            },
            {
            "title": "ARGOS Data Collection",
            "path": "argos"
            },
            {
            "title": "System",
            "path": "system-weather-and-earth-resources"
            },
            {
            "title": "Planet",
            "path": "planet"
            },
            {
            "title": "Spire",
            "path": "spire"
            }
        ]
        },
        {
        "groupHeader": { "title": "Communications", "path": "communications" },
        "groupCategories": [
            { "title": "Geosynchronous", "path": "geo" },
            { "title": "GEO Protected Zone", "path": "geo-protected-zone" },
            {
            "title": "GEO Protected Zone Plus",
            "path": "geo-protected-zone-plus"
            },
            {
            "title": "Intelsat",
            "path": "intelsat"
            },
            {
            "title": "SES",
            "path": "ses"
            },
            {
            "title": "Iridium",
            "path": "iridium"
            },
            {
            "title": "Iridium Next",
            "path": "iridium-next"
            },
            {
            "title": "Orbcomm",
            "path": "orbcomm"
            },
            {
            "title": "Globalstar",
            "path": "globalstar"
            },
            {
            "title": "Amateur Radio",
            "path": "amateur-radio"
            },
            {
            "title": "Experimental",
            "path": "experimental"
            },
            {
            "title": "Other Comm",
            "path": "other-comm"
            },
            {
            "title": "SatNOGS",
            "path": "satnogs"
            },
            {
            "title": "Gorizant",
            "path": "gorizant"
            },
            {
            "title": "Raduga",
            "path": "raduga"
            },
            {
            "title": "Molniya",
            "path": "molniya"
            }
        ]
        },
        {
        "groupHeader": { "title": "Navigation", "path": "navigation" },
        "groupCategories": [
            { "title": "GPS Operational", "path": "gps-ops" },
            { "title": "GLONASS Operational", "path": "glonass-operational" },
            {
            "title": "Galileo",
            "path": "galileo"
            },
            {
            "title": "Beidou",
            "path": "beidou"
            },
            {
            "title": "Satellite-Based Augmentation",
            "path": "satellite-based-augmentation"
            },
            {
            "title": "System",
            "path": "system-navigation"
            },
            {
            "title": "Satellite-Based Augmentation System (WAAS/EGNOS/MSAS)",
            "path": "sbas"
            },
            {
            "title": "Navy Navigation Satellite Systems (NNSS)",
            "path": "nnss"
            },
            {
            "title": "System (NNSS)",
            "path": "nnss-system"
            },
            {
            "title": "Russian LEO Navigation",
            "path": "musson"
            }
        ]
        },
        {
        "groupHeader": { "title": "Debris", "path": "debris" },
        "groupCategories": [
            { "title": "Indian ASAT Test", "path": "indian-asat-test" },
            { "title": "FENGYUN 1C", "path": "1999-025" },
            {
            "title": "IRIDIUM 33",
            "path": "iridium-33"
            },
            {
            "title": "COSMOS 2251",
            "path": "cosmos-2251"
            },
            {
            "title": "BREEZE-M R/B Breakup (2012-044C)",
            "path": "2012-044"
            }
        ]
        },
        {
        "groupHeader": { "title": "Scientific", "path": "scientific" },
        "groupCategories": [
            { "title": "Space & Earth Science", "path": "science" },
            { "title": "Geodetic", "path": "geodetic" },
            {
            "title": "Engineering",
            "path": "engineering"
            },
            {
            "title": "Education",
            "path": "education"
            }
        ]
        },
        {
        "groupHeader": { "title": "Misc.", "path": "misc" },
        "groupCategories": [
            { "title": "Miscellaneous Military", "path": "military" },
            { "title": "Radar Calibration", "path": "radar-calibration" },
            {
            "title": "CubeSats",
            "path": "cubesat"
            },
            {
            "title": "Last 30 Days' Launches",
            "path": "tle-new"
            },
            {
            "title": "Space Stations",
            "path": "stations"
            },
            {
            "title": "Other",
            "path": "other"
            }
        ]
        },
        {
            "groupHeader": { "title": "All", "path": "all"},
            "groupCategories": []
        }
        ]
        }


#TODO: take object instead of address to encode with a specified time
# Checks for valid inputs
def encode_jwt(addr):
    with open('unsafe_private.pem', 'r') as file:
        private_key = file.read()
    private_rsa_key = load_pem_private_key(bytes(private_key, 'utf-8'), password=None, backend=default_backend())
    exp = datetime.utcnow() + timedelta(days=7)
    encoded_jwt = encode({'address':addr, 'exp':exp}, private_rsa_key, algorithm='RS256')
    return encoded_jwt

def decode_jwt(user_jwt):
    with open('public.pem', 'r') as file:
        public_key = file.read()
    public_rsa_key = load_pem_public_key(bytes(public_key,'utf-8'), backend=default_backend())
    decoded_jwt = decode(user_jwt, public_rsa_key, algorithms='RS256')
    return decoded_jwt

def isValidNoradNumber(value):
    try:
        int_value = int(value)
    except Exception as e:
        print(e)
        return False
    if int_value < 100000 and int_value > 0:
        return True
    else:
        return False

def isValidEthereumAddress(addr):
    check_address = validate('eth', bytes(addr, 'utf-8'))
    return check_address.valid

def isValidEmailAddress(email):
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.search(regex, email)

def isValidSecret(secret):
    regex = r'^([0-9]{1,10})([\/])([0-9, a-f]{32})([\/])([0-9,a-f]{160})$'
    return re.search(regex, secret)

def isValidUserSetting(setting):
    regex = r'^([0-9,a-z,A-Z,\',!,\s,\\,!,@,#,$,%,^,&,*,(,),[,\],{,},+,\-,=,_,|,;,\,,.,/,?]{1,255})$'
    return re.search(regex, setting)


# Error messaging
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response




@app.before_request
def before_request_func():
    # Read config and set up database connection
    CONFIG = os.path.abspath("../trusat-config.yaml")
    g.db = database.Database(CONFIG)


@app.after_request
def after_request_func(response):
    if g.get('db') is not None:
        g.get('db').clean()
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response



def catalog_cache(response):
    response.headers['Cache-Control'] = 'max-age=300'
    return response



@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path != '' and os.path.exists("trusat-frontend/build/" + path):
        return send_from_directory('trusat-frontend/build', path)
    else:
        return send_from_directory("trusat-frontend/build", "index.html")


@app.route('/error', methods=['GET'])
def error_route():
    raise InvalidUsage('This is an expected error', status_code=400)


@app.route('/catalog/list', methods=['GET'])
def catalog_list():
    return g.get('celestrakCategories')


@app.route('/catalog/<catalog>/<int:offset>', methods=['GET'])
def catalog_weather(catalog, offset):
    # All catalogs with the associated query
    all_catalogs = {
        "priorities": g.get('db').selectCatalog_Priorities_JSON,
        "undisclosed": g.get('db').selectCatalog_Undisclosed_JSON,
        "latest": g.get('db').selectCatalog_Latest_JSON,
        "featured": g.get('db').selectCatalog_All_JSON,
        "visual": g.get('db').selectCatalog_All_JSON,
        "starlink": g.get('db').selectCatalog_All_JSON,
        "one-web": g.get('db').selectCatalog_All_JSON,
        "active": g.get('db').selectCatalog_All_JSON,
        "analyst": g.get('db').selectCatalog_All_JSON,
        "weather-earth": g.get('db').selectCatalog_All_JSON,
        "weather": g.get('db').selectCatalog_All_JSON,
        "noaa": g.get('db').selectCatalog_All_JSON,
        "goes": g.get('db').selectCatalog_All_JSON,
        "resource": g.get('db').selectCatalog_All_JSON,
        "sarsat": g.get('db').selectCatalog_All_JSON,
        "disaster-monitoring": g.get('db').selectCatalog_All_JSON,
        "tracking-and-data-relay": g.get('db').selectCatalog_All_JSON,
        "tdrss": g.get('db').selectCatalog_All_JSON,
        "argos": g.get('db').selectCatalog_All_JSON,
        "system-weather-and-earth-resources": g.get('db').selectCatalog_All_JSON,
        "planet": g.get('db').selectCatalog_All_JSON,
        "spire": g.get('db').selectCatalog_All_JSON,
        "communications": g.get('db').selectCatalog_All_JSON,
        "geo": g.get('db').selectCatalog_All_JSON,
        "geo-protected-zone": g.get('db').selectCatalog_All_JSON,
        "geo-protected-zone-plus": g.get('db').selectCatalog_All_JSON,
        "intelsat": g.get('db').selectCatalog_All_JSON,
        "ses": g.get('db').selectCatalog_All_JSON,
        "iridium": g.get('db').selectCatalog_All_JSON,
        "iridium-next": g.get('db').selectCatalog_All_JSON,
        "orbcomm": g.get('db').selectCatalog_All_JSON,
        "globalstar": g.get('db').selectCatalog_All_JSON,
        "amateur-radio": g.get('db').selectCatalog_All_JSON,
        "experimental": g.get('db').selectCatalog_All_JSON,
        "other-comm": g.get('db').selectCatalog_All_JSON,
        "satnogs": g.get('db').selectCatalog_All_JSON,
        "gorizant": g.get('db').selectCatalog_All_JSON,
        "raduga": g.get('db').selectCatalog_All_JSON,
        "molniya": g.get('db').selectCatalog_All_JSON,
        "navigation": g.get('db').selectCatalog_All_JSON,
        "gps-ops": g.get('db').selectCatalog_All_JSON,
        "glonass-operational": g.get('db').selectCatalog_All_JSON,
        "galileo": g.get('db').selectCatalog_All_JSON,
        "beidou": g.get('db').selectCatalog_All_JSON,
        "satellite-based-augmentation": g.get('db').selectCatalog_All_JSON,
        "system-navigation": g.get('db').selectCatalog_All_JSON,
        "sbas": g.get('db').selectCatalog_All_JSON,
        "nnss": g.get('db').selectCatalog_All_JSON,
        "nnss-system": g.get('db').selectCatalog_All_JSON,
        "musson": g.get('db').selectCatalog_All_JSON,
        "debris": g.get('db').selectCatalog_Debris_JSON,
        "indian-asat-test": g.get('db').selectCatalog_All_JSON,
        "1999-025": g.get('db').selectCatalog_All_JSON,
        "iridium-33": g.get('db').selectCatalog_All_JSON,
        "cosmos-2251": g.get('db').selectCatalog_All_JSON,
        "2012-044": g.get('db').selectCatalog_All_JSON,
        "scientific": g.get('db').selectCatalog_All_JSON,
        "science": g.get('db').selectCatalog_All_JSON,
        "geodetic": g.get('db').selectCatalog_All_JSON,
        "engineering": g.get('db').selectCatalog_All_JSON,
        "education": g.get('db').selectCatalog_All_JSON,
        "misc": g.get('db').selectCatalog_All_JSON,
        "military": g.get('db').selectCatalog_All_JSON,
        "radar-calibration": g.get('db').selectCatalog_All_JSON,
        "cubesat": g.get('db').selectCatalog_All_JSON,
        "tle-new": g.get('db').selectCatalog_All_JSON,
        "stations": g.get('db').selectCatalog_All_JSON,
        "other": g.get('db').selectCatalog_All_JSON,
        "all": g.get('db').selectCatalog_All_JSON
    }
    try:
        json_object = all_catalogs[catalog](fetch_row_count=200, offset_row_count=offset)
    except Exception as e:
        print(e)
        raise InvalidUsage('Could not get all', status_code=500)
    if json_object is not False:
        @after_this_request
        def add_header(response):
            return catalog_cache(response)
        return json_object
    else:
        return {}


@app.route('/tle/trusat_all.txt', methods=['GET'])
def catalog_trusat_all_txt():
    try:
        two_line_elements = g.get('db').selectTLE_all()
    except Exception as e:
        print(e)
        raise InvalidUsage('Could not get TLEs', status_code=500)
    if two_line_elements is not False:
        @after_this_request
        def add_header(response):
            return catalog_cache(response)
        return two_line_elements, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    else:
        return ''


@app.route('/tle/trusat_priorities.txt', methods=['GET'])
def catalog_trusat_priorities_txt():
    try:
        two_line_elements = g.get('db').selectTLE_priorities()
    except Exception as e:
        print(e)
        raise InvalidUsage('Could not get TLEs', status_code=500)
    if two_line_elements is not False:
        @after_this_request
        def add_header(response):
            return catalog_cache(response)
        return two_line_elements, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    else:
        return ''


@app.route('/tle/trusat_high_confidence.txt', methods=['GET'])
def catalog_trusat_high_confidence_txt():
    try:
        two_line_elements = g.get('db').selectTLE_high_confidence()
    except Exception as e:
        print(e)
        raise InvalidUsage('Could not get TLEs', status_code=500)
    if two_line_elements is not False:
        @after_this_request
        def add_header(response):
            return catalog_cache(response)
        return two_line_elements, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    else:
        return ''


@app.route('/astriagraph', methods=['GET'])
def catalog_astriagraph():
    try:
        tles_json = g.get('db').selectTLE_Astriagraph()
    except Exception as e:
        print(e)
        raise InvalidUsage('Could not get TLEs', status_code=500)
    if tles_json is not False:
        @after_this_request
        def add_header(response):
            return catalog_cache(response)
        return tles_json
    else:
        return ''


@app.route('/profile', methods=['GET'])
def profile():
    jwt_user_addr = ''
    try:
        user_addr = request.args.get("address")
    except Exception as e:
        print(e)
        raise InvalidUsage('Missing address', status_code=400)
    if isValidEthereumAddress(user_addr) is False:
        raise InvalidUsage('Address is invalid', status_code=400)
    try:
        user_profile_json = g.get('db').selectProfileInfo_JSON(user_addr)
        objects_observed_json = g.get('db').selectUserObjectsObserved_JSON(user_addr)
        observation_history_json = g.get('db').selectUserObservationHistory_JSON(user_addr)
        user_profile_json["objects_observed"] = objects_observed_json
        user_profile_json["observation_history"] = observation_history_json
        user_profile_json["observation_stations"] = []
    except Exception as e:
        print(e)
        raise InvalidUsage('Could not retrieve user information', status_code=500)
    try:
        cookie_jwt = request.cookies.get('jwt')
        if cookie_jwt is None:
            raise InvalidUsage('User is not logged in', status_code=400)
        decoded_jwt = decode_jwt(cookie_jwt)
        jwt_user_addr = decoded_jwt["address"]
    except Exception as e:
        print(e)
    if isValidEthereumAddress(jwt_user_addr) is False:
        raise InvalidUsage('Invalid Ethereum address', status_code=400)
    if jwt_user_addr.lower() == user_addr.lower():
        try:
            observation_station_numbers = g.get('db').selectUserStationNumbers_JSON(user_addr)
            for station in observation_station_numbers["user_stations"]:
                user_profile_json["observation_stations"].append(station)
        except Exception as e:
            print(e)
            raise InvalidUsage('Observation information could not be retrieved', status_code=500)

    for k,v in user_profile_json.items():
        if v == None or v =='NULL':
            user_profile_json[k] = ""

    @after_this_request
    def add_header(response):
        return catalog_cache(response)
    return user_profile_json


@app.route('/object/influence', methods=['GET'])
def object_influence():
    try:
        norad_number = request.args.get('norad_number')
    except Exception as e:
        print(e)
        raise InvalidUsage('Norad number is missing from parameters', status_code=400)
    if isValidNoradNumber(norad_number) is False:
        raise InvalidUsage('Norad number is not valid', status_code=400)
    try:
        json_object = g.get('db').selectObjectInfluence_JSON(norad_number)
    except Exception as e:
        print(e)
        raise InvalidUsage('Object influence could not be retrieved', status_code=500)
    if json_object:
        return json_object
    else:
        return {}


@app.route('/object/info', methods=['GET'])
def object_info():
    try:
        norad_number = request.args.get('norad_number')
    except Exception as e:
        print(e)
        raise InvalidUsage('Norad number is missing from parameters', status_code=400)
    if isValidNoradNumber(norad_number) is False:
        raise InvalidUsage('Norad number is not valid', status_code=400)
    try:
        json_object = g.get('db').selectObjectInfo_JSON(norad_number)
    except Exception as e:
        print(e)
        raise InvalidUsage('Object info could not be retrieved', status_code=500)
    if json_object:
        @after_this_request
        def add_header(response):
            return catalog_cache(response)
        return json_object
    else:
        return {}


@app.route('/object/history', methods=['GET'])
def object_history():
    try:
        norad_number = request.args.get('norad_number')
        year = request.args.get("year")
        int_year = int(year)
    except Exception as e:
        print(e)
        raise InvalidUsage('Missing norad number and/or year', status_code=400)
    if (isValidNoradNumber(norad_number) is False or
        int_year < 1957 or
        int_year > datetime.now().year):
        raise InvalidUsage('Year is out of range or norad number is invalid', status_code=400)
    try:
        real_entry = g.get('db').selectObjectHistoryByMonth_JSON(norad_number, year)
        year_response = {
            "December": [],
            "November": [],
            "October": [],
            "September": [],
            "August": [],
            "July": [],
            "June": [],
            "May": [],
            "April": [],
            "March": [],
            "February": [],
            "January": []
        }
        for items in real_entry:
            timestamp = datetime.fromtimestamp(float(items["observation_time"]))
            month_string = timestamp.strftime("%B")
            date = timestamp.day
            items["observation_date"] = date
            year_response[month_string].append(items)
        @after_this_request
        def add_header(response):
            return catalog_cache(response)
        return year_response
    except Exception as e:
        print(e)
        raise InvalidUsage('Could not get history', status_code=500)


@app.route('/object/userSightings', methods=['GET'])
def object_user_sightings():
    response_body = []
    try:
        norad_number = request.args.get('norad_number')
        cookie_jwt = request.cookies.get('jwt')
        decoded_jwt = decode_jwt(cookie_jwt)
        public_address = decoded_jwt["address"]
    except Exception as e:
        print(e)
        raise InvalidUsage('Parameter(s) missing', status_code=400)
    if (isValidNoradNumber(norad_number) is False or
        isValidEthereumAddress is False):
        raise InvalidUsage('Invalid norad number or Ethereum address', status_code=400)
    try:
        response_body = g.get('db').selectObjectUserSightings_JSON(norad_number, public_address)
        @after_this_request
        def add_header(response):
            return catalog_cache(response)
        return response_body
    except Exception as e:
        print(e)
        raise InvalidUsage('userSighting failed', status_code=500)

@app.route('/tle/object', methods=['GET'])
def tle_object():
    try:
        norad_number = request.args.get("norad_number")
    except Exception as e:
        print(e)
        raise InvalidUsage('Missing Norad number', status_code=400)
    if isValidNoradNumber(norad_number) is False:
        raise InvalidUsage('Invalid Norad number', status_code=400)
    try:
        two_line_elements = g.get('db').selectTLE_single(norad_number)
    except Exception as e:
        print(e)
        raise InvalidUsage('Could not get TLE', status_code=500)
    if two_line_elements:
        @after_this_request
        def add_header(response):
            return catalog_cache(response)
        return two_line_elements
    else:
        return ""


@app.route('/findObject', methods=['GET'])
def find_object():
    try:
        partial_string = request.args.get("objectName")
    except Exception as e:
        print(e)
        raise InvalidUsage('Object name missing', status_code=400)
    try:
        objects = g.get('db').selectFindObject(partial_string)
        @after_this_request
        def add_header(response):
            return catalog_cache(response)
        return objects
    except Exception as e:
        print(e)
        raise InvalidUsage('Could not find object', status_code=500)


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return ('', 204)


@app.route('/errorTest', methods=['GET'])
def error_test():
    raise InvalidUsage('message', status_code=400)

@app.route('/cookieMonster', methods=['GET'])
def cookie_monster():
    @after_this_request
    def add_header(response):
        response.set_cookie('test', 'cookieMonster', max_age=518400, httponly=True, samesite="Strict") #secure=True, httponly=True, samesite="Strict")
        return response
    return {}








### GET NONCE ENDPOINT ###
@app.route('/getNonce', methods=['POST'])
def get_nonce():
    try:
        addr = request.get_json()["address"]
    except Exception as e:
        print(e)
        raise InvalidUsage('Ethereum address missing', status_code=400)
    if isValidEthereumAddress(addr) is False:
        raise InvalidUsage('Invalid Ethereum address', status_code=400)
    try:
        email = request.get_json()["email"]
        if isValidEmailAddress is False:
            raise InvalidUsage('Invalid email address', status_code=400)
        results = g.get('db').selectObserverAddressFromEmail(email)
        if len(results) == 42:
            return {}
    except Exception as e:
        print(e)
    try:
        public_address_count = g.get('db').getObserverCountByID(public_address=addr)
    except Exception as e:
        print(e)
        raise InvalidUsage('message', status_code=500)
    random_number = str(secrets.randbits(256))
    response_message = '{"nonce":\"%s\"}' % random_number
    if public_address_count[0] == None or public_address_count[0] == 0:
        # New User
        try:
            g.get('db').addObserver(addr, "NULL", 0, "NULL")
            g.get('db').updateObserverNonceBytes(nonce=random_number, public_address=addr)
        except Exception as e:
            print(e)
            raise InvalidUsage('message', status_code=500)
    elif public_address_count[0] >= 1:
        # Old User
        try:
            g.get('db').updateObserverNonceBytes(nonce=random_number, public_address=addr)
        except Exception as e:
            print(e)
            raise InvalidUsage('message', status_code=500)
    return response_message


@app.route('/signup', methods=['POST'])
def signup():
    signed_public_key = '0'
    try:
        addr = request.get_json()["address"]
        if isValidEthereumAddress(addr) is False:
            raise InvalidUsage('message', status_code=400)
        old_nonce = g.get('db').getObserverNonceBytes(addr)
        email = request.get_json()["email"]
        signed_message = request.get_json()["signedMessage"]
        payload = request.get_json()["secret"]
    except Exception as e:
        print(e)
        raise InvalidUsage('message', status_code=400)
    try:
        if (isValidEmailAddress(email) is False or
            isValidSecret(payload) is False):
            raise InvalidUsage('message', status_code=400)
        nonce = old_nonce.encode('utf-8')
        g.get('db').updateObserverNonceBytes(nonce='NULL', public_address=addr)
        message_hash = sha3.keccak_256(nonce).hexdigest()
        message_hash = encode_defunct(hexstr=message_hash)
    except Exception as e:
        print(e)
        raise InvalidUsage('message', status_code=500)
    try:
        signed_public_key = Account.recover_message(message_hash, signature=signed_message)
    except Exception as e:
        print(e)
        print('message could not be checked')
    try:
        if signed_public_key.lower() == addr.lower():
            email_from_addr = g.get('db').selectEmailFromObserverAddress(addr)
            if email_from_addr == None or email_from_addr == '' or email_from_addr == b'NULL':
                if email != None or email != 'null' or email != 'NULL' or email != '':
                    try:
                        g.get('db').updateObserverEmail(email, addr)
                        message_text = 'Save this email: TruSat account recovery info for ' + email + '\n\n' + \
                                'To log into TruSat, you\'ll need your password AND this secret code:\n\n' + payload + \
                                '\n\nThis email is the only time we can send you this code. TruSat cannot reset your password for you. Please save this email forever and make a note of the password you used.\n\n' + \
                                'Login here: trusat.org/login\n\n' + \
                                'Why do we do it this way? Read more (trusat.org/faq)\n\n' + \
                                'Questions? Please email: Help@Beta.TruSat.org'
                        data = {"from": "TruSat Help <" + MAILGUN_EMAIL_ADDRESS + ">",
                                "to": [email],
                                "subject": "TruSat - Save this email: Recovery Info",
                                "text": message_text}
                        response = requests.post(
                                "https://api.mailgun.net/v3/beta.trusat.org/messages",
                                auth=("api", MAILGUN_API_KEY),
                                data=data
                            )
                        if response.status_code != 200:
                            print("Email failed to send.")
                            raise InvalidUsage('message', status_code=500)
                        return {'result': True}
                    except Exception as e:
                        print(e)
                        raise InvalidUsage('message', status_code=500)
    except Exception as e:
        print(e)
    else:
        raise InvalidUsage('message', status_code=400)
    raise InvalidUsage('message', status_code=500)


        ### LOGIN ENDPOINT ###
@app.route('/login', methods=['POST'])
def login():
    signed_public_key = '0'
    response_message = b''
    try:
        addr = request.get_json()["address"]
        old_nonce = g.get('db').getObserverNonceBytes(addr)
        signed_message = request.get_json()["signedMessage"]
    except Exception as e:
        print(e)
        raise InvalidUsage('Address or signed message missing', status_code=400)
    if isValidEthereumAddress(addr) is False:
        raise InvalidUsage('Address is not valid', status_code=400)
    nonce = old_nonce.encode('utf-8')
    g.get('db').updateObserverNonceBytes(nonce='NULL', public_address=addr)
    message_hash = sha3.keccak_256(nonce).hexdigest()
    message_hash = encode_defunct(hexstr=message_hash)
    try:
        signed_public_key = Account.recover_message(message_hash, signature=signed_message)
    except Exception as e:
        print(e)
        print('message could not be checked')
    try:
        email = request.get_json()["email"]
        secret = request.get_json()["secret"]
    except Exception as e:
        print(e)
        email = None
        secret = None
    if (email is not None and isValidEmailAddress(email) is False or
        secret is not None and isValidSecret(secret) is False):
        raise InvalidUsage('Email or secret are not valid', status_code=400)
    if signed_public_key.lower() == addr.lower():
        email_from_addr = g.get('db').selectEmailFromObserverAddress(addr)
        if email_from_addr == None or email_from_addr == '' or email_from_addr == b'NULL':
            if email != None:
                try:
                    g.get('db').updateObserverEmail(email, addr)
                    email_status = google_email.send_email(email, secret)
                    if email_status == False:
                        raise InvalidUsage('Email failed to send', status_code=500)
                    return {'result':True}
                except Exception as e:
                    print(e)
                    raise InvalidUsage('Email failed', status_code=500)
        encoded_jwt = encode_jwt(addr.lower())
        g.get('db').updateObserverJWT(encoded_jwt, '', addr)
        frontend_exp = time.time() + 604800
        response_message += b'{ "address": "' + bytes(addr.lower(), 'utf-8') + b'", "exp": ' + bytes(str(frontend_exp), 'utf-8') +  b' } '
        @after_this_request
        def add_header(response):
            response.set_cookie('jwt', encoded_jwt.decode('utf-8'), max_age=604800, secure=True, httponly=True)#, samesite="Strict") #secure=True, httponly=True, samesite="Strict")
            return response
        return response_message
    else:
        print("Login Failed")
        raise InvalidUsage('Login failed', status_code=400)


@app.route('/editProfile', methods=['POST'])
def edit_profile():
    try:
        user_jwt = request.cookies.get('jwt')
        decoded_jwt = decode_jwt(user_jwt)
        public_address = decoded_jwt["address"]
        observer_id = g.get('db').selectObserverIDFromAddress(public_address)
    except Exception as e:
        print(e)
        raise InvalidUsage('message', status_code=400)
    if isValidEthereumAddress(public_address) is False:
        raise InvalidUsage('message', status_code=400)
    try:
        username = request.get_json()["username"]
        if (username != "null" and
            username != None and
            isValidUserSetting(username)):
            g.get('db').updateObserverUsername(username, public_address)
    except Exception as e:
        print(e)
    try:
        bio = request.get_json()["bio"]
        if (bio != "null" and
            bio != None and
            isValidUserSetting(bio)):
            g.get('db').updateObserverBio(bio, public_address)
    except Exception as e:
        print(e)
    try:
        location = request.get_json()["location"]
        if (location != "null" and
            location != None and
            isValidUserSetting(location)):
            g.get('db').updateObserverLocation(location, public_address)
    except Exception as e:
        print(e)
    try:
        deleted_stations = request.get_json()["deleted_stations"]
        for station in deleted_stations:
            result = g.get('db').deleteStation(station, observer_id)
            if result is not True:
                print("failed to delete station")
    except Exception as e:
        print(e)
    try:
        station_name = request.get_json()['new_station_names']
        
        for station in station_name:
            result = g.get('db').updateStationName(station, station_name[station], observer_id)
            if result is not True:
                print("failed ot update name for " + station + " " + station_name[station])
    except Exception as e:
        print(e)
    try:
        station_notes = request.get_json()['new_station_notes']
        for station in station_notes:
            result = g.get('db').updateStationNotes(station, station_notes[station], observer_id)
            if result is not True:
                print("failed ot update notes for " + station + ' ' + station_notes[station])
    except Exception as e:
        print(e)
    return {}


@app.route('/claimAccount', methods=['POST'])
def claim_account():
    try:
        email = request.get_json()['email']
    except Exception as e:
        print(e)
        return {'result': False}
    if isValidEmailAddress(email) is False:
        raise InvalidUsage('message', status_code=400)
    try:
        with open('unsafe_private.pem', 'r') as file:
            private_key = file.read()
        private_rsa_key = load_pem_private_key(bytes(private_key, 'utf-8'), password=None, backend=default_backend())
        results = g.get('db').selectObserverAddressFromEmail(email)
        if results is not None:
            results = results.decode('utf-8')
        else:
            return {'result': False}
        old_password = g.get('db').selectObserverPasswordFromAddress(results)
        if old_password is not None:
            old_password = old_password.decode('utf-8')
            try:
                if decode_jwt(old_password):
                    return {'result': True}
            except:
                print('User already claimed account.')

        number = str(secrets.randbits(64))
        jwt_payload = {
                'email': email,
                'secret': number,
                'exp': datetime.utcnow() + timedelta(minutes=30)
            }
        encoded_jwt = encode(jwt_payload, private_rsa_key, algorithm='RS256')
        g.get('db').updateObserverPassword(encoded_jwt.decode('utf-8'), results)
        message_text = 'Please use the following link to verify your ownership of the following email ' + \
                email + '\n\nhttps://trusat.org/claim/' + encoded_jwt.decode('utf-8') + '\nThis link will expire in 24 hours.' + \
                '\n\nIf you did not request recovery of your account please contact us at:\nHelp@Beta.TruSat.org\n'
        data = {"from": "TruSat Help <" + MAILGUN_EMAIL_ADDRESS + ">",
                "to": [email],
                "subject": "TruSat - Recover Account",
                "text": message_text}
        response = requests.post(
                "https://api.mailgun.net/v3/beta.trusat.org/messages",
                auth=("api", MAILGUN_API_KEY),
                data=data
                )
        if response.status_code != 200:
            print("Email failed to send.")
            raise InvalidUsage('message', status_code=500)
        else:
            return {'result': True}
    except Exception as e:
        print(e)
        raise InvalidUsage('message', status_code=500)
    return {'result': False}


@app.route('/verifyClaimAccount', methods=['POST'])
def verify_claim_account():
    response_message = b''
    try:
        message_text = request.get_json()["secret"]
        address = request.get_json()["address"]
        user_jwt = request.get_json()['jwt']
    except Exception as e:
        print(e)
        raise InvalidUsage('message', status_code=400)
    if (isValidEthereumAddress(address) is False or
        isValidSecret(message_text) is False):
        raise InvalidUsage('message', status_code=400)
    #Lookup number and old address
    try:
        decoded_jwt = decode_jwt(user_jwt)
        secret = decoded_jwt["secret"]
        to = decoded_jwt["email"]
        old_address = g.get('db').selectObserverAddressFromPassword(user_jwt).decode('utf-8')
        if old_address is None:
            raise InvalidUsage('message', status_code=400)

        #replace address
        encoded_jwt = encode_jwt(address)
        g.get('db').updateObserverAddress(address, old_address)
        message_text = 'Save this email: TruSat account recovery info for ' + to + '\n\n' + \
            'To log into TruSat, you\'ll need your password AND this secret code:\n\n' + message_text + \
            '\n\nThis email is the only time we can send you this code. TruSat cannot reset your password for you. Please save this email forever and make a note of the password you used.\n\n' + \
            'Login here: trusat.org/login\n\n' + \
            'Why do we do it this way? Read more (trusat.org/faq)\n\n' + \
            'Questions? Please email: Help@Beta.TruSat.org'
        data = {"from": "TruSat Help <" + MAILGUN_EMAIL_ADDRESS + ">",
            "to": [to],
            "subject": "TruSat - Save this email: Recovery Info",
            "text": message_text}
        response = requests.post(
            "https://api.mailgun.net/v3/beta.trusat.org/messages",
            auth=("api", MAILGUN_API_KEY),
            data=data
            )
        if response.status_code != 200:
            print("Email failed to send.")
            raise InvalidUsage('message', status_code=500)
        g.get('db').updateObserverJWT(encoded_jwt, "", address)
        frontend_exp = time.time() + 604800
        response_message += b'{ "address": "' + bytes(address.lower(), 'utf-8') + b'", "exp": ' + bytes(str(frontend_exp), 'utf-8') +  b' } '
        @after_this_request
        def add_header(response):
            response.set_cookie('jwt', encoded_jwt.decode('utf-8'), max_age=604800, secure=True, httponly=True)#, samesite="Strict") #secure=True, httponly=True, samesite="Strict")
            return response
        return response_message
    except Exception as e:
        print(e)
        raise InvalidUsage('message', status_code=500)


@app.route('/submitObservation', methods=['POST'])
def submit_observation():
    try:
        user_jwt = request.cookies.get('jwt')
        decoded_jwt = decode_jwt(user_jwt)
        user_addr = decoded_jwt["address"]
    except Exception as e:
        print(e)
        raise InvalidUsage('message', status_code=400)
    if isValidEthereumAddress(user_addr) is False:
        raise InvalidUsage('message', status_code=400)
    try:
        single = request.get_json()["single"]
    except Exception as e:
        print(e)
    parsed_iod = []
    try:
        multiple = request.get_json()["multiple"]
        results = g.get('db').addObserverParsedIOD(multiple)
        if results is not False:
            (success, error_messages) = results
        else:
            raise InvalidUsage('message', status_code=500)
    except Exception as e:
        print(e)
        raise InvalidUsage('message', status_code=500)
    success_length = {'success':success, 'error_messages':error_messages}
    return success_length


@app.route('/seesat', methods=['POST'])
def seesat():
    email_information = request.get_json()["message"]["data"]
    email_history = urlsafe_b64decode(email_information).decode('utf-8')
    email_history = json.loads(email_history)
    # print(email_history)
    # print(google_email.get_email_history(email_history['historyId']))
    return ('', 204)


@app.route('/getObservationStations', methods=['POST'])
def get_observationStations():
    try:
        user_jwt = request.cookies.get('jwt')
        decoded_jwt = decode_jwt(user_jwt)
        jwt_user_addr = decoded_jwt["address"]
    except Exception as e:
        print(e)
    if jwt_user_addr is None or isValidEthereumAddress(jwt_user_addr) is False:
        raise InvalidUsage('User needs to log in', status_code=400)
    try:
        observation_station_numbers = g.get('db').selectUserStationNumbers_JSON(jwt_user_addr)
        return observation_station_numbers
    except Exception as e:
        print(e)
        raise InvalidUsage('Could not get station information', status_code=500)


@app.route('/generateStation', methods=['POST'])
def generate_station():
    try:
        user_jwt = request.cookies.get('jwt')
        decoded_jwt = decode_jwt(user_jwt)
        user_addr = decoded_jwt["address"]
        station_name = request.get_json()["station"]
        latitude = request.get_json()["latitude"]
        longitude = request.get_json()["longitude"]
        elevation = request.get_json()["elevation"]
        notes = request.get_json()["notes"]
    except Exception as e:
        print(e)
        raise InvalidUsage('Missing parameter(s)', status_code=400)
    if isValidEthereumAddress(user_addr) is False:
        raise InvalidUsage('message', status_code=400)
    try:
        user_id = g.get('db').selectObserverIDFromAddress(user_addr)
        latest_station = g.get('db').selectLatestStationID()
        if latest_station[0:1] == 'T':
            station_index = latest_station[1:]
            station_index = int(station_index, 36) + 1
            # Prevent I or O character
            if (station_index & 18) == 18 or (station_index & 24) == 24:
                station_index = station_index + 1
            if (station_index & 648) == 648 or (station_index & 864) == 864:
                station_index = station_index + 36
            if (station_index & 23328) == 23328 or (station_index & 31104) == 31104:
                station_index = station_index + 1296
            station_index = numpy.base_repr(station_index, 36)
            station_id = 'T' + station_index.rjust(3, '0')
        else:
            station_id = 'T000'
        print(station_id)
        station_result = g.get('db').addStation(station_id, user_id, latitude, longitude, elevation, station_name, notes)
        if station_result is None:
            raise InvalidUsage('Could not add station', status_code=500)
        if station_result is False:
            raise InvalidUsage('User has too many stations', status_code=400)
        # get last station
        # increment station
        # remove O and I
        # set and return
        return {'station_id': station_id}
    except Exception as e:
        print(e)
        raise InvalidUsage('message', status_code=500)

@app.route('/getAllObservations', methods=['POST'])
def get_all_observations():
    try:
        user_jwt = request.cookies.get('jwt')
        decoded_jwt = decode_jwt(user_jwt)
        user_addr = decoded_jwt["address"]
    except Exception as e:
        print(e)
        raise InvalidUsage('Missing parameter(s)', status_code=400)
    if isValidEthereumAddress(user_addr) is False:
        raise InvalidUsage('message', status_code=400)
    try:
        observations = g.get('db').selectUserIODs(user_addr)
        return observations
    except Exception as e:
        print(e)
        raise InvalidUsage('query failed', status_code=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0')