import random

print("Welcome to the number guessing game!!")

number = random.randint(1,100)
print("I have a number between 1 - 100 in mind")

if(input("Easy Mode : 'e' or Hard Mode : 'h' : ") == 'h'):
    tries = 5
else:
    tries = 10
print(f'You have {tries} tries')

while(tries > 0):
    guess = int(input('Make a guess : '))

    if(guess == number):
        break
    elif(guess < number):
        print("You guessed too low")
    else:
        print("You guessed too high")
    tries-=1
    print(f"You now only have {tries} tries remaining")

if(tries == 0):
    print(f"Well Played! But you lost, the number was {number}")
else:
    print("Correct! You won.")