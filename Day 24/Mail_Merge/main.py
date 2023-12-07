with open('./Input/Letters/starting_letter.txt') as file:
    letter = file.read()

with open('./Input/Names/invited_names.txt') as file:
    names = list()
    for line in file.readlines():
        names.append(line.strip())

for name in names:
    with open(f'./Output/ReadyToSend/mail_to_{name}.txt', 'w') as file:
        file.write(letter.replace('[name]', name))
