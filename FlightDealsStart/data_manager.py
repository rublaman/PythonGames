import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, api_key: str):
        self.__API_URL = "https://api.sheety.co/15c8f306457fd1b5f8dfc4449e832145/checkFlights/prices"
        self.__HEADERS = {
            'Authorization': f'Basic {api_key}'
        }

    def get_flights_from_google_sheet(self) -> dict:
        try:
            response = requests.get(self.__API_URL, headers=self.__HEADERS)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as err:
            print(f"Error in request: {err}")


test = DataManager(api_key="dGVzdFJ1YmVuOlBhc3N3MHJk")
print(test.get_flights_from_google_sheet())
