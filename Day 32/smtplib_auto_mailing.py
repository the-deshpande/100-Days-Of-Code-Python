import datetime as dt
import smtplib

email = "sender.test.151223@gmail.com"
password = "eyjsqwehpxkaiobv"
receiver_mail = "celeno4376@beeplush.com"

message = ("Subject:Hello\n\n"
           "This is the body of my email")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=receiver_mail, msg=message)

print(dt.datetime.now())
