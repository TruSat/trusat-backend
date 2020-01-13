from http.server import ThreadingHTTPServer,  HTTPServer, BaseHTTPRequestHandler
from http import cookies
import ssl
from io import BytesIO
import json
import secrets
import datetime as dt
import jwt
import copy
from jwt import encode, decode
from datetime import datetime, timedelta
from eth_account import Account
from eth_account.messages import defunct_hash_message, encode_defunct
import sha3
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from base64 import urlsafe_b64decode
from coinaddr import validate
import os
import re
import requests
import numpy
import time

import database
import google_email

MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY', False)
MAILGUN_EMAIL_ADDRESS = os.getenv('MAILGUN_EMAIL_ADDRESS', False)
WEBSITE_ORIGINS = os.getenv('WEBSITE_ORIGINS', False)
PORT_NUMBER = 8080

#TODO: take object instead of address to encode with a specified time
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

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        # TODO: Find which timeout is correct
        self.timeout = 10
        print(request)
        # Read database config from login.txt
        f = open('login.txt', 'r')
        lines = f.readlines()
        db_name = lines[0].strip()
        db_type = lines[1].strip()
        endpoint = lines[2].strip()
        username = lines[3].strip()
        password = lines[4].strip()
        f.close()
        self.db = database.Database(db_name, db_type, endpoint, username, password)
        super().__init__(request, client_address, server)

    def send_500(self, message='', explain='', request_origin='*'):
        self.send_response(500, message=message)
        self.send_header('Access-Control-Allow-Origin', request_origin)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        body_bytes = {"error": message + ': ' + explain}
        self.wfile.write(bytes(json.dumps(body_bytes), 'utf-8'))
        self.db.clean()

    def send_400(self, message='', explain='', request_origin='*'):
        self.send_response(400, message=message)
        self.send_header('Access-Control-Allow-Origin', request_origin)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        body_bytes = {"error": message + ': ' + explain}
        self.wfile.write(bytes(json.dumps(body_bytes), 'utf-8'))
        self.db.clean()

    def send_401(self, message='', explain='', request_origin='*'):
        self.send_response(401, message=message)
        self.send_header('Access-Control-Allow-Origin', request_origin)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        body_bytes = {"error": message + ': ' + explain}
        self.wfile.write(bytes(json.dumps(body_bytes), 'utf-8'))
        self.db.clean()

    def send_404(self, message='', explain='', request_origin='*'):
        self.send_error(404, message=message)
        self.send_header('Access-Control-Allow-Origin', request_origin)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.end_headers()
        self.db.clean()

    def send_204(self, request_origin='*'):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', request_origin)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.end_headers()

    def send_200_JSON(self, body_data, request_origin='*'):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', request_origin)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.end_headers()
        try:
            body_bytes = bytes(body_data, 'utf-8')
        except Exception as e:
            print(e)
            body_bytes = b'[]'
        self.wfile.write(body_bytes)

    def send_200_JSON2(self, body_data, request_origin='*'):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', request_origin)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.end_headers()
        self.wfile.write(body_data)

    def send_200_JSON_cache(self, body_data, request_origin='*'):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', request_origin)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Cache-Control', 'max-age=300')
        self.end_headers()
        try:
            body_bytes = bytes(body_data, 'utf-8')
        except Exception as e:
            print(e)
            body_bytes = b'[]'
        self.wfile.write(body_bytes)

    def send_200_text(self, body_data, request_origin='*'):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', request_origin)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.end_headers()
        try:
            body_bytes = bytes(body_data, 'utf-8')
        except Exception as e:
            print(e)
            body_bytes = b''
        self.wfile.write(body_bytes)

    def send_200_text_cache(self, body_data, request_origin='*'):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', request_origin)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Cache-Control', 'max-age=300')
        self.end_headers()
        try:
            body_bytes = bytes(body_data, 'utf-8')
        except Exception as e:
            print(e)
            body_bytes = b''
        self.wfile.write(body_bytes)

    def do_OPTIONS(self):
        try:
            request_origin = self.headers.get("Origin")
            if request_origin in WEBSITE_ORIGINS:
                request_origin = request_origin
            else:
                request_origin = '*'
            print(request_origin)
        except Exception as e:
            print(e)
            request_origin = False
        try:
            path = self.path.split('?')[0]
        except Exception as e:
            print(e)
            path = self.path

        if path == "/catalog/priorities" or \
                path == "/catalog/undisclosed" or \
                path == "/catalog/debris" or \
                path == "/catalog/latest" or \
                path == "/catalog/all" or \
                path == "/tle/trusat_all.txt" or \
                path == "/tle/trusat_priorities.txt" or \
                path == "/tle/trusat_high_confidence.txt" or \
                path == "/astriagraph" or \
                path == "/profile" or \
                path == "/object/influence" or \
                path == "/object/info" or \
                path == "/object/history" or \
                path == "/object/userSightings" or \
                path == "/tle/object" or \
                path == "/findObject" or \
                path == "/cookieMonster" or \
                path == "/errorTest":
            self.send_response(200)
            self.send_header('Accept', 'GET')
            #self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Origin', request_origin)
            self.send_header('Access-Control-Allow-Credentials', 'true')
            self.send_header('Access-Control-Allow-Headers', 'Cache-Control')
            self.end_headers()
        elif path == "/getNonce" or \
                path == "/signup" or \
                path == "/login" or \
                path == "/editProfile" or \
                path == "/claimAccount" or \
                path == "/verifyClaimAccount" or \
                path == "/getObservationStations" or \
                path == "/generateStation" or \
                path == "/submitObservation":
            self.send_response(200)
            self.send_header('Accept', 'POST')
            self.send_header('Access-Control-Allow-Headers', '*')
            self.send_header('Access-Control-Allow-Origin', request_origin)
            self.send_header('Access-Control-Allow-Credentials', 'true')
            self.end_headers()
        else:
            self.send_404(request_origin=request_origin)

    def do_GET(self):
        try:
            request_origin = self.headers.get("Origin")
            if request_origin in WEBSITE_ORIGINS:
                request_origin = request_origin
            else:
                request_origin = '*'
            print(request_origin)
        except Exception as e:
            print(e)
            request_origin = False
        try:
            user_cookie = cookies.SimpleCookie(self.headers.get('Cookie'))
            cookie_jwt = user_cookie['jwt'].value
            print("COOKIES!")
            print(user_cookie)
        except Exception as e:
            print(e)
            user_cookie = False
            cookie_jwt = False
        try:
            path = self.path.split('?')[0]
            parameters = self.path.split('?')[1]
        except Exception as e:
            print(e)
            path = self.path
        try:
            parameters = parameters.split('&')
            parameters_map = {}
            for param in parameters:
                parameters_map[param.split('=')[0]] = param.split('=')[1]
        except Exception as e:
            print(e)
            parameters_map = {}
        if path == "/catalog/priorities":
            try:
                json_object = self.db.selectCatalog_Priorities_JSON()
            except Exception as e:
                print(e)
                self.send_500(message='Could not get priorities', explain='Priorities query failed', request_origin=request_origin)
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object, request_origin=request_origin)
            else:
                self.send_200_JSON_cache(json.dumps({}), request_origin=request_origin)
                return

        elif path == "/catalog/undisclosed":
            try:
                json_object = self.db.selectCatalog_Undisclosed_JSON()
            except Exception as e:
                print(e)
                self.send_500(message='Could not get undisclosed', explain='Undisclosed query failed', request_origin=request_origin)
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object, request_origin=request_origin)
            else:
                self.send_200_JSON_cache(json.dumps({}), request_origin=request_origin)
                return

        elif path == "/catalog/debris":
            try:
                json_object = self.db.selectCatalog_Debris_JSON()
            except Exception as e:
                print(e)
                self.send_500(message='Could not get debris', explain='Debris query failed', request_origin=request_origin)
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object, request_origin=request_origin)
            else:
                self.send_200_JSON_cache(json.dumps({}), request_origin=request_origin)
                return

        elif path == "/catalog/latest":
            try:
                json_object = self.db.selectCatalog_Latest_JSON()
            except Exception as e:
                print(e)
                self.send_500(message='Could not get latest', explain='Latest query failed', request_origin=request_origin)
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object, request_origin=request_origin)
            else:
                self.send_200_JSON_cache(json.dumps({}), request_origin=request_origin)
                return

        elif path == "/catalog/all":
            try:
                json_object = self.db.selectCatalog_All_JSON()
            except Exception as e:
                print(e)
                self.send_500(message='Could not get all', explain='All query failed', request_origin=request_origin)
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object, request_origin=request_origin)
            else:
                self.send_200_JSON_cache(json.dumps({}), request_origin=request_origin)
                return

        elif path == "/tle/trusat_all.txt":
            try:
                two_line_elements = self.db.selectTLE_all()
            except Exception as e:
                print(e)
                self.send_500(message='Could not get TLEs', explain='TLE query failed', request_origin=request_origin)
                return
            if two_line_elements is not False:
                self.send_200_text_cache(two_line_elements, request_origin=request_origin)
            else:
                self.send_200_text_cache('', request_origin=request_origin)
                return

        elif path == "/tle/trusat_priorities.txt":
            try:
                two_line_elements = self.db.selectTLE_priorities()
            except Exception as e:
                print(e)
                self.send_500(message='Could not get TLEs', explain='TLE query failed', request_origin=request_origin)
                return
            if two_line_elements is not False:
                self.send_200_text_cache(two_line_elements, request_origin=request_origin)
            else:
                self.send_200_text_cache('', request_origin=request_origin)
                return

        elif path == "/tle/trusat_high_confidence.txt":
            try:
                two_line_elements = self.db.selectTLE_high_confidence()
            except Exception as e:
                print(e)
                self.send_500(message='Could not get TLEs', explain='TLE query failed', request_origin=request_origin)
                return
            if two_line_elements is not False:
                self.send_200_text_cache(two_line_elements, request_origin=request_origin)
            else:
                self.send_200_text_cache('', request_origin=request_origin)
                return

        elif path == "/astriagraph":
            try:
                tles_json = self.db.selectTLE_Astriagraph()
            except Exception as e:
                print(e)
                self.send_500(message='Could not get TLEs', explain='TLE query failed', request_origin=request_origin)
                return
            if tles_json is not False:
                self.send_200_text_cache(tles_json, request_origin=request_origin)
            else:
                self.send_200_text_cache('', request_origin=request_origin)
                return

        elif path == "/profile":
            jwt_user_addr = ''
            try:
                user_addr = parameters_map["address"]
            except Exception as e:
                print(e)
                self.send_400(message='Missing address', explain='Address is missing from the parameters', request_origin=request_origin)
                return
            if isValidEthereumAddress(user_addr) is False:
                self.send_400(message='Address is invalid', explain='Address is not an Ethereum Address', request_origin=request_origin)
                return
            try:
                user_profile_json = self.db.selectProfileInfo_JSON(user_addr)
                objects_observed_json = self.db.selectUserObjectsObserved_JSON(user_addr)
                observation_history_json = self.db.selectUserObservationHistory_JSON(user_addr)
                user_profile_json["objects_observed"] = objects_observed_json
                user_profile_json["observation_history"] = observation_history_json
                user_profile_json["observation_stations"] = []
            except Exception as e:
                print(e)
                self.send_500(message='Could not retrieve user information', explain='User information is missing in the database', request_origin=request_origin)
                return
            try:
                if cookie_jwt is not False:
                    user_jwt = cookie_jwt
                else:
                    user_jwt = parameters_map["jwt"]
                decoded_jwt = decode_jwt(user_jwt)
                jwt_user_addr = decoded_jwt["address"]
            except Exception as e:
                print(e)
                pass
            if isValidEthereumAddress(jwt_user_addr) is False:
                self.send_400(message='Invalid Ethereum address', explain='Ethereum address pulled from user JWT is not valid', request_origin=request_origin)
                return
            if jwt_user_addr.lower() == user_addr.lower():
                try:
                    observation_station_numbers = self.db.selectUserStationNumbers_JSON(user_addr)
                    for station in observation_station_numbers:
                        user_profile_json["observation_stations"].append(station)
                except Exception as e:
                    print(e)
                    self.send_500(message='Observation information could not be retrieved', explain='Error in query to retrieve observer station information', request_origin=request_origin)
                    return

            for k,v in user_profile_json.items():
                if v == None or v =='NULL':
                    user_profile_json[k] = ""
            user_profile = json.dumps(user_profile_json)

            self.send_200_JSON_cache(user_profile, request_origin=request_origin)

        elif path == '/object/influence':
            try:
                norad_number = parameters_map['norad_number']
            except Exception as e:
                print(e)
                self.send_400(message='Norad number is missing from parameters', explain='Did not recieve norad_number in the URI', request_origin=request_origin)
                return
            if isValidNoradNumber(norad_number) is False:
                self.send_400(message='Norad number is not valid', explain='Norad number is not a number from 1-99999', request_origin=request_origin)
                return
            try:
                json_object = self.db.selectObjectInfluence_JSON(norad_number)
            except Exception as e:
                print(e)
                self.send_500(message='Object influence could not be retrieved', explain='Query for object influce failed', request_origin=request_origin)
                return
            if json_object:
                self.send_200_JSON_cache(json_object, request_origin=request_origin)
            else:
                self.send_200_JSON(json.dumps({}), request_origin=request_origin)
                return

        elif path == '/object/info':
            try:
                norad_number = parameters_map['norad_number']
            except Exception as e:
                print(e)
                self.send_400(message='Norad number is missing from parameters', explain='Did not recieve norad_number in the URI', request_origin=request_origin)
                return
            if isValidNoradNumber(norad_number) is False:
                self.send_400(message='Norad number is not valid', explain='Norad number is not a number from 1-99999', request_origin=request_origin)
                return
            try:
                json_object = self.db.selectObjectInfo_JSON(norad_number)
            except Exception as e:
                print(e)
                self.send_500(message='Object info could not be retrieved', explain='Query for object info failed', request_origin=request_origin)
                return
            if json_object:
                self.send_200_JSON_cache(json_object, request_origin=request_origin)
            else:
                self.send_200_JSON_cache(json.dumps({}), request_origin=request_origin)
                return

        elif path == '/object/history':
            try:
                norad_number = parameters_map['norad_number']
                year = parameters_map["year"]
                int_year = int(year)
            except Exception as e:
                print(e)
                self.send_400(message='Missing norad number and/or year', explain='Parameters need a valid year and norad number', request_origin=request_origin)
                return
            if (isValidNoradNumber(norad_number) is False or
                int_year < 1957 or
                int_year > datetime.now().year):
                self.send_400(message='Year is out of range or norad number is invalid', explain='year is less than 1957, greater than the current year, or norad number is not valid', request_origin=request_origin)
                return
            try:
                real_entry = self.db.selectObjectHistoryByMonth_JSON(norad_number, year)
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
                response_body = json.dumps(year_response)
                self.send_200_JSON_cache(response_body, request_origin=request_origin)
            except Exception as e:
                print(e)
                self.send_500(message='Could not get history', explain='Object history querie failed', request_origin=request_origin)
                return

        elif path == '/object/userSightings':
            response_body = []
            try:
                norad_number = parameters_map['norad_number']
                if cookie_jwt is not False:
                    user_jwt = cookie_jwt
                else:
                    user_jwt = parameters_map['jwt']
                decoded_jwt = decode_jwt(user_jwt)
                public_address = decoded_jwt["address"]
            except Exception as e:
                print(e)
                self.send_400(message='Parameter(s) missing', explain='norad_number, jwt, address', request_origin=request_origin)
                return
            if (isValidNoradNumber(norad_number) is False or
                isValidEthereumAddress is False):
                self.send_400(message='Invalid norad number or Ethereum address', explain='Not proper format', request_origin=request_origin)
                return
            try:
                response_body = self.db.selectObjectUserSightings_JSON(norad_number, public_address)
                response_body = json.dumps(response_body)
                self.send_200_JSON_cache(response_body, request_origin=request_origin)
            except Exception as e:
                print(e)
                self.send_500(message='userSighting failed', explain='Query for userSightings was not successful', request_origin=request_origin)
                return

        elif path == "/tle/object":
            try:
                norad_number = parameters_map["norad_number"]
            except Exception as e:
                print(e)
                self.send_400(message='Missing Norad number', explain='Norad number parameter missing', request_origin=request_origin)
                return
            if isValidNoradNumber(norad_number) is False:
                self.send_400(message='Invalid Norad number', explain='Norad number is not valid', request_origin=request_origin)
                return
            try:
                two_line_elements = self.db.selectTLE_single(norad_number)
            except Exception as e:
                print(e)
                self.send_500(message='Could not get TLE', explain='Query failed to get TLE', request_origin=request_origin)
                return
            if two_line_elements:
                self.send_200_text_cache(two_line_elements, request_origin=request_origin)
            else:
                self.send_200_text_cache("", request_origin=request_origin)
                return

        elif path == "/findObject":
            try:
                partial_string = parameters_map["objectName"]
            except Exception as e:
                print(e)
                self.send_400(message='Object name missing', explain='Object name parameter missing', request_origin=request_origin)
                return
            try:
                objects = self.db.selectFindObject(partial_string)
                self.send_200_text_cache(objects, request_origin=request_origin)
            except Exception as e:
                self.send_500(message='Could not find object', explain='Query failed ot find object', request_origin=request_origin)
                print(e)
                return

        elif path == '/heartbeat':
            self.send_204(request_origin=request_origin)
            return

        elif path == '/errorTest':
            self.send_400(message='message', explain='explanation', request_origin=request_origin)
            return

        elif path == '/cookieMonster':
            try:
                ck = cookies.SimpleCookie(self.headers.get('Cookie'))
                print('COOKIES')
                print(ck['jwt'].value)
            except:
                print('noo cookies :(')
            C = cookies.SimpleCookie()
            cookie_exp = time.strftime("%a, %d %Y %H:%M:%S %Z", time.gmtime(time.time() + 518400))
            jwt_cookie = 'jwt=\"' + 'test' + '\"; Max-Age=6048000; Secure; HttpOnly; SameSite=Strict'
            C.load(jwt_cookie)
            print(cookie_exp)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', request_origin=request_origin)
            #self.send_header('Access-Control-Allow-Origin', 'http://devvymcdevface.trusat.org')
            self.send_header('Access-Control-Allow-Credentials', 'true')
            self.send_header("Set-Cookie", C.output(header='', sep=''))
            self.end_headers()
            return

        else:
            self.send_response(404)
        self.db.clean()


    def do_POST(self):
        try:
            request_origin = self.headers.get("Origin")
            if request_origin in WEBSITE_ORIGINS:
                request_origin = request_origin
            else:
                request_origin = '*'
            print(request_origin)
        except Exception as e:
            print(e)
            request_origin = False
        response_body = b""
        signed_public_key = '0'
        try:
            user_cookie = cookies.SimpleCookie(self.headers.get('Cookie'))
            cookie_jwt = user_cookie['jwt'].value
            print("COOKIE!")
            print(user_cookie)
        except Exception as e:
            print(e)
            user_cookie = False
            cookie_jwt = False

        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            json_body = json.loads(body)
        except Exception as e:
            print(e)
            self.send_400(message='Body improperly formatted', explain='Body is not properly formatted', request_origin=request_origin)
            return

        ### GET NONCE ENDPOINT ###
        if self.path == "/getNonce":
            try:
                addr = json_body["address"]
            except Exception as e:
                print(e)
                self.send_400(message='Ethereum address missing', explain='Ethereum address is not a parameter', request_origin=request_origin)
                return
            if isValidEthereumAddress(addr) is False:
                self.send_400(message='Invalid Ethereum address', explain='Ethereum address is not valid', request_origin=request_origin)
                return
            try:
                email = json_body["email"]
                if isValidEmailAddress is False:
                    self.send_400(message='message', explain='explanation', request_origin=request_origin)
                    return
                results = self.db.selectObserverAddressFromEmail(email)
                if len(results) == 42:
                    self.send_200_JSON(json.dumps({}), request_origin=request_origin)
                    return
            except Exception as e:
                print(e)
                pass

            try:
                public_address_count = self.db.getObserverCountByID(public_address=addr)
            except Exception as e:
                print(e)
                self.send_500(message='message', explain='explanation', request_origin=request_origin)
                return
            random_number = str(secrets.randbits(256))
            response_message = '{"nonce":\"%s\"}' % random_number
            if public_address_count[0] == None or public_address_count[0] == 0:
                # New User
                try:
                    self.db.addObserver(addr, "NULL", 0, "NULL")
                    self.db.updateObserverNonceBytes(nonce=random_number, public_address=addr)
                except Exception as e:
                    print(e)
                    self.send_500(message='message', explain='explanation', request_origin=request_origin)
                    return
            elif public_address_count[0] >= 1:
                # Old User
                try:
                    self.db.updateObserverNonceBytes(nonce=random_number, public_address=addr)
                except Exception as e:
                    print(e)
                    self.send_500(message='message', explain='explanation', request_origin=request_origin)
                    return
            self.send_200_JSON(response_message, request_origin=request_origin)

        elif self.path == "/signup":
            try:
                addr = json_body["address"]
                if isValidEthereumAddress(addr) is False:
                    self.send_400(message='message', explain='explanation', request_origin=request_origin)
                    return
                old_nonce = self.db.getObserverNonceBytes(addr)
                email = json_body["email"]
                signed_message = json_body["signedMessage"]
                payload = json_body["secret"]
            except Exception as e:
                print(e)
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return

            try:
                if (isValidEmailAddress(email) is False or
                    isValidSecret(payload) is False):
                    self.send_400(message='message', explain='explanation', request_origin=request_origin)
                    return

                nonce = old_nonce.encode('utf-8')
                self.db.updateObserverNonceBytes(nonce='NULL', public_address=addr)
                message_hash = sha3.keccak_256(nonce).hexdigest()
                message_hash = encode_defunct(hexstr=message_hash)
            except Exception as e:
                print(e)
                self.send_500(message='message', explain='explanation', request_origin=request_origin)
                return
            try:
                signed_public_key = Account.recover_message(message_hash, signature=signed_message)
            except Exception as e:
                print(e)
                print('message could not be checked')
            try:
                if signed_public_key.lower() == addr.lower():
                    email_from_addr = self.db.selectEmailFromObserverAddress(addr)
                    if email_from_addr == None or email_from_addr == '' or email_from_addr == b'NULL':
                        if email != None or email != 'null' or email != 'NULL' or email != '':
                            try:
                                self.db.updateObserverEmail(email, addr)
                                message_text = 'Save this email: TruSat account recovery info for ' + email + '\n\n' + \
                                        'To log into TruSat, you\'ll need your password AND this secret code:\n\n' + payload + \
                                        '\n\nThis email is the only time we can send you this code. TruSat cannot reset your password for you. Please save this email forever and make a note of the password you used.\n\n' + \
                                        'Login here: trusat.org/login\n\n' + \
                                        'Why do we do it this way? Read more (trusat.org/faq)\n\n' + \
                                        'Questions? Please email: Help@Beta.TruSat.org'
                                data = {"from": "TruSat Help <" + MAILGUN_EMAIL_ADDRESS + ">",
                                        "to": [email],
                                        "subject": "DEVVY TEST TruSat - Save this email: Recovery Info",
                                        "text": message_text}
                                response = requests.post(
                                        "https://api.mailgun.net/v3/beta.trusat.org/messages",
                                        auth=("api", MAILGUN_API_KEY),
                                        data=data
                                    )
                                if response.status_code != 200:
                                    print(response)
                                    print("Email failed to send.")
                                    self.send_500(message='message', explain='explanation', request_origin=request_origin)
                                    return
                                self.send_200_JSON(json.dumps({'result': True}), request_origin=request_origin)
                                return
                            except Exception as e:
                                print(e)
                                self.send_500(message='message', explain='explanation', request_origin=request_origin)
                                return
            except Exception as e:
                print(e)
            else:
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            self.send_500(message='message', explain='explanation', request_origin=request_origin)
            return


        ### LOGIN ENDPOINT ###
        elif self.path == "/login":
            try:
                addr = json_body["address"]
                old_nonce = self.db.getObserverNonceBytes(addr)
                signed_message = json_body["signedMessage"]
            except Exception as e:
                print(e)
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            if isValidEthereumAddress(addr) is False:
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            nonce = old_nonce.encode('utf-8')
            self.db.updateObserverNonceBytes(nonce='NULL', public_address=addr)
            message_hash = sha3.keccak_256(nonce).hexdigest()
            message_hash = encode_defunct(hexstr=message_hash)
            try:
                signed_public_key = Account.recover_message(message_hash, signature=signed_message)
            except Exception as e:
                print(e)
                print('message could not be checked')
            try:
                email = json_body["email"]
                secret = json_body["secret"]
            except Exception as e:
                print(e)
                email = None
                secret = None
            if (email is not None and isValidEmailAddress(email) is False or
                secret is not None and isValidSecret(secret) is False):
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            if signed_public_key.lower() == addr.lower():
                email_from_addr = self.db.selectEmailFromObserverAddress(addr)
                if email_from_addr == None or email_from_addr == '' or email_from_addr == b'NULL':
                    if email != None:
                        try:
                            self.db.updateObserverEmail(email, addr)
                            email_status = google_email.send_email(email, secret)
                            if email_status == False:
                                self.send_500(message='message', explain='explanation', request_origin=request_origin)
                                return
                            self.send_200_JSON(json.dumps({'result':True}), request_origin=request_origin)
                            return
                        except Exception as e:
                            print(e)
                            self.send_500(message='message', explain='explanation', request_origin=request_origin)
                            return
                encoded_jwt = encode_jwt(addr.lower())
                self.db.updateObserverJWT(encoded_jwt, '', addr)
                frontend_exp = time.time() + 604800
                response_message = b'{"jwt": "'
                response_message += encoded_jwt
                response_message += b'", "address": "' + bytes(addr.lower(), 'utf-8') + b'", "exp": ' + bytes(str(frontend_exp), 'utf-8') +  b' } '
                C = cookies.SimpleCookie()
                jwt_cookie = 'jwt=\"' + encoded_jwt.decode('utf-8') + '\"; Max-Age=604800; Secure; HttpOnly; SameSite=Strict'
                C.load(jwt_cookie)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', request_origin)
                self.send_header('Access-Control-Allow-Credentials', 'true')
                self.send_header("Set-Cookie", C.output(header='', sep=''))
                self.end_headers()
                self.wfile.write(response_message)
                return
            else:
                print("Login Failed")
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return

        elif self.path == "/editProfile":
            try:
                if cookie_jwt is not False:
                    user_jwt = cookie_jwt
                else:
                    user_jwt = json_body["jwt"]
                decoded_jwt = decode_jwt(user_jwt)
                public_address = decoded_jwt["address"]
                observer_id = self.db.selectObserverIDFromAddress(public_address)
            except Exception as e:
                print(e)
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            if isValidEthereumAddress(public_address) is False:
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            try:
                username = json_body["username"]
                if (username != "null" and
                    username != None and
                    isValidUserSetting(username)):
                    self.db.updateObserverUsername(username, public_address)
            except Exception as e:
                print("Username not being updated")
                print(e)
            #try:
            #    email = json_body["email"]
            #    if isValidEmailAddress(email):
            #        self.db.updateObserverEmail(email, public_address)
            #except Exception as e:
            #    print("Email not being updated")
            #    print(e)
            try:
                bio = json_body["bio"]
                if (bio != "null" and
                    bio != None and
                    isValidUserSetting(bio)):
                    self.db.updateObserverBio(bio, public_address)
            except Exception as e:
                print("Bio not being updated")
                print(e)
            try:
                location = json_body["location"]
                if (location != "null" and
                    location != None and
                    isValidUserSetting(location)):
                    self.db.updateObserverLocation(location, public_address)
            except Exception as e:
                print("Location not being updated")
                print(e)
            try:
                deleted_stations = json_body["deleted_stations"]
                for station in deleted_stations:
                    result = self.db.deleteStation(station, observer_id)
                    if result is not True:
                        print("failed to delete station")
            except Exception as e:
                print("No stations to delete")
                print(e)
            try:
                station_name = json_body['new_station_names']
                print('STATION')
                
                for station in station_name:
                    result = self.db.updateStationName(station, station_name[station], observer_id)
                    if result is not True:
                        print("failed ot update name for " + station + " " + station_name[station])
            except Exception as e:
                print('No station name change')
                print(e)
            try:
                station_notes = json_body['new_station_notes']
                for station in station_notes:
                    result = self.db.updateStationNotes(station, station_notes[station], observer_id)
                    if result is not True:
                        print("failed ot update notes for " + station + ' ' + station_notes[station])
            except Exception as e:
                print('No station notes change')
                print(e)
            self.send_200_JSON(response_body, request_origin=request_origin)

        elif self.path == '/claimAccount':
            try:
                email = json_body['email']
            except Exception as e:
                print(e)
                self.send_200_JSON(json.dumps({'result': False}), request_origin=request_origin)
                return
            if isValidEmailAddress(email) is False:
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            try:
                with open('unsafe_private.pem', 'r') as file:
                    private_key = file.read()
                private_rsa_key = load_pem_private_key(bytes(private_key, 'utf-8'), password=None, backend=default_backend())
                results = self.db.selectObserverAddressFromEmail(email)
                if results is not None:
                    results = results.decode('utf-8')
                else:
                    self.send_200_JSON(json.dumps({'result': False}), request_origin=request_origin)
                    return
                old_password = self.db.selectObserverPasswordFromAddress(results)
                if old_password is not None:
                    old_password = old_password.decode('utf-8')
                    try:
                        if decode_jwt(old_password):
                            self.send_200_JSON(json.dumps({'result': True}), request_origin=request_origin)
                            return
                    except:
                        print('User already claimed account.')

                number = str(secrets.randbits(64))
                jwt_payload = {
                        'email': email,
                        'secret': number,
                        'exp': datetime.utcnow() + timedelta(minutes=30)
                    }
                encoded_jwt = encode(jwt_payload, private_rsa_key, algorithm='RS256')
                self.db.updateObserverPassword(encoded_jwt.decode('utf-8'), results)
                message_text = 'Please use the following link to verify your ownership of the following email ' + \
                        email + '\n\nhttps://trusat.org/claim/' + encoded_jwt.decode('utf-8') + '\nThis link will expire in 24 hours.' + \
                        '\n\nIf you did not request recovery of your account please contact us at:\nHelp@Beta.TruSat.org\n'
                data = {"from": "TruSat Help <" + MAILGUN_EMAIL_ADDRESS + ">",
                        "to": [email],
                        "subject": "DEVVY TEST TruSat - Recover Account",
                        "text": message_text}
                response = requests.post(
                        "https://api.mailgun.net/v3/beta.trusat.org/messages",
                        auth=("api", MAILGUN_API_KEY),
                        data=data
                        )
                if response.status_code != 200:
                    print(response)
                    print("Email failed to send.")
                    self.send_500(message='message', explain='explanation', request_origin=request_origin)
                    return
                else:
                    self.send_200_JSON(json.dumps({'result': True}), request_origin=request_origin)
                    return
            except Exception as e:
                print(e)
                self.send_500(message='message', explain='explanation', request_origin=request_origin)
                return
            self.send_200_JSON(json.dumps({'result': False}), request_origin=request_origin)

        elif self.path == "/verifyClaimAccount":
            try:
                message_text = json_body["secret"]
                address = json_body["address"]
                if cookie_jwt is not False:
                    user_jwt = cookie_jwt
                else:
                    user_jwt = json_body["jwt"]
            except Exception as e:
                print(e)
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            if (isValidEthereumAddress(address) is False or
                isValidSecret(message_text) is False):
                print("Ëthereum address:")
                print(address)
                print("Secret:")
                print(message_text)
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            #Lookup number and old address
            try:
                decoded_jwt = decode_jwt(user_jwt)
                secret = decoded_jwt["secret"]
                to = decoded_jwt["email"]
                old_address = self.db.selectObserverAddressFromPassword(user_jwt).decode('utf-8')
                if old_address is None:
                    self.send_400(message='message', explain='explanation', request_origin=request_origin)
                    return

                #replace address
                encoded_jwt = encode_jwt(address)
                self.db.updateObserverAddress(address, old_address)
                message_text = 'Save this email: TruSat account recovery info for ' + to + '\n\n' + \
                    'To log into TruSat, you\'ll need your password AND this secret code:\n\n' + message_text + \
                    '\n\nThis email is the only time we can send you this code. TruSat cannot reset your password for you. Please save this email forever and make a note of the password you used.\n\n' + \
                    'Login here: trusat.org/login\n\n' + \
                    'Why do we do it this way? Read more (trusat.org/faq)\n\n' + \
                    'Questions? Please email: Help@Beta.TruSat.org'
                data = {"from": "TruSat Help <" + MAILGUN_EMAIL_ADDRESS + ">",
                    "to": [to],
                    "subject": "DEVVY TEST TruSat - Save this email: Recovery Info",
                    "text": message_text}
                response = requests.post(
                    "https://api.mailgun.net/v3/beta.trusat.org/messages",
                    auth=("api", MAILGUN_API_KEY),
                    data=data
                    )
                if response.status_code != 200:
                    print(response)
                    print("Email failed to send.")
                    self.send_500(message='message', explain='explanation', request_origin=request_origin)
                    return
                self.db.updateObserverJWT(encoded_jwt, "", address)
                frontend_exp = time.time() + 604800
                response_message = b'{"jwt": "'
                response_message += encoded_jwt
                response_message += b'", "address": "' + bytes(address.lower(), 'utf-8') + b'", "exp": ' + bytes(str(frontend_exp), 'utf-8') +  b' } '
                C = cookies.SimpleCookie()
                jwt_cookie = 'jwt=\"' + encoded_jwt.decode('utf-8') + '\"; Max-Age=604800; Secure; HttpOnly; SameSite=Strict'
                C.load(jwt_cookie)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.send_header('Access-Control-Allow-Origin', request_origin)
                self.send_header('Access-Control-Allow-Credentials', 'true')
                self.send_header("Set-Cookie", C.output(header='', sep=''))
                self.end_headers()
                self.wfile.write(response_message)
                self.db.updateObserverPassword('NULL', address)
                return

            except Exception as e:
                print(e)
                self.send_500(message='message', explain='explanation', request_origin=request_origin)
                return

        elif self.path == "/submitObservation":
            try:
                if cookie_jwt is not False:
                    user_jwt = cookie_jwt
                else:
                    user_jwt = json_body["jwt"]
                decoded_jwt = decode_jwt(user_jwt)
                user_addr = decoded_jwt["address"]
            except Exception as e:
                print(e)
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            if isValidEthereumAddress(user_addr) is False:
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            try:
                single = json_body["single"]
            except Exception as e:
                print(e)
            parsed_iod = []
            try:
                multiple = json_body["multiple"]
                results = self.db.addObserverParsedIOD(multiple)
                if results is not False:
                    (success, error_messages) = results
                else:
                    self.send_500(message='message', explain='explanation', request_origin=request_origin)
                    return
            except Exception as e:
                print(e)
                self.send_500(message='message', explain='explanation', request_origin=request_origin)
                return
            success_length = {'success':success, 'error_messages':error_messages}
            self.send_200_JSON(json.dumps(success_length), request_origin=request_origin)

        elif self.path == "/seesat":
            email_information = json_body["message"]["data"]
            email_history = urlsafe_b64decode(email_information).decode('utf-8')
            email_history = json.loads(email_history)
            print(email_history)
            print(google_email.get_email_history(email_history['historyId']))
            self.send_204(request_origin=request_origin)

        elif self.path == "/getObservationStations":
            try:
                if cookie_jwt is not False:
                    user_jwt = cookie_jwt
                else:
                    user_jwt = json_body["jwt"]
                decoded_jwt = decode_jwt(user_jwt)
                jwt_user_addr = decoded_jwt["address"]
            except Exception as e:
                print(e)
                pass
            if isValidEthereumAddress(jwt_user_addr) is False:
                self.send_400(message='Invalid Ethereum address', explain='Ethereum address pulled from user JWT is not valid', request_origin=request_origin)
                return
            try:
                observation_station_numbers = self.db.selectUserStationNumbers_JSON(jwt_user_addr)
                self.send_200_JSON(json.dumps(observation_station_numbers), request_origin=request_origin)
                return
            except Exception as e:
                print(e)
                self.send_500(message='Could not get station information', explain='Query to get observation stations has failed', request_origin=request_origin)

        elif self.path == '/generateStation':
            try:
                print(cookie_jwt)
                print(user_cookie)
                if cookie_jwt is not False:
                    user_jwt = cookie_jwt
                else:
                    user_jwt = json_body["jwt"]
                decoded_jwt = decode_jwt(user_jwt)
                user_addr = decoded_jwt["address"]
                station_name = json_body["station"]
                latitude = json_body["latitude"]
                longitude = json_body["longitude"]
                elevation = json_body["elevation"]
                notes = json_body["notes"]
            except Exception as e:
                print(e)
                self.send_400(message='Missing parameter(s)', explain='One or more of the required parameters are missing form the request body', request_origin=request_origin)
                return
            if isValidEthereumAddress(user_addr) is False:
                self.send_400(message='message', explain='explanation', request_origin=request_origin)
                return
            try:
                user_id = self.db.selectObserverIDFromAddress(user_addr)
                latest_station = self.db.selectLatestStationID()
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
                station_result = self.db.addStation(station_id, user_id, latitude, longitude, elevation, station_name, notes)
                if station_result is None:
                    self.send_500(message='Could not add station', explain='Query failed to add station for user', request_origin=request_origin)
                if station_result is False:
                    self.send_400(message='User has too many stations', explain='User has 10 or more stations', request_origin=request_origin)
                # get last station
                # increment station
                # remove O and I
                # set and return
                self.send_200_JSON(json.dumps({'station_id': station_id}), request_origin=request_origin)
                return
            except Exception as e:
                print(e)
                self.send_500(message='message', explain='explanation', request_origin=request_origin)
                return
            

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'')
            return

        self.db.clean()

httpd = ThreadingHTTPServer(('', PORT_NUMBER), SimpleHTTPRequestHandler)
httpd.timeout = 10

if os.getenv('TRUSAT_DISABLE_HTTPS', False):
  print('HTTPS disabled!')
else:
  httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='./privkey.pem', certfile='./fullchain.pem', server_side=True)

httpd.serve_forever()
