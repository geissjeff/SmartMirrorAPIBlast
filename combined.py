from __future__ import print_function
import requests
import serial
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
	#print("Temperature in", name,":", tempF, "degrees F")
	#print("Description in", name,":", description, "\n")
	returnString = str(round(tempF)) + "F " + str(description)
	return returnString

def news():
	news_base_url = "https://newsapi.org/v2/top-headlines?"
	news_API_Key = "04296e8f713f454990ac3eaf6b88d19f"
	stringReturn = list()
	country = "us"#input("Enter country (2 letter lowercase): ")
	news_final_url = news_base_url + "country=" + country + "&apiKey=" + news_API_Key
	response = requests.get(news_final_url).json()
	for i in range(0,5):
		#print(response["articles"][i]["title"])
		tempList = response["articles"][i]["title"].strip().split('-')
		if(len(tempList[1]) > 17):
			if(len(tempList[0]) > 45):
				stringReturn.append(tempList[0][:44] + "-" + tempList[1])
			else:
				stringReturn.append(tempList[0] + "-" + tempList[1])
		else:
			if(len(tempList[0]) > 60):
				stringReturn.append(tempList[0][:59] + "-" + tempList[1])
			else:
				stringReturn.append(tempList[0] + "-" + tempList[1])
	return stringReturn #list of strings

def clock():
	clock_base_url = "http://api.timezonedb.com/v2.1/get-time-zone?"
	clock_API_KEY = "Y5DE81BTSLO6"
	formatType = "json"
	by = "zone"
	zone = "America/Indiana/Indianapolis"
	clock_final_url = clock_base_url + "key=" + clock_API_KEY + "&format=" + formatType + "&by=" + by + "&zone=" + zone
	data = requests.get(clock_final_url).json()
	listTime = data["formatted"].strip().split(':')
	listDate = listTime[0].strip().split(' ')
	listReturn = list()
	if(int(listDate[1]) < 12):
		stringMessage = "Good Morning"
	elif(int(listDate[1]) < 18):
		stringMessage = "Good Afternoon"
	else:
		stringMessage = "Good Evening"
	listReturn.append(stringMessage)
	listReturn.append(listDate[0])
	listReturn.append(listDate[1]+":"+listTime[1])
	
	#print("The current time in", data["abbreviation"], "is: ", data["formatted"])
	return listReturn
		
def calendarRefresh(profile):
	returnString = ""
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
	#end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
	end = list(now)
	for i in range(len(end)):
		if(end[i-1] == 'T'):
			end[i] = '2'
		if(end[i-2] == 'T'):
			end[i] = '3'
		if(end[i-4] == 'T'):
			end[i] = '5'
		if(end[i-5] == 'T'):
			end[i] = '9'
		if(end[i-7] == 'T'):
			end[i] = '5'
		if(end[i-8] == 'T'):
			end[i] = '9'
	endTime= "".join(end)
	#print('Getting the upcoming 10 events')
	events_result = service.events().list(calendarId='primary', timeMin=now, timeMax = endTime,
						maxResults=10, singleEvents=True,
						orderBy='startTime').execute()
	events = events_result.get('items', [])
	returnList = list()
	if not events:
		returnString = 'No upcoming events found.\n'
	for event in events:
		start = event['start']# event['start'].get('date'))
		if(start.get('date') != None):
			#print(start.get('date'), event['summary'])
			returnString = "All Day:   " + event['summary']
		else:
			startDate = start.get('dateTime').strip().split('-')
			startTime = startDate[2].strip().split('T')
			#print("{}-{}-{}: {} {}".format(startDate[0], startDate[1], startTime[0], startTime[1],event['summary']))
			returnString = startTime[1] +" "+ event['summary']  #0314:30OK
		returnList.append(returnString)
	return returnList #list of 8 strings
def main():
	profile = 1
	while(True):
		#microResponse = list(serialTest())
		microResponse = list(input("Enter a serial command(6 bits)"))
	#	print(microResponse)
		if(microResponse[0] == '1'):
			if(microResponse[1] == '1'):
				profile = int(microResponse[2])#0-3
				brightness = int(microResponse[3]) #0-7
				print("Weather:\n")
				openWeather()
				print("News:\n")
				news()
				print("Time:\n")
				clock()
				calendarRefresh(profile)

if __name__ == '__main__':
    main()
