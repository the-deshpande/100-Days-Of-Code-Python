from resources import logo
import random

def dealer_count(array,deck):
    while(sum(array)<17):
        array.append(random.choice(deck))
    
    if(sum(array) > 21 and 11 in array):
        array[array.index(11)] = 1
        dealer_count(array,deck)
    
    return array

def main():
    print(logo)

    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    player =[random.choice(deck),random.choice(deck)]
    dealer =[random.choice(deck),random.choice(deck)]


    while(True):
        if(sum(player) > 21):
            if(11 in player):
                player[player.index(11)] = 1
            else:
                return False

        print(f'Your cards are {player}, Sum : {sum(player)}')
        print(f'The dealers first card is {dealer[0]}')

        if(input("Hit : 'h' or Stand 's' : ") == 'h'):
            player.append(random.choice(deck))
        else:
            break

    dealer = dealer_count(dealer,deck)

    print(f'The dealers final cards are {dealer}, Sum : {sum(dealer)}')
    if(sum(dealer) > 21):
        return True
    else:
        if(sum(dealer)<sum(player)):
            return True
        else:
            return False

while(True):
    if(main()):
        print("Congratulation!! You Won")
    else:
        print("Well Played!! But you did not Win")
    if(input("Do you wish to restart game 'y' : ") != 'y'):
        print("Thank you for playing!!")
        break

