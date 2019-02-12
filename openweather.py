import requests

API_key = "a0e157b3a341bfe1935ccc52588ae003"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

zip_code = input("Enter a Zip code: ")

Final_zip_url = base_url + "appid=" + API_key + "&zip=" + zip_code

weather_data = requests.get(Final_zip_url).json()

temp = weather_data["main"]["temp"]
description = weather_data["weather"][0]["description"]

tempF = 9*(temp - 273)/5 + 32
name = weather_data["name"]

print("Temperature in", name,":", tempF, "degrees F")
print("Description in", name,":", description, "\n")
