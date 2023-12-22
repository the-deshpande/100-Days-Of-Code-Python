import requests
from dotenv import dotenv_values

env = dotenv_values()

endpoint = 'https://api.tequila.kiwi.com/locations/query'

header = {
    'Content-Type': 'application/json',
    'apikey': env['TEQUILA_API_KEY'],
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, sheet_data):
        self.data = list()
        for entry in sheet_data:
            params = {
                'term': entry['city'],
                'location_types': 'airport',
            }
            response = requests.get(url=endpoint, headers=header, params=params)

            entry['iataCode'] = response.json()['locations'][0]['id']
            self.data.append(entry)

