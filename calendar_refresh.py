#!/usr/bin/env python3.4
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
CLIENT_ID_2 = "410689799908-6ogc86thrntu23bh5fqp5765uk6a04jr.apps.googleusercontent.com"
CLIENT_ID_3 = "857837625781-bnpbqg04mr12d4lth9i90hsmiarak1us.apps.googleusercontent.com"
CLIENT_ID_4 = "421968015868-68rkco8i9dp3u7f0b7p1nejapnssf5o3.apps.googleusercontent.com"
CLIENT_SECRET ="2AazhFQju-1X8mjRqunuluv7"
CLIENT_SECRET_2 ="5xTTaVVr3fY_jGJrJCtx4IDT"
CLIENT_SECRET_3 ="CXEU5DXQqllYBmm3C6-4zueo"
CLIENT_SECRET_4 ="Tl-BUygEx8THB8sHtkK3gtgn"
REFRESH_TOKEN = "1/HOYF-y6yl2FOSkxME3m0POyp0mmvEbKBc5H_1DMCGxU"
#credentials = None
client_config = {
    "installed": {
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "redirect_uris": "https://developers.google.com/oauthplayground",
        "client_id": CLIENT_ID,
        "client_secret":CLIENT_SECRET
    }
}
client_config_2 = {
    "installed": {
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "redirect_uris": "https://developers.google.com/oauthplayground",
        "client_id": CLIENT_ID_2,
        "client_secret":CLIENT_SECRET_2
    }
}
client_config_3 = {
    "installed": {
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "redirect_uris": "https://developers.google.com/oauthplayground",
        "client_id": CLIENT_ID_3,
        "client_secret":CLIENT_SECRET_3
    }
}
client_config_4 = {
    "installed": {
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "redirect_uris": "https://developers.google.com/oauthplayground",
        "client_id": CLIENT_ID_4,
        "client_secret":CLIENT_SECRET_4
    }
}
def initial(profile):
	if(profile == '1'):
		if os.path.exists('token.pickle'):
			with open('token.pickle', 'rb') as token:
				credentials=pickle.load(token)
		else:
			flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
			credentials = flow.run_console()
			access_token = credentials.token
			refresh_token = credentials.refresh_token
			with open('token.pickle', 'wb') as token:
				pickle.dump(credentials, token)
	elif(profile == '2'):
		if os.path.exists('token2.pickle'):
			with open('token2.pickle', 'rb') as token:
				credentials=pickle.load(token)
		else:
			flow = InstalledAppFlow.from_client_config(client_config_2, SCOPES)
			credentials = flow.run_console()
			access_token = credentials.token
			refresh_token = credentials.refresh_token
			with open('token2.pickle', 'wb') as token:
				pickle.dump(credentials, token)
	elif(profile == '3'):
		if os.path.exists('token3.pickle'):
			with open('token3.pickle', 'rb') as token:
				credentials=pickle.load(token)
		else:
			flow = InstalledAppFlow.from_client_config(client_config_3, SCOPES)
			credentials = flow.run_console()
			access_token = credentials.token
			refresh_token = credentials.refresh_token
			with open('token3.pickle', 'wb') as token:
				pickle.dump(credentials, token)
	elif(profile == '4'):
		if os.path.exists('token4.pickle'):
			with open('token4.pickle', 'rb') as token:
				credentials=pickle.load(token)
		else:
			flow = InstalledAppFlow.from_client_config(client_config_4, SCOPES)
			credentials = flow.run_console()
			access_token = credentials.token
			refresh_token = credentials.refresh_token
			with open('token4.pickle', 'wb') as token:
			    pickle.dump(credentials, token)
	service = build('calendar', 'v3', credentials = credentials)
	now = datetime.datetime.utcnow().isoformat() +'Z'# 'Z' indicates UTC time
	print('Getting the upcoming 10 events')
	events_result = service.events().list(calendarId='primary', timeMin=now,
						maxResults=10, singleEvents=True,
						orderBy='startTime').execute()
	events = events_result.get('items', [])
	if not events:
		print('No upcoming events found.')
	for event in events:
		start = event['start']# event['start'].get('date'))
		if(start.get('date') != None):
			print(start.get('date'), event['summary'])
		else:
			startDate = start.get('dateTime').strip().split('-')
			startTime = startDate[2].strip().split('T')
			print("{}-{}-{}: {} {}".format(startDate[0], startDate[1], startTime[0], startTime[1],event['summary']))

def main():
	profile = input("Enter number of profile\n")
	initial(profile)

if __name__ == '__main__':
    main()

