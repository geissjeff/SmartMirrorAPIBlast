from __future__ import print_function
from google_auth_oauthlib.flow import InstalledAppFlow
from apiclient.discovery import build
import datetime
import pickle
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CLIENT_ID ="671143266543-dnper0a5b777rkid7gh655od6130tj60.apps.googleusercontent.com"
CLIENT_SECRET ="2AazhFQju-1X8mjRqunuluv7"
REFRESH_TOKEN = "1/HOYF-y6yl2FOSkxME3m0POyp0mmvEbKBc5H_1DMCGxU"
credentials = None
client_config = {
    "installed": {
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "redirect_uris": "https://developers.google.com/oauthplayground",
        "client_id": CLIENT_ID,
        "client_secret":CLIENT_SECRET
    }
}
def initial():
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			credentials=pickle.load(token)
	else:
		flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
		credentials = flow.run_console()
		access_token = credentials.token
		refresh_token = credentials.refresh_token
		print("Access token: %s" % access_token) 
		with open('token.pickle', 'wb') as token:
		    pickle.dump(credentials, token)
	print("Access Token: %s" % credentials.token)
	service = build('calendar', 'v3', credentials = credentials)
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


def after():
	credentials = Credentials(
		None,
		refresh_token = REFRESH_TOKEN,
		token_uri = "https://accounts.google.com/o/oauth2/token",
		client_id = CLIENT_ID,
		client_secret = CLIENT_SECRET
	)
	access_token = credentials.token
	print("Access token: %s" % access_token) 
	service = build('calendar', 'v3', credentials = credentials)
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


def calendar_api():
	service = build('calendar', 'v3', credentials = credentials)
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
def main():
	#if (access_token is NULL):
	initial()
	#else:
#	after()
#	calendar_api()

if __name__ == '__main__':
    main()
