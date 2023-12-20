import requests
from twilio.rest import Client

account_sid = 'AC91f0842ac5a7325da4c544f849cf7bc6'
auth_token = 'b6d6745e987a1c01ad7ce67e30c83578'

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
            from_='+12059315393',
            to='+91##########',
        )
        print(message.status)
        break
