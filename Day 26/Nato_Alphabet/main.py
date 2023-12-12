import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {value.iloc[0]: value.iloc[1] for index, value in df.iterrows()}


def phonetic_generator():
    word = input('Enter a word : ').upper()
    try:
        phonetic = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Only Alphabets")
        phonetic_generator()
    else:
        print("Say : ")
        print(*phonetic)


phonetic_generator()
