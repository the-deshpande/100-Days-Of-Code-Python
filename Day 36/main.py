import requests
from datetime import date, timedelta
from dotenv import dotenv_values
import json
from twilio.rest import Client

env = dotenv_values('.env')

yesterday = str(date.today() - timedelta(days=1))
day_before = str(date.today() - timedelta(days=2))


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHAVANTAGE_PARAMS = {
    'symbol': STOCK,
    'apikey': env['ALPHAVANTAGE_ACCESS_KEY'],
}

NEWS_PARAMS = {
    'q': COMPANY_NAME,
    'from': day_before,
    'sortBy': 'publishedAt',
    'apiKey': env['NEWS_KEY'],
}


response = requests.get(url=env['ALPHAVANTAGE_API'],params=ALPHAVANTAGE_PARAMS)
with open('data.json','w') as file:
    json.dump(response.json(), file, indent=4)

with open('data.json') as file:
    data = json.load(file)

yesterday_close = float(data['Time Series (Daily)'][yesterday]['4. close'])
day_before_close = float(data['Time Series (Daily)'][day_before]['4. close'])

if abs(yesterday_close-day_before_close)/yesterday_close > 5:
    print('Huge Change')
else:
    print("Minor Change")

response = requests.get(url=env['NEWS_API'], params=NEWS_PARAMS)
data = response.json()
for i in range(3):
    print(data['articles'][i]['source']['name'])
    print(data['articles'][i]['title'])
    print(data['articles'][i]['description'])
    print('-----------------------------------------------')

message = (f"{STOCK} : {round(abs(yesterday_close-day_before_close)/yesterday_close, 4)}% change in {COMPANY_NAME}\n"
           f"News : {data['articles'][0]['title']}")

client = Client(env['TWILIO_SID'], env['TWILIO_AUTH_TOKEN'])
message = client.messages.create(
    body=message,
    from_=env['TWILIO_PHONE_NO'],
    to=env['PHONE_NO'],
)
print(message.status)
