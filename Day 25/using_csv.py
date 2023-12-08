import csv

import pandas
import pandas as pd

with open('./weather_data.csv') as file:
    data = [i.strip().split(',') for i in file.readlines()]
    print(data)

print()

with open('./weather_data.csv') as file:
    data = csv.reader(file)
    temperatures = list()
    for row in data:
        temperatures.append(row[1])
    temperatures = list(map(int,temperatures[1:]))
print(temperatures)

print()

data = pandas.read_csv('./weather_data.csv')
print(data.to_dict())
temp = data['temp'].to_list()
print(data['temp'].mean())
print()

print(data[data['day'] == 'Monday']['temp']*(9/5)+32)

# Creating dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv('new_data.csv')
