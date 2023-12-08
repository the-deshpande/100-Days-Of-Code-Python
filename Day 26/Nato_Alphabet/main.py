import pandas as pd

word = input('Enter a word : ')

df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {value.iloc[0]: value.iloc[1] for index, value in df.iterrows()}

phonetic = [nato_dict[letter.upper()] for letter in word]
print("Say : ")
print(*phonetic)
