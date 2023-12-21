import requests
from dotenv import dotenv_values
import datetime as dt
env = dotenv_values()

today = dt.datetime.now()

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "Content-Type": "application/json",
    "x-app-id": env["APP_ID"],
    "x-app-key": env["API_KEY"],
}

exercise = input("What did you work out today? : ")

query = {
    "query": exercise,
}

response = requests.post(url=endpoint, headers=header, json=query)

header = {
    "Content-Type": 'application/json',
    'Authorization': f"Bearer {env['AUTH_TOKEN']}"
}

for exercise in response.json()['exercises']:
    workout = {
        'workout': {
            'date': today.strftime('%x'),
            'time': today.strftime('%X'),
            'exercise': exercise['name'],
            'duration': str(exercise['duration_min']),
            'calories': exercise['nf_calories'],
        }
    }

    response = requests.post(url=env['SHEETY_POST_ENDPOINT'], json=workout, headers=header)
    print(response.json())
