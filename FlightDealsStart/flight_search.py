import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    # https://tequila.kiwi.com/
    # https://api.tequila.kiwi.com/v2/search?

    def __init__(self, api_key: str):
        self.__API_URL = ""
        self.__HEADERS = {
            'Authorization': f'Basic {api_key}'
        }

    def get_flight_price(self, info: dict) -> dict:
        try:
            response = requests.get(self.__API_URL, headers=self.__HEADERS)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as err:
            print(f"Error in request: {err}")
