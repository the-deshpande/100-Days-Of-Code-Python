import random
import resources

print(resources.logo)

word = random.choice(resources.word_list)
print(f'The chosen word is {word}')

display = ['_']*len(word)

lives = 6
while(True):
    print(*display)
    letter = input("Guess a letter : ").lower()
    
    if(len(letter) != 1):
        print("Enter exactly 1 letter")
        continue

    if(letter in display):
        print("This letter has already been guessed")
        continue
    
    for i in range(len(word)):
        if(word[i] == letter):
            display[i] = letter
    
    if(letter in display):
        print(f"Correct!! '{letter}' is found in the word")

    if('_' not in display):
        print(*display)
        print("You Won!")
        break

    if(letter not in word):
        print(f"Wrong Choice!! '{letter}' is not present in the word, you lose a life")
        lives-=1
        if(lives == 0):
            print("You Lose!")
            break
    print(resources.stages[lives])
