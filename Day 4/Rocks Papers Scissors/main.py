"""
## Roacks Papers and Scissors
A simple game of rocks papers and scissors
"""
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hands_signs = [rock,paper,scissors]

choice = int(input("Enter '0':Rock '1':Paper '2':Scissors"))
print(hands_signs[choice])

pc_choice = random.randint(0,2)
print('My Choice')
print(hands_signs[pc_choice])

if(choice == 0):
    if(pc_choice == 0):
        print("Its a Draw!!!")
    elif(pc_choice == 1):
        print("You Lose!!!")
    else:
        print("You Win!!!")
elif(choice == 1):
    if(pc_choice == 0):
        print("You Win!!!")
    elif(pc_choice == 1):
        print("Its a Draw!!!")
    else:
        print("You Lose!!!")
else:
    if(pc_choice == 0):
        print("You Lose!!!")
    elif(pc_choice == 1):
        print("You Win!!!")
    else:
        print("Its a Draw!!!")
