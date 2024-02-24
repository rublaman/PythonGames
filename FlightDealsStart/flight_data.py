from FlightDealsStart.data_manager import DataManager

class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self, api_key: str):
        self.__flights = DataManager(api_key).get_flights_from_google_sheet()

    def struct_flights(self):
        flights = self.__flights["prices"]
