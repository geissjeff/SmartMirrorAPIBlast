from __future__ import print_function
import datetime
import pickle
import os.path
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI, client
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CLIENT_ID = "671143266543-nhnrjkgvu64edkahkiv9edmit3l0uqhq.apps.googleusercontent.com" 
CLIENT_SECRET = "_IhQ7c8vY4sLQo8CJXxL8KX0" 
REFRESH_TOKEN = "1/HOYF-y6yl2FOSkxME3m0POyp0mmvEbKBc5H_1DMCGxU"

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            #creds = flow.run_local_server()
            creds = client.GoogleCredentials(
                access_token = None,
                client_id = CLIENT_ID, 
                client_secret = CLIENT_SECRET, 
                refresh_token = REFRESH_TOKEN,
                token_expiry = None,
                token_uri = GOOGLE_TOKEN_URI,
                user_agent = None,
                revoke_uri = GOOGLE_REVOKE_URI)
            creds.refresh(httplib2.Http())
            http = creds.authorize(httplib2.Http())
            

        # Save the credentials for the next run
        #with open('token.pickle', 'wb') as token:
        #    pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()



#Refresh token: 1/HOYF-y6yl2FOSkxME3m0POyp0mmvEbKBc5H_1DMCGxU
