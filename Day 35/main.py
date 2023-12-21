import requests
from twilio.rest import Client
from dotenv import dotenv_values

env = dotenv_values('.env')

account_sid = env['TWILIO_SID']
auth_token = env['TWILIO_AUTH_TOKEN']

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = 'd8cfd610dfc8843de37f582d50de6a69'
LATITUDE = 18.520430
LONGITUDE = 73.856743

parameters = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'appid': api_key,
    'cnt': 4,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()

for section in weather_data['list']:
    if section['weather'][0]['id'] < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's gonna be raining",
            from_=env['TWILIO_PHONE_NO'],
            to=env['PHONE_NO'],
        )
        print(message.status)
        break
