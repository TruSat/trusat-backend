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

def encode_jwt(addr):
    with open('unsafe_private.pem', 'r') as file:
        private_key = file.read()
    private_rsa_key = load_pem_private_key(bytes(private_key, 'utf-8'), password=None, backend=default_backend())
    encoded_jwt = encode({'address':addr}, private_rsa_key, algorithm='RS256')
    return encoded_jwt

def decode_jwt(user_jwt):
    print(user_jwt)
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

    def send_500(self):
        self.send_response(500)
        self.db.clean()

    def send_400(self):
        self.send_response(400)
        self.db.clean()

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
            parameters = self.path.split('?')[1]
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
            except:
                self.send_500()
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_500()
                return
        
        elif path == "/catalog/undisclosed":
            try:
                json_object = self.db.selectCatalog_Undisclosed_JSON()
            except:
                self.send_500()
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_500()
                return

        elif path == "/catalog/debris":
            try:
                json_object = self.db.selectCatalog_Debris_JSON()
            except:
                self.send_500()
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_500()
                return

        elif path == "/catalog/latest":
            try:
                json_object = self.db.selectCatalog_Latest_JSON()
            except:
                self.send_500()
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_500()
                return

        elif path == "/catalog/all":
            try:
                json_object = self.db.selectCatalog_All_JSON()
            except:
                self.send_500()
                return
            if json_object is not False:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_500()
                return

        elif path == "/tle/trusat_all.txt":
            try:
                two_line_elements = self.db.selectTLE_all()
            except:
                self.send_500()
                return
            if two_line_elements is not False:
                self.send_200_text_cache(two_line_elements)
            else:
                self.send_500()
                return

        elif path == "/tle/trusat_priorities.txt":
            try:
                two_line_elements = self.db.selectTLE_priorities()
            except:
                self.send_500()
                return
            if two_line_elements is not False:
                self.send_200_text_cache(two_line_elements)
            else:
                self.send_500()
                return

        elif path == "/tle/trusat_high_confidence.txt":
            try:
                two_line_elements = self.db.selectTLE_high_confidence()
            except:
                self.send_500()
                return
            if two_line_elements is not False:
                self.send_200_text_cache(two_line_elements)
            else:
                self.send_500()
                return

        elif path == "/astriagraph":
            try:
                tles_json = self.db.selectTLE_Astriagraph()
            except:
                self.send_500()
                return
            if tle_json is not False:
                self.send_200_text_cache(tles_json)
            else:
                self.send_500()
                return

        elif path == "/profile":
            try:
                user_addr = parameters_map["address"]
            except Exception as e:
                print("PROFILE EXCEPTION")
                print(e)
                self.send_400()
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
            try:
                norad_number = parameters_map['norad_number']
            except:
                self.send_400()
                return
            try:
                json_object = self.db.selectObjectInfluence_JSON(norad_number)
            except:
                self.send_500()
                return
            if json_object:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_500()
                return

        elif path == '/object/info':
            try:
                norad_number = parameters_map['norad_number']
            except:
                self.send_400()
                return
            try:
                json_object = self.db.selectObjectInfo_JSON(norad_number)
            except:
                self.send_500()
                return
            if json_object:
                self.send_200_JSON_cache(json_object)
            else:
                self.send_500()
                return

        elif path == '/object/history':
            try:
                norad_number = parameters_map['norad_number']
                year = parameters_map["year"]
            except Exception as e:
                print(e)
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
            except:
                self.send_500()
                return

        elif path == '/object/userSightings':
            try:
                norad_number = parameters_map['norad_number']
                public_address = parameters_map['address']
            except:
                self.send_400()
                return
            try:
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
            except:
                self.send_500()
                return

        elif path == "/tle/object":
            try:
                norad_number = parameters_map["norad_number"]
            except:
                self.send_400()
                return
            try:
                two_line_elements = self.db.selectTLE_single(norad_number)
            except:
                self.send_500()
                return
            if two_line_elements:
                self.send_200_text_cache(two_line_elements)
            else:
                self.send_500()
                return

        elif path == "/findObject":
            try:
                object_name = parameters_map["objectName"]
            except:
                self.send_400()
                return
            try:
                object_name = int(object_name)
            except Exception as e:
                print(e)
            try:
                objects = self.db.selectFindObject(object_name)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Cache-Control', 'max-age=300')
                self.end_headers()
                self.wfile.write(bytes(objects, 'utf-8'))
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
        except:
            self.send_400()
            return

        ### GET NONCE ENDPOINT ###
        if self.path == "/getNonce":
            try:
                addr = json_body["address"]
            except:
                self.send_400()
                return
            try:
                public_address_count = self.db.getObserverCountByID(public_address=addr)
            except:
                self.send_500()
                return
            random_number = secrets.randbits(16)
            response_message = '{"nonce":\"%s\"}' % random_number
            if public_address_count[0] == None or public_address_count[0] == 0:
                # New User
                try:
                    self.db.addObserver(addr, "NULL", 0, "NULL")
                    self.db.updateObserverNonce(nonce=random_number, public_address=addr)
                except:
                    self.send_500()
                    return
            elif public_address_count[0] >= 1:
                # Old User
                try:
                    self.db.updateObserverNonce(nonce=random_number, public_address=addr)
                except:
                    self.send_500()
                    return
            response_body = bytes(response_message, 'utf-8')

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)


        elif self.path == "/signup":
            try:
                addr = json_body["address"]
                old_nonce = self.db.getObserverNonce(addr)
                email = json_body["email"]
                signed_message = json_body["signedMessage"]
                payload = json_body["secret"]
            except:
                self.send_400()
                return
            nonce = str(old_nonce[0]).encode('utf-8')
            self.db.updateObserverNonce(nonce=0, public_address=addr)
            message_hash = sha3.keccak_256(nonce).hexdigest()
            message_hash = encode_defunct(hexstr=message_hash)
            try:
                signed_public_key = Account.recover_message(message_hash, signature=signed_message)
            except:
                print('message could not be checked')
            if signed_public_key.lower() == addr.lower():
                email_from_addr = self.db.selectEmailFromObserverAddress(addr)
                if email_from_addr == None or email_from_addr == '' or email_from_addr == b'NULL':
                    if email != None or email != 'null' or email != 'NULL' or email != '':
                        try:
                            self.db.updateObserverEmail(email, addr)
                            google_email.send_email(email, payload)
                            self.send_response(204)
                            return
                        except Exception as e:
                            print(e)
                            self.send_500()
                            return
            else:
                print("public key is incorrect")
                self.send_400()
                return
            self.send_500()
            return


        ### LOGIN ENDPOINT ###
        elif self.path == "/login":
            try:
                addr = json_body["address"]
                old_nonce = self.db.getObserverNonce(addr)
                signed_message = json_body["signedMessage"]
            except:
                self.send_400()
                return
            try:
                email = json_body["email"]
                secret = json_body["secret"]
            except:
                email = None
            nonce = str(old_nonce[0]).encode('utf-8')
            self.db.updateObserverNonce(nonce=0, public_address=addr)
            message_hash = sha3.keccak_256(nonce).hexdigest()
            message_hash = encode_defunct(hexstr=message_hash)
            try:
                signed_public_key = Account.recover_message(message_hash, signature=signed_message)
            except:
                print('message could not be checked')
            if signed_public_key.lower() == addr.lower():
                email_from_addr = self.db.selectEmailFromObserverAddress(addr)
                if email_from_addr == None or email_from_addr == '' or email_from_addr == b'NULL':
                    if email != None:
                        try:
                            self.db.updateObserverEmail(email, addr)
                            google_email.send_email(email, secret)
                            self.send_response(204)
                            return
                        except Exception as e:
                            print(e)
                            self.send_500()
                            return
                with open('unsafe_private.pem', 'r') as file:
                    private_key = file.read()
                private_rsa_key = load_pem_private_key(bytes(private_key, 'utf-8'), password=None, backend=default_backend())
                encoded_jwt = encode({'address':addr.lower()}, private_rsa_key, algorithm='RS256')
                self.db.updateObserverJWT(encoded_jwt, '', addr)
                response_message = b'{"jwt":"'
                response_message += encoded_jwt
                response_message += b'"}'
                response_body = response_message
            else:
                print("public key is incorrect")
                self.send_400()
                return
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == "/editProfile":
            try:
                user_jwt = json_body["jwt"]
                decoded_jwt = decode_jwt(user_jwt)
                public_address = decoded_jwt["address"]
            except:
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
                    
        elif self.path == '/claimAccount':
            try:
                email = json_body['email']
            except:
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
                            'exp': datetime.utcnow() + timedelta(1800)
                        }
                    encoded_jwt = encode(jwt_payload, private_rsa_key, algorithm='RS256')
                    self.db.updateObserverPassword(encoded_jwt.decode('utf-8'), results.decode('utf-8'))
                    google_email.send_recovery_email(email, 'http://trusat.org/claim/' + encoded_jwt.decode('utf-8'))
            except:
                self.send_500()
                return
            self.send_response(204)

        elif self.path == "/verifyClaimAccount":
            try:
                message_text = json_body["secret"]
                address = json_body["address"]
                user_jwt = json_body["jwt"]
            except:
                self.send_400()
                return
            #Lookup number and old address
            try:
                decoded_jwt = decode_jwt(user_jwt)
                print("Secret")
                secret = decoded_jwt["secret"]
                print("email")
                to = decoded_jwt["email"]
                print("post email")
                old_address = self.db.selectObserverAddressFromPassword(user_jwt).decode('utf-8')
                #replace address
                encoded_jwt = encode_jwt(address)
                self.db.updateObserverAddress(address, old_address)
                print(old_address)
                print(address)
                google_email.send_email(to, message_text)
                self.db.updateObserverJWT(encoded_jwt, "", json_body["address"])
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
                self.send_500()
                return

        elif self.path == '/emailSecret':
            try:
                to = json_body['to']
                message_text = json_body['payload']
            except:
                self.send_400()
                return
            try:
                google_email.send_email(to, message_text)
            except:
                self.send_500()
                return
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'{}')

        elif self.path == "/submitObservation":
            try:
                user_jwt = json_body["jwt"]
                decoded_jwt = decode_jwt(user_jwt)
                user_addr = decoded_jwt["address"]
            except:
                self.send_400()
                return
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
            except Exception as e:
                print(e)
            parsed_iod = []
            try:
                multiple = json_body["multiple"]
                try:
                    parsed_iod = iod.parse_iod_lines(multiple)
                    if len(parsed_iod):
                        for item in multiple.split('\n'):
                            temp_iod = iod.parse_iod_lines(item)
                            it += 1
                            if temp_iod:
                                removed_iods[it] = False
                            else:
                                error_messages.append("Observation on line {} did not match IOD format.".format(it))
                                removed_iods[it] = True
                except:
                    print("Not IOD")
                if not parsed_iod:
                    try:
                        parsed_iod = iod.parse_uk_lines(multiple)
                        if len(parsed_iod):
                            for item in multiple.split('\n'):
                                temp_iod = iod.parse_uk_lines(item)
                                it += 1
                                if temp_iod:
                                    removed_iods[it] = False
                                else:
                                    error_messages.append("Observation on line {} did not match UK format.".format(it))
                                    removed_iods[it] = True
                    except:
                        print("Not UK")
                if not parsed_iod:
                    try:
                        parsed_iod = iod.parse_rde_record(multiple)
                        if len(parsed_iod):
                            rde_multiple = multiple.split('\n')
                            for i in range(0, len(parsed_iod)-2):
                                temp_iod = iod.parse_rde_record("{}\n{}\n{}".format(rde_multiple[i], rde_multiple[i+1], rde_multiple[i+2]))
                                it += 1
                                if temp_iod:
                                    i += 2
                                    removed_iods[it] = False
                                    removed_iods[it+1] = False
                                    removed_iods[it+2] = False
                                    it += 2
                                else:
                                    error_messages.append("Observation on line {} did not match RDE format.".format(it))
                                    removed_iods[it] = True
                            #check each line as starting point and roll through parsing
                            #After all this chaos, go ahead and try to add it to the db

                    except:
                        print("Not RDE")
                submission_time = datetime.now()
                it = 0
                #one at a time, line up the items in parsed_iod so they can be checked against the original array of observations, otherwise the numbers returned back won't be aligned with the original lines
                for entry in parsed_iod:
                    it += 1
                    individual_entry = []
                    individual_entry.append(entry)
                    entry_value = self.db.addParsedIOD(individual_entry, user_addr, submission_time)
                    success += entry_value[0]
                    while removed_iods[it] == True:
                        it += 1
                    if entry_value[0] == 0:
                        error_messages.append("Observation on line {} has already been submitted.".format(it))
            except Exception as e:
                error_messages.append("Could not determine observation format.")
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
            print(email_history)
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
