import smtplib
from dotenv import dotenv_values
from datetime import datetime

env = dotenv_values()

with open('date.txt') as file:
    last_date = datetime.strptime(file.readline(), '%Y-%m-%d')

today = datetime.today()
if (today - last_date).days > 90:

    message = ("Subject: Request for a Raise\n\n"
               "Good Morning Boss,"
               "I would like to apply for a hike considering that I believe that for the last few months I have been"
               "working hard and have actually made the company high profits. I believe that this should fall under"
               "consideration for my raise. Let us have a meeting to talk about this further.")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=env['EMAIL'], password=env['PASSWORD'])
        connection.sendmail(from_addr=env['EMAIL'], to_addrs=env['RECEIVER'], msg=message)

    with open('date.txt', 'w') as file:
        file.write(today.strftime('%Y-%m-%d'))
