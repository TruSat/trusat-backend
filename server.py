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

# Use the database module from our sister repo. We assume it is installed alongside this repo.
import sys
sys.path.insert(1,"../sathunt-database")
import database
import google_email

# The following 7 lines are necessary until the iod module is public
import inspect
import os
import sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
iod_path = os.path.join(parentdir, "trusat-iod")
sys.path.insert(1,iod_path)
import iod

PORT_NUMBER = 8080

def encode_jwt(user_jwt, addr):
    with open('unsafe_private.pem', 'r') as file:
        private_key = file.read()
    private_rsa_key = load_pem_private_key(bytes(private_key, 'utf-8'), password=None, backend=default_backend())
    encoded_jwt = encode({'address':addr}, private_rsa_key, algorithm='RS256')
    return encoded_jwt

def decode_jwt(user_jwt):
    with open('public.pem', 'r') as file:
        public_key = file.read()
    public_rsa_key = load_pem_public_key(bytes(public_key,'utf-8'), backend=default_backend())
    decoded_jwt = decode(user_jwt, public_rsa_key, algorithms='RS256')
    return decoded_jwt

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

    def send_200_text_tle(self, body_data):
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
        print('PATH IS:')
        print(self.path)
        self.send_response(200)
        self.send_header('Accept', 'GET')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Cache-Control')
        self.end_headers()

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
            json_object = self.db.selectCatalog_Priorities_JSON()
            self.send_200_JSON_cache(json_object)
        
        elif path == "/catalog/undisclosed":
            json_object = self.db.selectCatalog_Undisclosed_JSON()
            self.send_200_JSON_cache(json_object)

        elif path == "/catalog/debris":
            json_object = self.db.selectCatalog_Debris_JSON()
            self.send_200_JSON_cache(json_object)

        elif path == "/catalog/latest":
            json_object = self.db.selectCatalog_Latest_JSON()
            self.send_200_JSON_cache(json_object)

        elif path == "/catalog/all":
            json_object = self.db.selectCatalog_All_JSON()
            self.send_200_JSON_cache(json_object)

        elif path == "/tle/trusat_all.txt":
            two_line_elements = self.db.selectTLE_all()
            self.send_200_text_tle(two_line_elements)

        elif path == "/tle/trusat_priorities.txt":
            two_line_elements = self.db.selectTLE_priorities()
            self.send_200_text_tle(two_line_elements)

        elif path == "/tle/trusat_high_confidence.txt":
            two_line_elements = self.db.selectTLE_high_confidence()
            self.send_200_text_tle(two_line_elements)

        elif path == "/astriagraph":
            tles_json = self.db.selectTLE_Astriagraph()
            self.send_200_text_tle(tles_json)

        elif path == "/profile":
            try:
                user_addr = parameters_map["address"]
            except Exception as e:
                print("PROFILE EXCEPTION")
                print(e)
                self.send_response(400)
                return
            #user_jwt = json_body["jwt"]
            #try:
            #    user_addr = json_body["addresss"]
            #except:
            #    try:
            #        user_addr = json_body["address"]
            #    except:
            #        decoded_jwt = decode_jwt(user_jwt)
            #        user_addr = decoded_jwt["address"]

            #try:
            #    with open('public.pem', 'r') as file:
            #        public_key = file.read()
            #    public_rsa_key = load_pem_public_key(bytes(public_key,'utf-8'), backend=default_backend())
            #    decoded_jwt = decode(user_jwt, public_rsa_key, algorithms='RS256')
            #    decoded_addr = decoded_jwt["address"]
            #except:
            #    print("need to update the jwt for user")






            #try:
            #    user_addr = json_body["address"]
            #except:
            #    try:
            #        user_addr = db.getObserverFromJWT(user_jwt)
            #    except:
            #        self.send_response(418)
            #        self.send_header('Content-type', 'applicaiton/json')
            #        self.send_header('Access-Control-Allow-Origin', '*')
            #        self.end_headers()
            #        self.wfile.write(b'{}')
            #        return
            objects_observed_json = self.db.selectUserObjectsObserved_JSON(user_addr)
            observation_history_json = self.db.selectUserObservationHistory_JSON(user_addr)
            #credentials = self.db.getObserverJWT(user_addr)
            observation_station_numbers = self.db.selectUserStationNumbers_JSON(user_addr)
            user_profile_json = self.db.selectProfileInfo_JSON(user_addr)
            user_profile_json["observation_stations"] = []
            for station in observation_station_numbers:
                user_profile_json["observation_stations"].append(station["station_number"])
            user_profile_json["objects_observed"] = objects_observed_json
            user_profile_json["observation_history"] = observation_history_json
            user_profile_json["public_username"] = False
            user_profile_json["public_location"] = False
            #if credentials[0].decode("utf-8") == user_jwt:
            #    response_body = bytes(json.dumps(user_profile_json), 'utf-8')
            for k,v in user_profile_json.items():
                if v == None or v =='NULL':
                    user_profile_json[k] = ""
            user_profile = json.dumps(user_profile_json)

            self.send_200_JSON_cache(user_profile)

        elif path == '/object/influence':
            norad_number = parameters_map['norad_number']
            json_object = self.db.selectObjectInfluence_JSON(norad_number)
            self.send_200_JSON_cache(json_object)

        elif path == '/object/info':
            norad_number = parameters_map['norad_number']
            json_object = self.db.selectObjectInfo_JSON(norad_number)
            self.send_200_JSON_cache(json_object)

        elif path == '/object/history':
            norad_number = parameters_map['norad_number']
            year = None
            try:
                year = parameters_map["year"]
            except Exception as e:
                print(e)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'[]')
                return
            real_entry = self.db.selectObjectHistoryByMonth_JSON(norad_number, year)
            year_response = {}
            real_response = []
            internals = {
                "date": 0,
                "observation": []
            }
            prev_month_string = "January"
            month_string = "January"
            new_real_response = copy.deepcopy(real_response)
            new_internals = copy.deepcopy(internals)
            for items in real_entry:
                timestamp = datetime.fromtimestamp(float(items["observation_time"]))
                month_string = timestamp.strftime("%B")
                date = timestamp.day
                if date == new_internals["date"]:
                    items["observation_quality"] = secrets.randbits(7)
                    new_internals["observation"].append(items)
                else:
                    if new_internals["date"] != 0:
                        new_real_response.append(new_internals)
                    new_internals = copy.deepcopy(internals)
                    new_internals["date"] = date
                    items["observation_quality"] = secrets.randbits(7)
                    new_internals["observation"].append(items)
                if prev_month_string != month_string:
                    year_response[prev_month_string] = copy.deepcopy(new_real_response)
                    new_real_response = copy.deepcopy(real_response)
                    prev_month_string = month_string
            if new_internals["date"] != 0:
                new_real_response.append(new_internals)
            year_response[month_string] = new_real_response
            response_body = json.dumps(year_response)
            self.send_200_JSON_cache(response_body)

        elif path == '/object/userSightings':
            norad_number = parameters_map['norad_number']

            public_address = parameters_map['address']
            #user_jwt = json_body['jwt']
            #decoded_jwt = decode_jwt(user_jwt)
            #try:
            #    public_address = decoded_jwt["address"]
            #except:
            #    self.send_response(403)
            #    self.end_headers()
            #    self.wfile.write(b'')
            #    return

            response_body = self.db.selectObjectUserSightings_JSON(norad_number, public_address)
            self.send_200_JSON_cache(response_body)

        elif path == "/tle/object":
            norad_number = parameters_map["norad_number"]
            two_line_elements = self.db.selectTLE_single(norad_number)
            self.send_200_text(two_line_elements)

        elif path == "/findObject":
            object_name = parameters_map["objectName"]
            try:
                object_name = int(object_name)
            except Exception as e:
                print(e)
            objects = self.db.selectFindObject(object_name)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'max-age=300')
            self.end_headers()
            try:
                self.wfile.write(bytes(objects, 'utf-8'))
            except Exception as e:
                self.wfile.write(b'[]')
                print(e)

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'')
        self.db.clean()


    def do_POST(self):
        response_body = b""
        signed_public_key = '0'

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        #try:
        #    self.db.createTables()
        #except:
        #    print("Tables already exist")
        try:
            json_body = json.loads(body)
        except:
            print('json could not be parsed:' + str(body))
            return

        ### GET NONCE ENDPOINT ###
        if self.path == "/getNonce":
            public_address_count = self.db.getObserverCountByID(public_address=json_body["address"])
            random_number = secrets.randbits(16)
            response_message = '{"nonce":\"%s\"}' % random_number
            if public_address_count[0] == None or public_address_count[0] == 0:
                # New User
                self.db.addObserver(json_body["address"], "NULL", 0, "NULL")
                self.db.updateObserverNonce(nonce=random_number, public_address=json_body["address"])
            elif public_address_count[0] >= 1:
                # Old User
                self.db.updateObserverNonce(nonce=random_number, public_address=json_body["address"])
            response_body = bytes(response_message, 'utf-8')

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        ### LOGIN ENDPOINT ###
        elif self.path == "/login":
            old_nonce = self.db.getObserverNonce(json_body["address"])
            email = json_body["email"]
            nonce = str(old_nonce[0]).encode('utf-8')
            message_hash = sha3.keccak_256(nonce).hexdigest()
            message_hash = encode_defunct(hexstr=message_hash)
            try:
                signed_public_key = Account.recover_message(message_hash, signature=json_body["signedMessage"])
            except:
                print('message could not be checked')
            if signed_public_key.lower() == json_body["address"].lower():
                print(email)
                if email != None:
                    self.db.updateObserverEmail(email, json_body["address"])
                with open('unsafe_private.pem', 'r') as file:
                    private_key = file.read()
                private_rsa_key = load_pem_private_key(bytes(private_key, 'utf-8'), password=None, backend=default_backend())
                encoded_jwt = encode({'address':json_body["address"].lower()}, private_rsa_key, algorithm='RS256')
                db.updateObserverJWT(encoded_jwt, '', json_body["address"])
                response_message = b'{"jwt":"'
                response_message += encoded_jwt
                response_message += b'"}'
                response_body = response_message
            else:
                print("public key is incorrect")
                response_body = bytes('{}', 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == "/editProfile":
            #public_address = json_body["address"]
            user_jwt = json_body["jwt"]
            decoded_jwt = decode_jwt(user_jwt)
            public_address = decoded_jwt["address"]
            if db.getObserverJWT(public_address)[0].decode("utf-8") == user_jwt:
                try:  
                    username = json_body["username"]
                    if username != "null" and username != None:
                        self.db.updateObserverUsername(username, public_address)
                except Exception as e:
                    print("Username not being updated")
                    print(e)
                try:
                    email = json_body["email"]
                    if email != "null" and email != None:
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
                try:
                    public_location = json_body["public_location"]
                    if public_location != "null" and public_location != None:
                        self.db.updateObserverPublicLocation(public_location, public_address)
                except Exception as e:
                    print("Location flag could not be found")
                    print(e)
                try:
                    public_username = json_body["public_username"]
                    if public_username != "null":
                        self.db.updateObserverPublicUsername(public_username, public_username)
                except Exception as e:
                    print("Username flag could not be found")
                    print(e)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)
                    

        ### PROFILE ENDPOINT ###
        elif self.path == "/profile":
            user_jwt = json_body["jwt"]
            try:
                user_addr = json_body["addresss"]
            except:
                try:
                    user_addr = json_body["address"]
                except:
                    decoded_jwt = decode_jwt(user_jwt)
                    user_addr = decoded_jwt["address"]

            try:
                with open('public.pem', 'r') as file:
                    public_key = file.read()
                public_rsa_key = load_pem_public_key(bytes(public_key,'utf-8'), backend=default_backend())
                decoded_jwt = decode(user_jwt, public_rsa_key, algorithms='RS256')
                decoded_addr = decoded_jwt["address"]
            except:
                print("need to update the jwt for user")
            #try:
            #    user_addr = json_body["address"]
            #except:
            #    try:
            #        user_addr = db.getObserverFromJWT(user_jwt)
            #    except:
            #        self.send_response(418)
            #        self.send_header('Content-type', 'applicaiton/json')
            #        self.send_header('Access-Control-Allow-Origin', '*')
            #        self.end_headers()
            #        self.wfile.write(b'{}')
            #        return
            objects_observed_json = self.db.selectUserObjectsObserved_JSON(user_addr)
            observation_history_json = self.db.selectUserObservationHistory_JSON(user_addr)
            #credentials = self.db.getObserverJWT(user_addr)
            observation_station_numbers = self.db.selectUserStationNumbers_JSON(user_addr)
            user_profile_json = self.db.selectProfileInfo_JSON(user_addr)
            user_profile_json["observation_stations"] = []
            for station in observation_station_numbers:
                user_profile_json["observation_stations"].append(station["station_number"])
            user_profile_json["objects_observed"] = objects_observed_json
            user_profile_json["observation_history"] = observation_history_json
            user_profile_json["public_username"] = False
            user_profile_json["public_location"] = False
            #if credentials[0].decode("utf-8") == user_jwt:
            #    response_body = bytes(json.dumps(user_profile_json), 'utf-8')
            for k,v in user_profile_json.items():
                if v == None or v =='NULL':
                    user_profile_json[k] = ""
            user_profile = json.dumps(user_profile_json)
            response_body = bytes(user_profile, 'utf-8')

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'max-age=2')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == '/claimAccount':
            email = json_body['email']
            with open('unsafe_private.pem', 'r') as file:
                private_key = file.read()
            private_rsa_key = load_pem_private_key(bytes(private_key, 'utf-8'), password=None, backend=default_backend())
            results = self.db.selectObserverAddressFromEmail(email)
            if results != None:
                number = str(secrets.randbits(64))
                jwt_payload = {
                        'email': email,
                        'secret': number,
                        'exp': datetime.utcnow() + timedelta(1800)
                    }
                encoded_jwt = encode(jwt_payload, private_rsa_key, algorithm='RS256')
                self.db.updateObserverPassword(encoded_jwt.decode('utf-8'), results.decode('utf-8'))
                google_email.send_recovery_email(email, 'http://trusat.consensys.space/claim/' + encoded_jwt.decode('utf-8'))
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'{}')

        elif self.path == "/verifyClaimAccount":
            message_text = json_body["secret"]
            address = json_body["address"]
            user_jwt = json_body["jwt"]
            print(user_jwt)
            #Lookup number and old address
            try:
                with open('public.pem', 'r') as file:
                    public_key = file.read()
                public_rsa_key = load_pem_public_key(bytes(public_key,'utf-8'), backend=default_backend())
                decoded_jwt = decode(user_jwt, public_rsa_key, algorithms='RS256')
                secret = decoded_jwt["secret"]
                to = decoded_jwt["email"]
                old_address = self.db.selectObserverAddressFromPassword(user_jwt).decode('utf-8')
                #replace address
                key = str(secrets.randbits(10))
                encoded_jwt = encode({'address':address}, key, algorithm='HS256')
                self.db.updateObserverAddress(address, old_address)
                print(old_address)
                print(address)
                google_email.send_email(to, message_text)
                self.db.updateObserverJWT(encoded_jwt, key, json_body["address"])
                response_message = b'{"jwt":"'
                response_message += encoded_jwt
                response_message += b'"}'
                response_body = response_message

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(response_body)
            except Exception as e:
                print(e)
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'{}')


        elif self.path == '/emailSecret':
            to = json_body['to']
            message_text = json_body['payload']
            google_email.send_email(to, message_text)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'{}')

        elif self.path == '/object/influence':
            norad_number = json_body['norad_number']
            json_object = self.db.selectObjectInfluence_JSON(norad_number)
            self.send_200_JSON(json_object)

        elif self.path == '/object/info':
            norad_number = json_body['norad_number']
            json_object = self.db.selectObjectInfo_JSON(norad_number)
            self.send_200_JSON(json_object)

        elif self.path == '/object/history':
            print(json_body)
            norad_number = json_body['norad_number']
            year = None
            try:
                year = json_body["year"]
            except Exception as e:
                print(e)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'[]')
                return
            real_entry = self.db.selectObjectHistoryByMonth_JSON(norad_number, year)
            year_response = {}
            real_response = []
            internals = {
                "date": 0,
                "observation": []
            }
            prev_month_string = "January"
            month_string = "January"
            new_real_response = copy.deepcopy(real_response)
            new_internals = copy.deepcopy(internals)
            for items in real_entry:
                timestamp = datetime.fromtimestamp(float(items["observation_time"]))
                month_string = timestamp.strftime("%B")
                date = timestamp.day
                if date == new_internals["date"]:
                    items["observation_quality"] = secrets.randbits(7)
                    new_internals["observation"].append(items)
                else:
                    if new_internals["date"] != 0:
                        new_real_response.append(new_internals)
                    new_internals = copy.deepcopy(internals)
                    new_internals["date"] = date
                    items["observation_quality"] = secrets.randbits(7)
                    new_internals["observation"].append(items)
                if prev_month_string != month_string:
                    year_response[prev_month_string] = copy.deepcopy(new_real_response)
                    new_real_response = copy.deepcopy(real_response)
                    prev_month_string = month_string
            if new_internals["date"] != 0:
                new_real_response.append(new_internals)
            year_response[month_string] = new_real_response
            response_body = bytes(json.dumps(year_response), 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'public')
            self.send_header('Cache-Control', 'max-age=300')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == '/object/userSightings':
            norad_number = json_body['norad_number']

            public_address = json_body['address']
            #user_jwt = json_body['jwt']
            #decoded_jwt = decode_jwt(user_jwt)
            #try:
            #    public_address = decoded_jwt["address"]
            #except:
            #    self.send_response(403)
            #    self.end_headers()
            #    self.wfile.write(b'')
            #    return

            tmp = self.db.selectObjectUserSightings_JSON(norad_number, public_address)
            response_body = bytes(tmp, 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == "/tle/object":
            norad_number = json_body["norad_number"]
            two_line_elements = self.db.selectTLE_single(norad_number)
            self.send_200_text(two_line_elements)

        elif self.path == "/findObject":
            object_name = json_body["objectName"]
            try:
                object_name = int(object_name)
            except Exception as e:
                print(e)
            objects = self.db.selectFindObject(object_name)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            try:
                self.wfile.write(bytes(objects, 'utf-8'))
            except Exception as e:
                self.wfile.write(b'[]')
                print(e)

        elif self.path == "/submitObservation":
            user_jwt = json_body["jwt"]
            decoded_jwt = decode_jwt(user_jwt)
            user_addr = decoded_jwt["address"]
            #user_addr = db.getObserverFromJWT(user_jwt)
            parsed_iod_array = []
            success = 0
            error_messages = []
            removed_iods = {}
            it = 0
            #credentials = db.getObserverJWT(user_addr)
            if user_addr == None:
                self.send_response(401)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'')
                return
            #TODO: FIX THIS, I NEED NEW ADDRESS FLOW NOW!
            try:
                single = json_body["single"]
                print(single)
            except Exception as e:
                print(e)
            try:
                multiple = json_body["multiple"]
                for item in multiple:
                    parsed_iod = iod.parse_iod_lines(item)
                    it += 1
                    print(parsed_iod)
                    if parsed_iod:
                        parsed_iod_array.append(parsed_iod)
                        removed_iods[it] = False
                    else:
                        error_messages.append("Observation on line {} did not match expected format.".format(it))
                        removed_iods[it] = True
                        
                submission_time = datetime.now()
                it = 0
                for entry in  parsed_iod_array:
                    it += 1
                    entry_value = self.db.addParsedIOD(entry, user_addr, submission_time)
                    success += entry_value[0]
                    while removed_iods[it] == True:
                        it += 1
                    error_messages.append("Observation on line {} has already been submitted.".format(it))
            except Exception as e:
                print(e)
            if success > 0:
                db.commit_IOD_db_writes();
            success_length = {'success':success, 'error_messages':error_messages}#len(parsed_iod_array)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(success_length),'utf-8'))

        elif self.path == "/seesat":
            email_information = json_body["message"]["data"]
            email_history = urlsafe_b64decode(email_information).decode('utf-8')
            email_history = json.loads(email_history)
            print(google_email.get_email_history(email_history['historyId']))
            self.send_response(204)
            self.end_headers()

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
