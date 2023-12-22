import requests
from dotenv import dotenv_values

env = dotenv_values()

header = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {env['AUTH_TOKEN']}'
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        response = requests.get(url=env['SHEETY_ENDPOINT'], headers=header)
        self.prices = response.json()['prices']

    def update(self, sheet_data):
        self.prices = sheet_data
        self.upload()

    def upload(self):
        for entry in self.prices:
            price = {'price': entry}
            requests.put(url=f"{env['SHEETY_ENDPOINT']}/{entry['id']}", headers=header, json=price)

