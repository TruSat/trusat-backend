from http.server import ThreadingHTTPServer,  HTTPServer, BaseHTTPRequestHandler
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

import database
import google_email


PORT_NUMBER = 8080

# TODO: Enforce all external variables obey strict definitions

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
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.search(regex, email)

def isValidSecret(secret):
    regex = '^([0-9]{1,10})([\/])([0-9, a-f]{32})([\/])([0-9,a-f]{160})$'
    return re.search(regex, secret)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
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

    def send_500(self):
        self.send_response(500)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.db.clean()

    def send_400(self):
        self.send_response(400)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.db.clean()

    def send_401(self):
        self.send_response(401)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.db.clean()

    def send_404(self):
        self.send_response(404)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.db.clean()

    def send_204(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def send_200_JSON(self, body_data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        try:
            body_bytes = bytes(body_data, 'utf-8')
        except Exception as e:
            print(e)
            body_bytes = b'[]'
        self.wfile.write(body_bytes)

    def send_200_JSON2(self, body_data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body_data)

    def send_200_JSON_cache(self, body_data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'max-age=300')
        self.end_headers()
        try:
            body_bytes = bytes(body_data, 'utf-8')
        except Exception as e:
            print(e)
            body_bytes = b'[]'
        self.wfile.write(body_bytes)

    def send_200_text(self, body_data):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        try:
            body_bytes = bytes(body_data, 'utf-8')
        except Exception as e:
            print(e)
            body_bytes = b''
        self.wfile.write(body_bytes)

    def send_200_text_cache(self, body_data):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
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
                path == "/findObject":
            self.send_response(200)
            self.send_header('Accept', 'GET')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Headers', 'Cache-Control')
            self.end_headers()
        else:
            self.send_404()

    def do_GET(self):
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
                self.send_500()
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_200_JSON_cache(json.dumps({}))
                return
        
        elif path == "/catalog/undisclosed":
            try:
                json_object = self.db.selectCatalog_Undisclosed_JSON()
            except Exception as e:
                print(e)
                self.send_500()
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_200_JSON_cache(json.dumps({}))
                return

        elif path == "/catalog/debris":
            try:
                json_object = self.db.selectCatalog_Debris_JSON()
            except Exception as e:
                print(e)
                self.send_500()
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_200_JSON_cache(json.dumps({}))
                return

        elif path == "/catalog/latest":
            try:
                json_object = self.db.selectCatalog_Latest_JSON()
            except Exception as e:
                print(e)
                self.send_500()
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_200_JSON_cache(json.dumps({}))
                return

        elif path == "/catalog/all":
            try:
                json_object = self.db.selectCatalog_All_JSON()
            except Exception as e:
                print(e)
                self.send_500()
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_200_JSON_cache(json.dumps({}))
                return

        elif path == "/tle/trusat_all.txt":
            try:
                two_line_elements = self.db.selectTLE_all()
            except Exception as e:
                print(e)
                self.send_500()
                return
            if two_line_elements is not False:
                self.send_200_text_cache(two_line_elements)
            else:
                self.send_200_text_cache('')
                return

        elif path == "/tle/trusat_priorities.txt":
            try:
                two_line_elements = self.db.selectTLE_priorities()
            except Exception as e:
                print(e)
                self.send_500()
                return
            if two_line_elements is not False:
                self.send_200_text_cache(two_line_elements)
            else:
                self.send_200_text_cache('')
                return

        elif path == "/tle/trusat_high_confidence.txt":
            try:
                two_line_elements = self.db.selectTLE_high_confidence()
            except Exception as e:
                print(e)
                self.send_500()
                return
            if two_line_elements is not False:
                self.send_200_text_cache(two_line_elements)
            else:
                self.send_200_text_cache('')
                return

        elif path == "/astriagraph":
            try:
                tles_json = self.db.selectTLE_Astriagraph()
            except Exception as e:
                print(e)
                self.send_500()
                return
            if tles_json is not False:
                self.send_200_text_cache(tles_json)
            else:
                self.send_200_text_cache('')
                return

        elif path == "/profile":
            jwt_user_addr = ''
            try:
                user_addr = parameters_map["address"]
            except Exception as e:
                print(e)
                self.send_400()
                return
            if isValidEthereumAddress(user_addr) is False:
                self.send_400()
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
                self.send_500()
                return
            try:
                user_jwt = parameters_map["jwt"]
                decoded_jwt = decode_jwt(user_jwt)
                jwt_user_addr = decoded_jwt["address"]
            except Exception as e:
                print(e)
                pass
            if isValidEthereumAddress(jwt_user_addr) is False:
                self.send_400()
                return
            if jwt_user_addr.lower() == user_addr.lower():
                try:
                    observation_station_numbers = self.db.selectUserStationNumbers_JSON(user_addr)
                    for station in observation_station_numbers:
                        user_profile_json["observation_stations"].append(station["station_number"])
                except Exception as e:
                    print(e)
                    self.send_500()
                    return

            for k,v in user_profile_json.items():
                if v == None or v =='NULL':
                    user_profile_json[k] = ""
            user_profile = json.dumps(user_profile_json)

            self.send_200_JSON_cache(user_profile)

        elif path == '/object/influence':
            try:
                norad_number = parameters_map['norad_number']
            except Exception as e:
                print(e)
                self.send_400()
                return
            if isValidNoradNumber(norad_number) is False:
                self.send_400()
                return
            try:
                json_object = self.db.selectObjectInfluence_JSON(norad_number)
            except Exception as e:
                print(e)
                self.send_500()
                return
            if json_object:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_200_JSON(json.dumps({}))
                return

        elif path == '/object/info':
            try:
                norad_number = parameters_map['norad_number']
            except Exception as e:
                print(e)
                self.send_400()
                return
            if isValidNoradNumber(norad_number) is False:
                self.send_400()
                return
            try:
                json_object = self.db.selectObjectInfo_JSON(norad_number)
            except Exception as e:
                print(e)
                self.send_500()
                return
            if json_object:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_200_JSON_cache(json.dumps({}))
                return

        elif path == '/object/history':
            try:
                norad_number = parameters_map['norad_number']
                year = parameters_map["year"]
                int_year = int(year)
            except Exception as e:
                print(e)
                self.send_400()
                return
            if (isValidNoradNumber(norad_number) is False or
                int_year < 1957 or
                int_year > datetime.now().year):
                self.send_400()
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
                self.send_200_JSON_cache(response_body)
            except Exception as e:
                print(e)
                self.send_500()
                return

        elif path == '/object/userSightings':
            response_body = []
            try:
                norad_number = parameters_map['norad_number']
                user_jwt = parameters_map['jwt']
                decoded_jwt = decode_jwt(user_jwt)
                public_address = decoded_jwt["address"]
            except Exception as e:
                print(e)
                self.send_400()
                return
            if (isValidNoradNumber(norad_number) is False or
                isValidEthereumAddress is False):
                self.send_400()
                return
            try:
                response_body = self.db.selectObjectUserSightings_JSON(norad_number, public_address)
                response_body = json.dumps(response_body)
                self.send_200_JSON_cache(response_body)
            except Exception as e:
                print(e)
                self.send_500()
                return

        elif path == "/tle/object":
            try:
                norad_number = parameters_map["norad_number"]
            except Exception as e:
                print(e)
                self.send_400()
                return
            if isValidNoradNumber(norad_number) is False:
                self.send_400()
                return
            try:
                two_line_elements = self.db.selectTLE_single(norad_number)
            except Exception as e:
                print(e)
                self.send_500()
                return
            if two_line_elements:
                self.send_200_text_cache(two_line_elements)
            else:
                self.send_200_text_cache("")
                return

        elif path == "/findObject":
            try:
                object_name = parameters_map["objectName"]
            except Exception as e:
                print(e)
                self.send_400()
                return
            try:
                object_name = int(object_name)
            except Exception as e:
                print(e)
            try:
                objects = self.db.selectFindObject(object_name)
                self.send_200_text_cache(objects)
            except Exception as e:
                self.send_500()
                print(e)
                return

        else:
            self.send_response(404)
        self.db.clean()


    def do_POST(self):
        response_body = b""
        signed_public_key = '0'

        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            json_body = json.loads(body)
        except Exception as e:
            print(e)
            self.send_400()
            return

        ### GET NONCE ENDPOINT ###
        if self.path == "/getNonce":
            try:
                addr = json_body["address"]
            except Exception as e:
                print(e)
                self.send_400()
                return
            if isValidEthereumAddress(addr) is False:
                self.send_400()
                return
            try:
                email = json_body["email"]
                if isValidEmailAddress is False:
                    self.send_400()
                    return
                results = self.db.selectObserverAddressFromEmail(email)
                if len(results) == 42:
                    self.send_200_JSON(json.dumps({}))
                    return
            except Exception as e:
                print(e)
                pass

            try:
                public_address_count = self.db.getObserverCountByID(public_address=addr)
            except Exception as e:
                print(e)
                self.send_500()
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
                    self.send_500()
                    return
            elif public_address_count[0] >= 1:
                # Old User
                try:
                    self.db.updateObserverNonceBytes(nonce=random_number, public_address=addr)
                except Exception as e:
                    print(e)
                    self.send_500()
                    return
            self.send_200_JSON(response_message)

        elif self.path == "/signup":
            try:
                # TODO: put timeout on email sending and verify payload isn't malicious
                addr = json_body["address"]
                if isValidEthereumAddress(addr) is False:
                    self.send_400()
                    return
                old_nonce = self.db.getObserverNonceBytes(addr)
                email = json_body["email"]
                signed_message = json_body["signedMessage"]
                payload = json_body["secret"]
            except Exception as e:
                print(e)
                self.send_400()
                return

            if (isValidEmailAddress(email) is False or
                isValidSecret(payload) is False):
                self.send_400()
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
            if signed_public_key.lower() == addr.lower():
                email_from_addr = self.db.selectEmailFromObserverAddress(addr)
                if email_from_addr == None or email_from_addr == '' or email_from_addr == b'NULL':
                    if email != None or email != 'null' or email != 'NULL' or email != '':
                        try:
                            self.db.updateObserverEmail(email, addr)
                            email_status = google_email.send_email(email, payload)
                            if email_status == False:
                                self.send_500()
                                return
                            self.send_200_JSON(json.dumps({'result': True}))
                            return
                        except Exception as e:
                            print(e)
                            self.send_500()
                            return
            else:
                self.send_400()
                return
            self.send_500()
            return


        ### LOGIN ENDPOINT ###
        elif self.path == "/login":
            try:
                addr = json_body["address"]
                old_nonce = self.db.getObserverNonceBytes(addr)
                signed_message = json_body["signedMessage"]
            except Exception as e:
                print(e)
                self.send_400()
                return
            if isValidEthereumAddress(addr) is False:
                self.send_400()
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
                self.send_400()
                return
            if signed_public_key.lower() == addr.lower():
                email_from_addr = self.db.selectEmailFromObserverAddress(addr)
                if email_from_addr == None or email_from_addr == '' or email_from_addr == b'NULL':
                    if email != None:
                        try:
                            self.db.updateObserverEmail(email, addr)
                            email_status = google_email.send_email(email, secret)
                            if email_status == False:
                                self.send_500()
                                return
                            self.send_200_JSON(json.dumps({'result':True}))
                            return
                        except Exception as e:
                            print(e)
                            self.send_500()
                            return
                encoded_jwt = encode_jwt(addr.lower())
                self.db.updateObserverJWT(encoded_jwt, '', addr)
                response_message = b'{"jwt":"'
                response_message += encoded_jwt
                response_message += b'"}'
                self.send_200_JSON2(response_message)
            else:
                print("Login Failed")
                self.send_400()
                return

        elif self.path == "/editProfile":
            try:
                user_jwt = json_body["jwt"]
                decoded_jwt = decode_jwt(user_jwt)
                public_address = decoded_jwt["address"]
            except Exception as e:
                print(e)
                self.send_400()
                return
            if isValidEthereumAddress(public_address) is False:
                self.send_400()
                return
            if self.db.getObserverJWT(public_address)[0].decode("utf-8") == user_jwt:
                try:  
                    username = json_body["username"]
                    if username != "null" and username != None:
                        self.db.updateObserverUsername(username, public_address)
                except Exception as e:
                    print("Username not being updated")
                    print(e)
                try:
                    email = json_body["email"]
                    if isValidNoradNumber(norad_number):
                        self.db.updateObserverEmail(email, public_address)
                except Exception as e:
                    print("Email not being updated")
                    print(e)
                try:
                    bio = json_body["bio"]
                    if bio != "null" and bio != None:
                        self.db.updateObserverBio(bio, public_address)
                except Exception as e:
                    print("Bio not being updated")
                    print(e)
                try:
                    location = json_body["location"]
                    if location != "null" and location != None:
                        self.db.updateObserverLocation(location, public_address)
                except Exception as e:
                    print("Location not being updated")
                    print(e)
            self.send_200_JSON(response_body)
                    
        elif self.path == '/claimAccount':
            try:
                email = json_body['email']
            except Exception as e:
                print(e)
                self.send_400()
                return
            if isValidEmailAddress(email) is False:
                self.send_400()
                return
            try:
                with open('unsafe_private.pem', 'r') as file:
                    private_key = file.read()
                private_rsa_key = load_pem_private_key(bytes(private_key, 'utf-8'), password=None, backend=default_backend())
                results = self.db.selectObserverAddressFromEmail(email)
                if results != None:
                    number = str(secrets.randbits(64))
                    jwt_payload = {
                            'email': email,
                            'secret': number,
                            'exp': datetime.utcnow() + timedelta(minutes=30)
                        }
                    encoded_jwt = encode(jwt_payload, private_rsa_key, algorithm='RS256')
                    self.db.updateObserverPassword(encoded_jwt.decode('utf-8'), results.decode('utf-8'))
                    # TODO: Check that the password has expired before sending another email
                    email_status = google_email.send_recovery_email(email, 'http://trusat.org/claim/' + encoded_jwt.decode('utf-8'))
                    if email_status == False:
                        self.send_500()
                        return
                else:
                    self.send_200_JSON(json.dumps({'result': False}))
                    return
            except Exception as e:
                print(e)
                self.send_500()
                return
            self.send_200_JSON(json.dumps({'result': True}))

        elif self.path == "/verifyClaimAccount":
            try:
                message_text = json_body["secret"]
                address = json_body["address"]
                user_jwt = json_body["jwt"]
            except Exception as e:
                print(e)
                self.send_400()
                return
            if (isValidEthereumAddress(address) is False or
                isValidSecret(message_text) is False):
                self.send_400()
                return
            #Lookup number and old address
            try:
                decoded_jwt = decode_jwt(user_jwt)
                secret = decoded_jwt["secret"]
                to = decoded_jwt["email"]
                old_address = self.db.selectObserverAddressFromPassword(user_jwt).decode('utf-8')
                
                #replace address
                encoded_jwt = encode_jwt(address)
                self.db.updateObserverAddress(address, old_address)
                email_status = google_email.send_email(to, message_text)
                if email_status == False:
                    self.send_500()
                    return
                self.db.updateObserverJWT(encoded_jwt, "", json_body["address"])
                response_message = b'{"jwt":"'
                response_message += encoded_jwt
                response_message += b'"}'
                response_body = response_message

                self.send_200_JSON2(response_body)
                self.db.updateObserverPassword('NULL', results.decode('utf-8'))
            except Exception as e:
                print(e)
                self.send_500()
                return

        elif self.path == "/submitObservation":
            try:
                user_jwt = json_body["jwt"]
                decoded_jwt = decode_jwt(user_jwt)
                user_addr = decoded_jwt["address"]
            except Exception as e:
                print(e)
                self.send_400()
                return
            if isValidEthereumAddress(user_addr) is False:
                self.send_400()
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
                    self.send_500()
                    return
            except Exception as e:
                print(e)
                self.send_500()
                return
            success_length = {'success':success, 'error_messages':error_messages}
            self.send_200_JSON(json.dumps(success_length))

        elif self.path == "/seesat":
            email_information = json_body["message"]["data"]
            email_history = urlsafe_b64decode(email_information).decode('utf-8')
            email_history = json.loads(email_history)
            print(email_history)
            print(google_email.get_email_history(email_history['historyId']))
            self.send_204()

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'')
            return

        self.db.clean()

httpd = ThreadingHTTPServer(('', PORT_NUMBER), SimpleHTTPRequestHandler)

if os.getenv('TRUSAT_DISABLE_HTTPS', False):
  print('HTTPS disabled!')
else:
  httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='./privkey.pem', certfile='./fullchain.pem', server_side=True)

httpd.serve_forever()
