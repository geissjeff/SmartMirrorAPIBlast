import requests

base_url = "https://newsapi.org/v2/top-headlines?"

API_Key = "04296e8f713f454990ac3eaf6b88d19f"

country = "us"#input("Enter country (2 letter lowercase): ")

final_url = base_url + "country=" + country + "&apiKey=" + API_Key

response = requests.get(final_url).json()

for i in range(0,5):
	print(response["articles"][i]["title"])
