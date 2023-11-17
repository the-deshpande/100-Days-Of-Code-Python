'''
# Password Generator
Generates a strong password which can be used to create an account
'''
import random
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'
array = [letters,numbers,symbols]

print("Welcome the the password generator")
num_of_letters = int(input('Enter the total number letters you want : '))
num_of_numbers = int(input('How many numbers would you like : '))
num_of_symbols = int(input('How many symbols would you like : '))
key = [0]*(num_of_letters-num_of_numbers-num_of_symbols)+[1]*num_of_numbers+[2]*num_of_symbols
print("Your password could be : ",end='')
for i in range(num_of_letters):
    element = random.choice(key)
    print(random.choice(array[element]),end='')
    key.remove(element)
