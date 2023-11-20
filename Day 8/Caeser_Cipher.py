import art
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# def encrypt(plain_text,shift):
#     cipher_text = list()
#     for i in plain_text:
#         cipher_text.append(alphabet[(alphabet.index(i)+shift)%26])
#     print(f"The encrypted text is {''.join(cipher_text)}")

# def decrypt(cipher_text,shift):
#     plain_text = list()
#     for i in cipher_text:
#         plain_text.append(alphabet[(alphabet.index(i)-shift)%26])
#     print(f"The decrypted text is {''.join(plain_text)}")

def ceaser(text,shift,direction):
    new_text = list()
    if(direction == 'd'):
        shift *= -1
    for i in text:
        if i not in alphabet:
            new_text.append(i)
            continue
        new_text.append(alphabet[(alphabet.index(i)+shift)%26])
    print(f"The cipher text is '{''.join(new_text)}'")

print(art.logo)
while(True):
    direction = input("Enter 'e' to encode and 'd' to decode : ")
    text = input("Enter the text : ").lower()
    shift = int(input("Enter the shift : "))
    ceaser(text,shift,direction)
    if(input("Enter 'e' to exit : ") == 'e'):
        print("Good Bye")
        break