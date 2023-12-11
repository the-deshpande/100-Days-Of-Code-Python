"""
# Password Generator
Generates a strong password which can be used to create an account
"""
import random
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'
array = [letters, numbers, symbols]


def generate():
    num_of_letters = random.randint(12, 18)
    num_of_numbers = random.randint(2, 4)
    num_of_symbols = random.randint(2, 4)
    key = [0]*(num_of_letters-num_of_numbers-num_of_symbols)+[1]*num_of_numbers+[2]*num_of_symbols
    password = ''
    for i in range(num_of_letters):
        element = random.choice(key)
        password += random.choice(array[element])
        key.remove(element)
    return password
