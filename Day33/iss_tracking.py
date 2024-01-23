import requests

iss_endpoint = "http://api.open-notify.org/iss-now.json"

response = requests.get(iss_endpoint)
response.raise_for_status()

data = response.json()

iss_latitude = data["iss_position"]["latitude"]
iss_longitude = data["iss_position"]["longitude"]

iss_position = (iss_latitude, iss_longitude)

print(iss_position)