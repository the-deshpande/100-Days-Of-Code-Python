from twilio.rest import Client
from dotenv import dotenv_values
from user_list import UserList
import smtplib

env = dotenv_values()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(env['TWILIO_SID'], env['TWILIO_AUTH_TOKEN'])
        self.receivers = UserList().users

    def send_sms(self, details: dict):
        body = (f"Low Price Alert!!! "
                f"Only ${details['price']} to fly from "
                f"{details['cityFrom']}-{details['cityCodeFrom']} to {details['cityTo']}-{details['cityCodeTo']}, "
                f"on {details['utc_date']} at {details['utc_time'][:5]} UTC")
        message = self.client.messages.create(
            body=body,
            from_=env['TWILIO_PHONE_NO'],
            to=env['PHONE_NO'],
        )
        print(message.status)

    def send_mail(self, details: dict):
        body = (f"Only ${details['price']} to fly from "
                f"{details['cityFrom']}-{details['cityCodeFrom']} to {details['cityTo']}-{details['cityCodeTo']}, "
                f"on {details['utc_date']} at {details['utc_time'][:5]} UTC")
        for receiver in self.receivers:
            main = (f"Subject:Low Price Alert!!!\n\n"
                    f"Dear {receiver['firstName']} {receiver['lastName']},\n")
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=env['SENDER_EMAIL'], password=env['SENDER_PASSWORD'])
                connection.sendmail(from_addr=env['SENDER_EMAIL'], to_addrs=receiver['email'], msg=(main+body))

