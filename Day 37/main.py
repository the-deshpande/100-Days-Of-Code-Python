import requests
from datetime import datetime

USERNAME = 'thedeshpande'
TOKEN = 'the_deshpande'

header = {
    'X-USER-TOKEN': TOKEN,
}

pixela_endpoint = 'https://pixe.la/v1/users'
pixela_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# To create a account

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': 'graph1',
    'name': 'Consistency Graph',
    'unit': 'day',
    'type': 'int',
    'color': 'sora',
}

# Creating a Graph

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

today = datetime.now().strftime('%Y%m%d')

pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
pixel_config = {
    'date': today,
    'quantity': '1',
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=header)
# print(response.text)

pixel_put_data = {
    'quantity': '12'
}

# response = requests.put(url=f"{pixel_endpoint}/{today}", json=pixel_put_data, headers=header)
# print(response.text)

response = requests.delete(url=f"{pixel_endpoint}/{today}", headers=header)
print(response.text)
