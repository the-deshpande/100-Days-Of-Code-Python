from dotenv import dotenv_values
import requests

env = dotenv_values('../.env')

f_name = input("Enter your first name : ")
l_name = input("Enter your last name : ")

while True:
    email = input("Enter your email address : ")
    cnf_email = input("Confirm your email address : ")

    if email == cnf_email:
        break

    print("The email does not match, kindly re-enter")

header = {
    'Content-Type': 'application/json',
    'Authorization': f'bearer {env['AUTH_TOKEN']}',
}

params = {
    'user': {
        'firstName': f_name,
        'lastName': l_name,
        'email': email
    }
}

response = requests.post(url=env['USERS_ENDPOINT'], headers=header, json=params)

if response.status_code == 200:
    print("You have been successfully signed up")
else:
    print("There has been some issue")

