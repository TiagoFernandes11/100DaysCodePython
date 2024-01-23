import requests

# Chave ainda nao funcionando

lat = -23.550520
lon = -46.633308
api_weather_key = "d9e1bd56567856c9e811151507a0054e"

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_weather_key
}

api_weather_call = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(api_weather_call, params=weather_params)
data = response.json()
print(data)
