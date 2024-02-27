import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    # https://tequila.kiwi.com/
    # Docu -> https://tequila.kiwi.com/portal/docs/tequila_api/search_api

    def __init__(self, api_key: str):
        self.__API_URL = f"https://api.tequila.kiwi.com/v2/search?"
        self.__HEADERS = {
            'Authorization': f'Basic {api_key}'
        }

    def __create_query(self, flight_details: dict) -> str:

        return ""


    def get_flight_price(self, flight_details: dict) -> dict:

        query = self.__create_query()

        try:
            response = requests.get(self.__API_URL, headers=self.__HEADERS)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as err:
            print(f"Error in request: {err}")


test = FlightSearch(api_key="")
print(test.get_flight_price())