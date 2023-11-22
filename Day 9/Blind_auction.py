import os
from time import sleep
import resources

bidders = {}

print(resources.logo)
print("Welcome to the blind bid!")
while(True):
    name = input("Enter your name : ")
    bid = int(input("Enter your bid : "))
    bidders[name] = bid
    if(input("Are there other bidders left : ").lower() != 'yes'):
        break
    os.system('cls')
    sleep(1)

max = ''
for key in bidders:
    if(max == ''):
        max = key
        continue
    if(bidders[key]>bidders[max]):
        max = key

os.system('cls')
print("The bid is over")
print(f'Congratulations!! {max} you have won the product at the bid of ${bidders[max]}')