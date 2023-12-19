import requests
import datetime as dt
import smtplib

email = "sender.test.151223@gmail.com"
password = "eyjsqwehpxkaiobv"

LATITUDE = 18.520430
LONGITUDE = 73.856743


def is_overhead():
    response = requests.get(url='https://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])
    if abs(iss_lat - LATITUDE) <= 5 and abs(iss_lng - LONGITUDE) <= 5:
        return True
    return False


def is_night():
    today = dt.datetime.today()
    parameters = {
        'lat': LATITUDE,
        'lng': LONGITUDE,
        'formatted': 0,
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1][:2])
    sunset = int(data['results']['sunset'].split("T")[1][:2])
    if today.hour >= sunset or today.hour <= sunrise:
        return True
    return False


if is_overhead() and is_night():
    with smtplib.SMTP('smtp.google.com', 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs='desh.kaiwalya@gmail.com',msg="Subject:Hey\n\nLook Up")
