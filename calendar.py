import requests

base_url = "https://www.googleapis.com/calendar/v3/users/me/calendarList"
response = requests.get(url = base_url, headers = {"Authorization": "Bearer ACCESS_TOKEN"},)
response.raise_for_status()
calendars = response.json().get("items")