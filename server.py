from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json
import secrets
import datetime
import jwt

from eth_account import Account
from eth_account.messages import defunct_hash_message, encode_defunct
import sha3

import database

PORT_NUMBER = 8080

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        db = database.Database('Astrana.db', 'sqlite', "NULL", "NULL", "NULL")

        if self.path == "/mostRecent":
            print("Homepage")
            community_recent_query = {}
            community_recent_query['community_observations'] = []
            recent_observations = db.getRecentObservations()
            try:
                recent_observations = db.getRecentObservations()
            except:
                print("only latest observation")
            for tup in recent_observations:
                entry = {
                    "object_name": "Filler",
                    "object_type": "Filler",
                    "user_name": tup[2],
                    "time_stamp": datetime.datetime(tup[7], 
                        tup[8],
                        tup[9],
                        tup[10],
                        tup[11],
                        tup[12],
                        tup[13]).timestamp(),
                    "object_number": tup[0],
                    "international_designation": tup[4]
                    }
                community_recent_query["community_observations"].append(entry)
            response_body = bytes(json.dumps(community_recent_query), 'utf-8')
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
        db = database.Database('Astrana.db')
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
            random_number = secrets.randbits(64)
            response_message = '{"nonce":\"%s\"}' % random_number
            if public_address_count == 0:
                # New User
                print("new user")
                db.addObserver(json_body["publicAddress"], "NULL", "NULL", "NULL")
                db.updateObserverNonce(nonce=random_number, public_address=json_body["publicAddress"])
            if public_address_count == 1:
                # Old User
                print("old user")
                db.updateObserverNonce(nonce=random_number, public_address=json_body["publicAddress"])
            response_body = bytes(response_message, 'utf-8')

        ### LOGIN ENDPOINT ###
        elif self.path == "/login":
            print('login')
            old_nonce = db.getObserverNonce(json_body["publicAddress"])
            print(old_nonce[0])
            nonce = old_nonce[0].encode('utf-8')
            message_hash = sha3.keccak_256(nonce).hexdigest()
            message_hash = encode_defunct(hexstr=message_hash)
            print("hashed messaged: " + str(message_hash))
            print(json_body["signedMessage"])
            print("public address: " + json_body["publicAddress"])
            signed_public_key = Account.recover_message(message_hash, signature=json_body["signedMessage"])
            try:
                signed_public_key = Account.recover_message(message_hash, signature=json_body["signedMessage"])
                #signed_public_key = w3.eth.account.recoverHash(str(message_hash), signature=json_body["signedMessage"])
                print("recovered address: " + signed_public_key)
            except:
                print('message could not be checked')
            if signed_public_key.lower() == json_body["publicAddress"].lower():
                #jwt
                print("jwt")
                key = nonce
                encoded_jwt = jwt.encode({'some':'payload'}, key, algorithm='HS256')
                db.updateObserverJWT(encoded_jwt, key, json_body["publicAddress"])
                response_message = b'{"jwt":'
                response_message += encoded_jwt
                response_message += b'}'
                response_body = response_message
            else:
                print("public key is incorrect")
                response_body = bytes('{}', 'utf-8')

        elif self.path == "/userHomepage":
            print("Homepage")
            community_recent_query = {}
            community_recent_query['community_observations'] = []
            try:
                recent_observations = db.getRecentObservations()
            except:
                print("only latest observation")
            for tup in recent_observations:
                entry = {
                    "object_name": "Filler",
                    "object_type": "Filler",
                    "user_name": tup[1],
                    "time_stamp": datetime.datetime(tup[6], 
                        tup[7],
                        tup[8],
                        tup[9],
                        tup[10],
                        tup[11],
                        tup[12]).timestamp(),
                    "object_number": tup[0],
                    "international_designation": tup[3]
                    }
                community_recent_query["community_observations"].append(entry)
            response_body = bytes(json.dumps(community_recent_query), 'utf-8')

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response_body)

httpd = HTTPServer(('', 8081), SimpleHTTPRequestHandler)
httpd.serve_forever()
