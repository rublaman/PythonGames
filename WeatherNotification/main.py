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

id_weather_list = weather_ids = [x["weather"][0]["id"] for x in weather_data["list"] if x["weather"][0]["id"] < 700]

if len(id_weather_list) >= 1:
    print("Bring an umbrella")
