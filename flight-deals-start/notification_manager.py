import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self, target_phone_number: str):
        self.phone_number = target_phone_number

    def send_mail(self) -> None:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        number_twilio = os.environ['TWILIO_PHONE_NUMBER']
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body="Test",
                from_=f'{number_twilio}',
                to=f'{self.phone_number}'
            )
