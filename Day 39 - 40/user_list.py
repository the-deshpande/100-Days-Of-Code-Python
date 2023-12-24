import requests
from dotenv import dotenv_values

env = dotenv_values()

header = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {env['AUTH_TOKEN']}'
}


class UserList:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        response = requests.get(url=env['USERS_ENDPOINT'], headers=header)
        self.users = response.json()['users']
