from __future__ import print_function
import requests
#import serial
import time
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

def serialTest():
	serialport = serial.Serial(port = "/dev/ttyAMA0",
				 baudrate=9600,parity=serial.PARITY_NONE,
				 stopbits=serial.STOPBITS_ONE,
				 bytesize=serial.EIGHTBITS,timeout=3.0)

	while(~rcv):
	#	serialport.write("Hello World")
		rcv = serialport.read(8)
		print(repr(rcv))
		time.sleep(1)
	return rcv

def openWeather():
	weather_API_key = "a0e157b3a341bfe1935ccc52588ae003"
	weather_base_url = "http://api.openweathermap.org/data/2.5/weather?"
	weather_zip_code = "47906"				#input("Enter a Zip code: ")
	weather_Final_zip_url = weather_base_url + "appid=" + weather_API_key + "&zip=" + weather_zip_code
	weather_data = requests.get(weather_Final_zip_url).json()
	temp = weather_data["main"]["temp"]
	description = weather_data["weather"][0]["description"]
	tempF = 9*(temp - 273)/5 + 32
	name = weather_data["name"]
	print("Temperature in", name,":", tempF, "degrees F")
	print("Description in", name,":", description, "\n")

def news():
	news_base_url = "https://newsapi.org/v2/top-headlines?"
	news_API_Key = "04296e8f713f454990ac3eaf6b88d19f"
	country = "us"#input("Enter country (2 letter lowercase): ")
	news_final_url = news_base_url + "country=" + country + "&apiKey=" + news_API_Key
	response = requests.get(news_final_url).json()
	for i in range(0,5):
		print(response["articles"][i]["title"])

def clock():
	clock_base_url = "http://api.timezonedb.com/v2.1/get-time-zone?"
	clock_API_KEY = "Y5DE81BTSLO6"
	formatType = "json"
	by = "zone"
	zone = "America/Indiana/Indianapolis"
	clock_final_url = clock_base_url + "key=" + clock_API_KEY + "&format=" + formatType + "&by=" + by + "&zone=" + zone
	data = requests.get(clock_final_url).json()
	print("The current time in", data["abbreviation"], "is: ", data["formatted"])
		
def calendarRefresh(profile):
	if(profile == 1):
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
	elif(profile == 2):
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
	elif(profile == 3):
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
	elif(profile == 4):
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
	enable = 0
	on = 0
	while(True):
		#microResponse = serialTest()
		microResponse = input("Enter a serial command(1-8)")
		print(microResponse)
		if(microResponse == 1):
			if(on == 0):
				on =1
			else:
				on = 0
			print("Device on?:", on, "\n")
		elif(microResponse == 2):
			if(enable == 0):
				enable = 1
			else:
				enable = 0
			profile = 1
			print("Device enabled?:", enable, "\n")
		elif(microResponse == 3):
			profile+=1
			if(profile>4):
				profile = 1
		elif(microResponse == 4):
			profile-=1
			if(proifle <1):
				profile = 4
		if(on and enable):
			print("Weather:\n")
			openWeather()
			print("News:\n")
			news()
			print("Time:\n")
			clock()
			calendarRefresh(profile)
		print(on, enable)	

if __name__ == '__main__':
    main()
