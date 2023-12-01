import resources
import random
import os

def main(A,score=0):
    B=random.choice(resources.data)
    print(f'Option A : {A["name"]} a {A["description"]} in {A["country"]}')
    print(resources.vs)
    print(f'Option B : {B["name"]} a {B["description"]} in {B["country"]}')
    guess = input("Who has more followers 'A' or 'B' : ")
    print(f"{A['name']} has {A['follower_count']} mil followers whereas {B['name']} has {B['follower_count']} mil followers")
    if(guess == 'A' and A['follower_count']>B['follower_count']):
        score+=1
        print(f"Correct!!!! Your score is {score} now")
        return main(A=A,score=score)
    elif(guess == 'B' and A['follower_count']<B['follower_count']):
        score+=1
        print(f"Correct!!!! Your score is {score} now")
        return main(A=B,score=score)
    else:
        print("Oh! That was wrong")
        print("Game Over!!")
        return score

while(True):
    print(resources.logo)
    print("Welcome to the game Higher Lower")
    score = main(A=random.choice(resources.data))
    print(f'Good game, your final score is {score}')
    if(input("Do you wish to restart game 'y' : ").lower() != 'y'):
        print("Thankyou for playing")
        break
    os.system('cls')
