import requests

api_key = "4af39db540863028eefdaf74dffb3a65"
LAT = 51.507351
LONG = -0.127758
URL = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
}

response = requests.get(URL, params=weather_params)
print(response.json())
