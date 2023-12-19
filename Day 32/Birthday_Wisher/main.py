import datetime as dt
import random
import pandas as pd
import smtplib

letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
today = dt.datetime.today().date()
df = pd.read_csv('./birthdays.csv')
birthdays = df[(df['month'] == today.month) & (df['day'] == today.day)]
email = "sender.test.151223@gmail.com"
password = "eyjsqwehpxkaiobv"

for index, value in birthdays.iterrows():
    with open(f'./letter_templates/{random.choice(letters)}') as file:
        content = file.readlines()
    for i in range(len(content)):
        content[i] = content[i].replace('[NAME]', value['name'])
    content = ['Subject:Happy Birthday\n\n'] + content
    message = ''.join(content)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=value['email'], msg=message)

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




