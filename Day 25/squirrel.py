import pandas as pd

data = pd.read_csv('./squirrel.csv')

print(data['Primary Fur Color'].unique())
data_dict = dict()
data_dict['colors'] = data['Primary Fur Color'].unique()[1:]
data_dict['count'] = list()
for i in data['Primary Fur Color'].unique()[1:]:
    data_dict['count'].append(data[data['Primary Fur Color'] == i]['Primary Fur Color'].count())

pd.DataFrame(data_dict).to_csv('squirrel_color.csv')
