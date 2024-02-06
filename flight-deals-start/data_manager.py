import requests
import os
from datetime import datetime


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_flights_from_google_sheet(self):
        SHEETY_API_URL = "https://api.sheety.co/15c8f306457fd1b5f8dfc4449e832145/checkFlights/prices"

        headers = {
            'Authorization': f'Basic Om51bGw='
        }

        response = requests.get(SHEETY_API_URL, headers=headers)
