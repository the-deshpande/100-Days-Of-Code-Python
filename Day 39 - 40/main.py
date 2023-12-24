# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


sheet_data = DataManager()
flight_data = FlightData(sheet_data.prices)
notifier = NotificationManager()

print(sheet_data.prices)
print(flight_data.data)

for i in range(len(sheet_data.prices)):
    if sheet_data.prices[i]['lowestPrice'] >= flight_data.data[i]['price']:
        notifier.send_sms(flight_data.data[i])
        notifier.send_mail(flight_data.data[i])

