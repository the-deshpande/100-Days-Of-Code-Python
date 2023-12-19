import datetime as dt
import smtplib
import random

today = dt.datetime.now().weekday()
email = "sender.test.151223@gmail.com"
password = "eyjsqwehpxkaiobv"
receiver_mail = "celeno4376@beeplush.com"

with open('./quotes.txt') as file:
    quote = random.choice(file.readlines())

message = f"Subject:Morning Motivation\n\n{quote}"

if today == 4:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=receiver_mail, msg=message)
