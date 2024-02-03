import requests
import os
from datetime import datetime


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_flights_from_google_sheet(self):
        SHEETY_API_URL = "https://api.sheety.co/----------/workoutTracking/flights"

        headers = {
            'Authorization': f'Basic ---------'
        }

        response = requests.post(SHEETY_API_URL, headers=headers)
