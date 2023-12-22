from twilio.rest import Client
from dotenv import dotenv_values

env = dotenv_values()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, details: dict):
        client = Client(env['TWILIO_SID'], env['TWILIO_AUTH_TOKEN'])
        body = (f"Low Price Alert!!! "
                f"Only ${details['price']} to fly from "
                f"{details['cityFrom']}-{details['cityCodeFrom']} to {details['cityTo']}-{details['cityCodeTo']}, "
                f"on {details['utc_date']} at {details['utc_time'][:5]} UTC")
        message = client.messages.create(
            body=body,
            from_=env['TWILIO_PHONE_NO'],
            to=env['PHONE_NO'],
        )
        print(message.status)
