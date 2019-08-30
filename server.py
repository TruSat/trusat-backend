from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
from io import BytesIO
import json
import secrets
import datetime
import jwt
import copy
from jwt import encode
from datetime import datetime

from eth_account import Account
from eth_account.messages import defunct_hash_message, encode_defunct
import sha3

import database
import google_email

PORT_NUMBER = 8080

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        f = open('login.txt', 'r')
        lines = f.readlines()
        db_name = lines[0].strip()
        db_type = lines[1].strip()
        endpoint = lines[2].strip()
        username = lines[3].strip()
        password = lines[4].strip()
        f.close()
        db = database.Database(db_name, db_type, endpoint, username, password)

        if self.path == "/mostRecent":
            print("Homepage")
            community_recent_query = {}
            community_recent_query['community_observations'] = []
            try:
                recent_observations = db.getRecentObservations()
                print(recent_observations)
            except:
                print("only latest observation")
            for tup in recent_observations:
                entry = {
                    "object_name": "Filler",
                    "object_origin": "Filler",
                    "object_type": "Filler",
                    "object_purpose": "Filler",
                    "time_last_tracked": tup[7].decode('utf-8'),
                    "address_last_tracked": "filler",
                    "username_last_tracked": tup[2].decode('utf-8')
                    }
                community_recent_query["community_observations"].append(entry)
            response_body = bytes(json.dumps(community_recent_query), 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)
            
        elif self.path == "/priority":
            print("Priority")
            community_priority_query = {}
            community_priority_query['community_observations'] = []
            try:
                recent_observations = db.selectGlobalPriorities()
                print(recent_observations)
            except:
                print("only latest observation")
            for tup in recent_observations:
                entry = {
                    "object_name": tup[1],
                    "object_origin": tup[2],
                    "object_type": tup[3],
                    "object_purpose": tup[4],
                    "time_last_tracked": tup[5].timestamp(),
                    "address_last_tracked": "filler",
                    "username_last_tracked": tup[6]
                    }
                community_priority_query["community_observations"].append(entry)
            response_body = bytes(json.dumps(community_priority_query), 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == "/catalog/priorities":
            json_object = db.selectCatalog_Priorities_JSON()
            response_body = bytes(json_object, 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)
        
        elif self.path == "/catalog/undisclosed":
            json_object = db.selectCatalog_Undisclosed_JSON()
            response_body = bytes(json_object, 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == "/catalog/debris":
            json_object = db.selectCatalog_Debris_JSON()
            response_body = bytes(json_object, 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == "/catalog/latest":
            json_object = db.selectCatalog_Latest_JSON()
            response_body = bytes(json_object, 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == "/catalog/all":
            json_object = db.selectCatalog_All_JSON()
            response_body = bytes(json_object, 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == "/tle/trusat_all.txt":
            two_line_elements = db.selectTLE_all()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes(two_line_elements, 'utf-8'))

        elif self.path == "/tle/trusat_priorities.txt":
            two_line_elements = db.selectTLE_priorities()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes(two_line_elements, 'utf-8'))

        elif self.path == "/tle/trusat_high_confidence.txt":
            two_line_elements = db.selectTLE_high_confidence()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes(two_line_elements, 'utf-8'))

        elif self.path == "/astriagraph":
            tles_json = db.selectTLE_Astriagraph()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes(tles_json, 'utf-8'))

        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'HI JOHN')
        db.clean()


    def do_POST(self):
        response_body = b""
        signed_public_key = '0'

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        f = open('login.txt', 'r')
        lines = f.readlines()
        db_name = lines[0].strip()
        db_type = lines[1].strip()
        endpoint = lines[2].strip()
        username = lines[3].strip()
        password = lines[4].strip()
        f.close()
        db = database.Database(db_name, db_type, endpoint, username, password)
        try:
            db.createTables()
        except:
            print("Tables already exist")
        try:
            json_body = json.loads(body)
        except:
            print('json could not be parsed')

        ### GET NONCE ENDPOINT ###
        if self.path == "/getNonce":
            print('getNonce')
            public_address_count = db.getObserverCountByID(public_address=json_body["address"])
            random_number = secrets.randbits(16)
            response_message = '{"nonce":\"%s\"}' % random_number
            if public_address_count[0] == None or public_address_count[0] == 0:
                # New User
                print("new user")
                db.addObserver(json_body["address"], "NULL", 0, "NULL")
                db.updateObserverNonce(nonce=random_number, public_address=json_body["address"])
            elif public_address_count[0] >= 1:
                # Old User
                print("old user")
                db.updateObserverNonce(nonce=random_number, public_address=json_body["address"])
            response_body = bytes(response_message, 'utf-8')

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        ### LOGIN ENDPOINT ###
        elif self.path == "/login":
            print('login')
            old_nonce = db.getObserverNonce(json_body["address"])
            print(old_nonce[0])
            nonce = str(old_nonce[0]).encode('utf-8')
            message_hash = sha3.keccak_256(nonce).hexdigest()
            message_hash = encode_defunct(hexstr=message_hash)
            print("hashed messaged: " + str(message_hash))
            print(json_body["signedMessage"])
            print("public address: " + json_body["address"])
            try:
                signed_public_key = Account.recover_message(message_hash, signature=json_body["signedMessage"])
                #signed_public_key = w3.eth.account.recoverHash(str(message_hash), signature=json_body["signedMessage"])
                print("recovered address: " + signed_public_key)
            except:
                print('message could not be checked')
            if signed_public_key.lower() == json_body["address"].lower():
                key = nonce
                encoded_jwt = encode({'some':'payload'}, key, algorithm='HS256')
                db.updateObserverJWT(encoded_jwt, key, json_body["address"])
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
            public_address = json_body["address"]
            user_jwt = json_body["jwt"]
            print(json_body)
            print(json_body["email"])
            if db.getObserverJWT(public_address)[0].decode("utf-8") == user_jwt:
                try:  
                    username = json_body["username"]
                    db.updateObserverUsername(username, public_address)
                except Exception as e:
                    print("Username not being updated")
                    print(e)
                try:
                    email = json_body["email"]
                    db.updateObserverEmail(email, public_address)
                except Exception as e:
                    print("Email not being updated")
                    print(e)
                try:
                    bio = json_body["bio"]
                    db.updateObserverBio(bio, public_address)
                except Exception as e:
                    print("Bio not being updated")
                    print(e)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)
                    

        ### PROFILE ENDPOINT ###
        elif self.path == "/profile":
            objects_observed_json = json.loads(db.selectObjectsObserved_JSON())
            observation_history_json = json.loads(db.selectObservationHistory_JSON())
            user_jwt = json_body["jwt"]
            user_addr = json_body["address"]
            credentials = db.getObserverJWT(user_addr)
            user_profile = db.selectProfileInfo_JSON(user_addr)
            user_profile_json = json.loads(user_profile)
            user_profile_json["objects_observed"] = objects_observed_json
            user_profile_json["observation_history"] = observation_history_json
            if credentials[0].decode("utf-8") == user_jwt:
                response_body = bytes(json.dumps(user_profile_json), 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == '/emailSecret':
            to = json_body['to']
            message_text = json_body['payload']
            google_email.send_email(to, message_text)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == '/object/influence':
            norad_number = json_body['norad_number']
            object_influence = [
                {
                    "observation_time": "1550398277",
                    "username": "Leo Barhorst",
                    "user_address": "0x1863a72A0244D603Dcd00CeD99b94d517207716a",
                    "user_location": "Brooklyn, USA",
                    "observation_quality": "34",
                    "time_difference": "1.42",
                    "weight": "33"
                },
                {
                    "observation_time": "1550398277",
                    "username": "Jim Smith",
                    "user_address": "0x1863a72A0244D603Dcd00CeD99b94d517207716a",
                    "user_location": "Los Angeles, USA",
                    "observation_quality": "45",
                    "time_difference": "1.42",
                    "weight": "33"
                },
                {
                    "observation_time": "1550398277",
                    "username": "Joe Bloggs",
                    "user_address": "0x1863a72A0244D603Dcd00CeD99b94d517207716a",
                    "user_location": "London, UK",
                    "observation_quality": "20",
                    "time_difference": "1.42",
                    "weight": "33"
                }
                ]
            response_body = bytes(db.selectObjectInfluence_JSON(norad_number), 'utf-8')
            #response_body = bytes(json.dumps(object_influence), 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == '/object/info':
            norad_number = json_body['norad_number']
            object_info = db.selectObjectInfo_JSON(norad_number)
            print(norad_number)
            response_body = bytes(object_info, 'utf-8')
            print(object_info)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == '/object/history':
            norad_number = json_body['norad_number']
            year = json_body['year']
           # object_history = db.selectObjectHistory_summary(norad_number)
           # response_body = bytes(json.dumps(object_history), 'utf-8')
            year = json_body["year"]
            month = json_body["month"]
            real_entry = db.selectObjectHistoryByMonth_JSON(norad_number, year, month)
            real_response = []
            internals = {
                "date": 0,
                "observation": []
            }
            new_internals = copy.deepcopy(internals)
            for items in real_entry:
                items = json.loads(items)
                date = datetime.fromtimestamp(float(items["observation_time"])).day
                if date == new_internals["date"]:
                    new_internals["observation"].append(items)
                else:
                    if new_internals["date"] != 0:
                        real_response.append(new_internals)
                    new_internals = copy.deepcopy(internals)
                    new_internals["date"] = date
                    new_internals["observation"].append(items)
            if new_internals["date"] != 0:
                real_response.append(new_internals)
            response_body = bytes(json.dumps(real_response), 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == '/object/userSightings':
            norad_number = json_body['norad_number']
            user_jwt = json_body['jwt']
            public_address = json_body['address']
            object_user_sightings = [
                    {
                        "observation_time": "1550398277",
                        "username": "Leo Barhorst",
                        "user_location": "Brooklyn, USA",
                        "observation_quality": "34",
                        "observation_time_difference": "1.42",
                        "weight": "10"
                    },
                    {
                        "username": "Leo Barhorst",
                        "user_location": "Brooklyn, USA",
                        "observation_quality": "34",
                        "observation_time_difference": "1.42",
                        "weight": "1"
                    },
                    {
                        "username": "Leo Barhorst",
                        "user_location": "Brooklyn, USA",
                        "quality": "20",
                        "time_difference": "1.42",
                        "weight": "0"
                    }
                ]
            print(user_jwt)
            tmp = db.selectObjectUserSightings_JSON(norad_number, public_address)
            response_body = bytes(tmp, 'utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_body)

        elif self.path == "/tle/object":
            norad_number = json_body["norad_number"]
            two_line_elements = db.selectTLE_single(norad_number)
            print(two_line_elements)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            try:
                self.wfile.write(bytes(two_line_elements), 'utf-8')
            except:
                self.wfile.write(b'')

        elif self.path == "/findObject":
            object_name = json_body["objectName"]
            objects = db.selectFindObject(object_name)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            try:
                self.wfile.write(bytes(objects, 'utf-8'))
            except Exception as e:
                try:
                    self.wfile.write(bytes(db.selectFindObject(int(object_name)), 'utf-8'))
                except:
                    print('numbers not working either')
                    self.wfile.write(b'[]')
                print(e)

        elif self.path == "/submitObservation":
            user_jwt = json_body["jwt"]
            #TODO: FIX THIS, I NEED NEW ADDRESS FLOW NOW!
            try:
                single = json_body["single"]
            except Exception as e:
                print(e)
            try:
                multiple = json_body["multiple"]
            except Exception as e:
                print(e)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'')

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'')
            return

        db.clean()

httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='./privkey.pem', certfile='./fullchain.pem', server_side=True)
httpd.serve_forever()
