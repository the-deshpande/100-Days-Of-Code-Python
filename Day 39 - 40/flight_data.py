import requests
from dotenv import dotenv_values
from datetime import date, timedelta

env = dotenv_values()

endpoint = 'https://api.tequila.kiwi.com/v2/search'

source = 'LON'
header = {
    'Content-Type': 'application/json',
    'apikey': env['TEQUILA_API_KEY'],
}


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, sheet_data):
        self.data = list()
        for entry in sheet_data:
            params = {
                'fly_from': source,
                'fly_to': entry['iataCode'],
                'date_from': (date.today() + timedelta(days=1)).strftime('%d/%m/%Y'),
                'data_to': (date.today() + timedelta(days=180)).strftime('%d/%m/%Y'),
                'limit': 1,
            }
            response = requests.get(url=endpoint, headers=header, params=params)

            try:
                output = response.json()['data'][0]
            except KeyError:
                continue
            else:
                self.data.append({
                    'cityFrom': output['cityFrom'],
                    'cityCodeFrom': output['cityCodeFrom'],
                    'cityTo': output['cityTo'],
                    'cityCodeTo': output['cityCodeTo'],
                    'utc_date': output['utc_departure'].split("T")[0],
                    'utc_time': output['utc_departure'].split("T")[1],
                    'price': output['price']
                })

