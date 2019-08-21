from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
from io import BytesIO
import json
import secrets
import datetime
import jwt

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

        elif self.path == "/priority-json":
            print("Priority-JSON")
            json_object = db.selectGlobalPriorities_JSON()
            print(json_object)
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
        

        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'HI JOHN')


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
            public_address_count = db.getObserverCountByID(public_address=json_body["publicAddress"])
            random_number = secrets.randbits(16)
            response_message = '{"nonce":\"%s\"}' % random_number
            print('public address count: ' + str(public_address_count[0]))
            if public_address_count[0] == None or public_address_count[0] == 0:
                # New User
                print("new user")
                db.addObserver(json_body["publicAddress"], "NULL", 0, "NULL")
                db.updateObserverNonce(nonce=random_number, public_address=json_body["publicAddress"])
            elif public_address_count[0] >= 1:
                # Old User
                print("old user")
                db.updateObserverNonce(nonce=random_number, public_address=json_body["publicAddress"])
            response_body = bytes(response_message, 'utf-8')

        ### LOGIN ENDPOINT ###
        elif self.path == "/login":
            print('login')
            old_nonce = db.getObserverNonce(json_body["publicAddress"])
            print(old_nonce[0])
            nonce = str(old_nonce[0]).encode('utf-8')
            message_hash = sha3.keccak_256(nonce).hexdigest()
            message_hash = encode_defunct(hexstr=message_hash)
            print("hashed messaged: " + str(message_hash))
            print(json_body["signedMessage"])
            print("public address: " + json_body["publicAddress"])
            try:
                signed_public_key = Account.recover_message(message_hash, signature=json_body["signedMessage"])
                #signed_public_key = w3.eth.account.recoverHash(str(message_hash), signature=json_body["signedMessage"])
                print("recovered address: " + signed_public_key)
            except:
                print('message could not be checked')
            if signed_public_key.lower() == json_body["publicAddress"].lower():
                key = nonce
                encoded_jwt = jwt.encode({'some':'payload'}, key, algorithm='HS256')
                db.updateObserverJWT(encoded_jwt, key, json_body["publicAddress"])
                response_message = b'{"jwt":"'
                response_message += encoded_jwt
                response_message += b'"}'
                response_body = response_message
            else:
                print("public key is incorrect")
                response_body = bytes('{}', 'utf-8')

        ### PROFILE ENDPOINT ###
        elif self.path == "/profile":
            user_profile = {
                    "user_name": "Filler_McFiller",
                    "user_image": "https://i.amz.mshcdn.com/KCJWkZNiwPyNXPcV0CN7yeL8G0A=/fit-in/1200x9600/https%3A%2F%2Fblueprint-api-production.s3.amazonaws.com%2Fuploads%2Fcard%2Fimage%2F784551%2F0e3defde-7d59-4d94-b094-51d187f930da.jpg",
                    "location": "Filler, FI",
                    "observation_count": "9001",
                    "objects_tracked": "1",
                    "avg_quality_level": "80%",
                    "bio": "Filler filly fill fill",
                    "objects_observed": [],
                    "observation_history": []
                }

            object_observed = {
                    "object_name": "Filler",
                    "object_origin": "Filler",
                    "object_type": "Filler",
                    "object_primary_purpose": "Filler",
                    "object_secondary_purpose": "Filler",
                    "observation_count": "0",
                    "time_last_tracked": "0",
                    "address_last_tracked": "0x0",
                    "username_last_tracked": "Filler_McFiller"
                }

            observation_history = {
                    "time_submitted": "0",
                    "object_name": "Filler",
                    "right_ascension": "Filler",
                    "declanation": "Filler",
                    "brightness": "0.0",
                    "conditions": "Filler"
                }
            user_jwt = json_body["jwt"]
            user_addr = json_body["eth_addr"]
            credentials = db.getObserverJWT(user_addr)
            if credentials[0][0] == user_jwt:
                print(user_jwt)

        elif self.path == '/email':
            to = json_body['to']
            message_text = json_body['payload']
            google_email.send_email(to, message_text)

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write()
            return


        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response_body)

httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
#httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='./privkey.pem', certfile='./fullchain.pem', server_side=True)
httpd.serve_forever()
