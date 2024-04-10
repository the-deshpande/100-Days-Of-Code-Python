from data import ascii_art, morse_converter
import pyperclip

while True:
    print(ascii_art)
    text = input("Enter the text you wish to translate: ")
    morse = list()

    for letter in text:
        morse.append(morse_converter.get(letter.upper()))
        if morse[-1] == None:
            morse = morse[:-1]
    morse = ' '.join(morse)

    print("Your text is translated to (It has been copied to your clipboard):")
    pyperclip.copy(morse)
    print(morse)
    print("------------------------------------------------------------")

    more = input("Enter anything if you wish to continue: ")

    if not more:
        print("Thank-you for using the morse code translator")
        break
