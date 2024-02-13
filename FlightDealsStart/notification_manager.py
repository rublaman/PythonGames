import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self, target_phone_number: str):
        self.target_phone_number = target_phone_number

    def send_sms(self, flight_detail: dict) -> None:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        number_twilio = os.environ['TWILIO_PHONE_NUMBER']
        client = Client(account_sid, auth_token)
        body_message = self.__build_message(flight_detail)

        message = client.messages \
            .create(
                body=body_message,
                from_=f'{number_twilio}',
                to=f'{self.target_phone_number}'
            )

    def __build_message(self, flight_detail: dict) -> str:
        return f"Your flight from XXX will be {flight_detail}"
