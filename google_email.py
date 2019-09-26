from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from email.mime.text import MIMEText
import base64



def create_message(sender, to, subject, message_text):
    message_text = 'Save this email: TruSat account recovery info for ' + to + '\n\n' + \
      'To log into TruSat, you\'ll need your password AND this secret code:\n\n' + message_text + \
      '\n\nThis email is the only time we can send you this code. TruSat cannot restore your account or reset your password for you. Please save this email forever and make a note of the password you used.\n\n' + \
      'Why do we do it this way? Read more\n\n' + \
      'Questions? Please email: Support@TruSat.org'
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



def send_email(to, message_text):
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    creds = None

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

    send_message(service, 'me', message_to_send)













def create_recovery_message(sender, to, subject, message_text):
    message_text = 'Please use the following link to verify your ownership of the following email:\n' + to + '\nIf you did not request recovery of your account please contact us at: Support@TruSat.org\n' + message_text + '\nThis link will expire in 30 minutes.'
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8'))}


def send_recovery_email(to, message_text):
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    creds = None

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

    send_message(service, 'me', message_to_send)
    






def get_email_history(history_id):
    SCOPES = [#'https://www.googleapis.com/auth/gmail.send',
            'https://www.googleapis.com/auth/gmail.readonly']#,
            #'https://www.googleapis.com/auth/gmail.metadata',
            #'https://mail.google.com']

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
    try:
        history = (service.users().history().list(userId='me', startHistoryId=history_id-10).execute())
        changes = history['history'] if 'history' in history else []
        try:
            message = service.users().messages().get(UserId='me', id=changes[0]["messages"]["id"]).execute()
        except:
            message = None
        return (changes, history, message)
    except Exception as e:
        print(e)
        return []
