from __future__ import print_function
import datetime
import pickle
import os.path
import flask
import requests
import google.oauth2.credentials
from googleapiclient.discovery import build
import google_auth_oauthlib.flow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CLIENT_ID = "671143266543-nhnrjkgvu64edkahkiv9edmit3l0uqhq.apps.googleusercontent.com" 
CLIENT_SECRET = "_IhQ7c8vY4sLQo8CJXxL8KX0" 
REFRESH_TOKEN = "1/HOYF-y6yl2FOSkxME3m0POyp0mmvEbKBc5H_1DMCGxU"
REDIRECT_URI = "https://developers.google.com/oauthplayground"

def test_api_request():
    if 'credentials' not in flask.session:
        return flask.redirect('authorize')

    credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])

    service = build('calendar', 'v3', credentials=credentials)
    calendar_api()
    flask.session['credentials'] = credentials_to_dict(credentials)
    return flask.jsonify(**files)


def authorize():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file('credentials.json', scopes=SCOPES)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
    authorization_url, state = flow.authorization_url(access_type = 'offline',
                                                      included_granted_scopes = 'true')
    flask.session['state'] = state
    return flask.redirect(authorization_url)

def oauth2callback():
    state = flask.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file('credentials.json', scopes=SCOPES, state=state)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    flask.session['credentials'] = credentials_to_dict(credentials)
    return flask.redirect(flask.url_for('test_api_request'))
def revoke():
    if 'credentials' not in flask.session:
        return ('You need to <a href="/authorize">authorize</a> before ' +
            'testing the code to revoke credentials.')
    credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])
    revoke = requests.post('https://accounts.google.com/o/oauth2/revoke',
                            params={'token':credentials.token},
                            headers = {'content-type': 'application/x-www-form-urlencoded'})
    status_code = getattr(revoke, 'status_code')
    if status_code == 200:
        return('Credentials successfully revoked.')
    else:
        return('an error occured')

def clear_credentials():
    if 'credentials' in flask.session:
        del flask.session['credentials']
    return ('Credentials ahve been cleared.<br><br>')
def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri' : credentials.token_uri,
            'client_id' : credentials.client_id,
            'client_secret' : credentials.client_secret,
            'scopes' : credentials.scopes}





def main():
    test_api_request()












# def main():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     credentials = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             credentials = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not credentials or not credentials.valid:
#         if credentials and credentials.expired and credentials.refresh_token:
#             credentials.refresh(Request())
#         else:
#             state = flask.session['state']
#             flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES, state = state)
#             flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
#             authorization_response = flask.request.url
#             flow.fetch_token(authorization_response=authorization_response)
#             credentials = flow.credentials
#             flask.session['credentials'] = {
#             'token'         : credentials.token,
#             'refresh_token' : credentials.refresh_token,
#             'token_uri'     : credentials.token_uri,
#             'client_id'     : credentials.client_id,
#             'client_secret' : credentials.client_secret,
#             'scopes'        : credentials.scopes
#             }

#     service = build('calendar', 'v3', credentials=credentials)
def calendar_api():
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
