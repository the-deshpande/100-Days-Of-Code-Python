import requests
import datetime as dt

LATITUDE = 18.520430
LONGITUDE = 73.856743
today = dt.datetime.today()

parameters = {
    'lat': LATITUDE,
    'lng': LONGITUDE,
    'formatted': 0,
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data['results']['sunrise'].split("T")[1][:2])
sunset = int(data['results']['sunset'].split("T")[1][:2])


