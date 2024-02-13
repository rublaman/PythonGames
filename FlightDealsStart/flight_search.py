import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        pass

    # def get_flights(self) -> None:
    #     account_sid = os.environ['TWILIO_ACCOUNT_SID']
    #     auth_token = os.environ['TWILIO_AUTH_TOKEN']
    #     number_twilio = os.environ['TWILIO_PHONE_NUMBER']
    #     client = Client(account_sid, auth_token)
    #     body_message = self.__build_message(flight_detail)
    #
    #     message = client.messages \
    #         .create(
    #             body=body_message,
    #             from_=f'{number_twilio}',
    #             to=f'{self.target_phone_number}'
    #         )
