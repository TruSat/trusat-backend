from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from email.mime.text import MIMEText
import base64
from time import sleep

import threading
import logging
import database


def init_email_sending():
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    creds = None

    try:
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_console()
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)
        return True
    except Exception as e:
        print(e)
        return False




def stop_history_watch():
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    creds = None
    try:
        if os.path.exists('history_token.pickle'):
            with open('history_token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_console()
            with open('history_token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)

        results = service.users().stop(userId='me').execute()
        print(results)
        return True
    except Exception as e:
        print(e)
        return False




def init_history_watch():
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    creds = None
    try:
        if os.path.exists('history_token.pickle'):
            with open('history_token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_console()
            with open('history_token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        request = {
                'labelIds': ['Label_4696745878389955477'],
                'topicName': 'projects/trusat-256517/topics/TruSat'
            }
        service = build('gmail', 'v1', credentials=creds)


        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])
                print(label['id'])


        results = service.users().watch(userId='me', body=request).execute()
        print(results)
        return True
    except Exception as e:
        print(e)
        return False


def create_message(sender, to, subject, message_text):
    message_text = 'Save this email: TruSat account recovery info for ' + to + '\n\n' + \
      'To log into TruSat, you\'ll need your password AND this secret code:\n\n' + message_text + \
      '\n\nThis email is the only time we can send you this code. TruSat cannot reset your password for you. Please save this email forever and make a note of the password you used.\n\n' + \
      'Login here: trusat.org/login\n\n' + \
      'Why do we do it this way? Read more (trusat.org/faq)\n\n' + \
      'Questions? Please email: Help@Beta.TruSat.org'
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8'))}

def send_message(service, user_id, message):
    message["raw"] = message["raw"].decode('utf-8')
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        return message
    except Exception as error:
        print('An error occurred: %s' % error)
        return False



def send_email(to, message_text):
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    creds = None

    try:
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_console()
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)

        message_to_send = create_message('kenan.oneal@consensys.net', to, 'TruSat - Save this email: Recovery Info', message_text)

        sent_message = send_message(service, 'me', message_to_send)
        if sent_message == False:
            return False
        return True
    except:
        return False













def create_recovery_message(sender, to, subject, message_text):
    message_text = 'Please use the following link to verify your ownership of the following email ' + \
        to + '\n\n' + message_text + '\nThis link will expire in 30 minutes.' + \
        '\n\nIf you did not request recovery of your account please contact us at:\nHelp@Beta.TruSat.org\n'
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8'))}


def send_recovery_email(to, message_text):
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    creds = None

    try:
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_console()
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)

        message_to_send = create_recovery_message('kenan.oneal@consensys.net', to, 'TruSat - Recover Account', message_text)

        sent_message = send_message(service, 'me', message_to_send)
        if sent_message == False:
            return False
        return True
    except:
        return False
    






def get_email_history(history_id):
    thread_to_use = threading.Thread(target=wait_for_email, args=(history_id,))
    thread_to_use.start()
    return history_id

def wait_for_email(history_id):
    sleep(600)

    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    creds = None

    if os.path.exists('history_token.pickle'):
        with open('history_token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_console()
        with open('history_token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    CONFIG = os.path.abspath("../../trusat-config.yaml")
    db = database.Database(CONFIG)

    try:
        history = (service.users().history().list(userId='me', startHistoryId=history_id).execute())
        changes = history['history'] if 'history' in history else []
        try:
            change_id = []
            messages = []
            for i in changes:
                tmp_id = i['messages'][0]['id'] if 'messages' in i else ''
                if tmp_id != '':
                    change_id.append(tmp_id)
            if len(change_id) != 0:
                for i in change_id:
                    try:
                        message = service.users().messages().get(userId='me', id=i).execute()
                        for label in message['labelIds']:
                            if label == 'Label_4696745878389955477':
                                messages.append(message['snippet'])
                                for j in message["payload"]["parts"]:
                                    if j["mimeType"] == "text/plain":
                                        email_body_base64 = j["body"]["data"]
                                        email_body = base64.urlsafe_b64decode(email_body_base64).decode('utf-8')
                                        body = email_body.replace('\r\n', '\n')
                                        (success, errors) = db.addObserverParsedIOD(body)
                                        print("SUCCESS")
                                        print(success)
                                        print("ERRORS")
                                        print(errors)
                                for j in message["payload"]["headers"]:
                                    if j["name"] == "From":
                                        email_from_unparsed = j["value"]
                                        email_from = email_from_unparsed.split("\u003c")[1].split("\u003e")[0]
                                    elif j["name"] == "To":
                                        email_to_unparsed = j["value"]
                                        email_to = email_to_unparsed.split("\u003c")[1].split("\u003e")[0]
                                    elif j["name"] == "Date":
                                        email_timestamp = j["value"]
                    except Exception as e:
                        print(e)
                        pass

            else:
                messages = []
        except Exception as e:
            print(e)
            messages = None
        db.clean()
        return messages
    except Exception as e:
        print(e)
        db.clean()
        return []
