import requests

end_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "API-KEY"

weather_params = {
    "lat": 40.416775,
    "lon": -3.703790,
    "appid": api_key,
    "cnt": 4
}

r = requests.get(end_point, params=weather_params)
r.raise_for_status()
weather_data = r.json()

