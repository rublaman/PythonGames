import requests
import os
from twilio.rest import Client

twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
openweather_end_point = "https://api.openweathermap.org/data/2.5/forecast"
openweather_api_key = os.environ['OPEN_WEATHER_AUTH_TOKEN']

weather_params = {
    "lat": 37.270969,
    "lon": -79.941429,
    "appid": openweather_api_key,
    "cnt": 4
}

r = requests.get(openweather_end_point, params=weather_params)
r.raise_for_status()
weather_data = r.json()

id_weather_list = weather_ids = [x["weather"][0]["id"] for x in weather_data["list"] if x["weather"][0]["id"] < 700]

if len(id_weather_list) >= 1:
    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today! Remember to bring an ☔.",
        from_='+twilio-phone',
        to='+my-verified-phone'
    )
    print(message.sid)
