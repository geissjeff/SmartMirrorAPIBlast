import requests

base_url = "http://api.timezonedb.com/v2.1/get-time-zone?"

API_KEY = "Y5DE81BTSLO6"

formatType = "json"

by = "zone"


zone = "America/Indiana/Indianapolis"


final_url = base_url + "key=" + API_KEY + "&format=" + formatType + "&by=" + by + "&zone=" + zone

data = requests.get(final_url).json()


print("The current time in", data["abbreviation"], "is: ", data["formatted"])
