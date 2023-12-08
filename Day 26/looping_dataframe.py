import pandas as pd

student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

for key, value in student_dict.items():
    print(key, value)

df = pd.DataFrame(student_dict)
for key, value in df.items():
    print(key, value)

for index, row in df.iterrows():
    print(index, row)
