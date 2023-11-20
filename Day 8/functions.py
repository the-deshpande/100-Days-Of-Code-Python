def greet():
    print("Hi")
    print("Seems like a great day!")
    print("How are you?")
    print()
greet()

def greet_with_name(name):
    print(f'Hi {name}')
    print("Seems like a great day!")
    print(f'How are you, {name}?')
    print()
greet_with_name('Angela')

def greet_with(name,location):
    print(f'Hey {name}')
    print(f'What is it like in {location}')
    print()
greet_with('Angela','Nowhere')
greet_with('Nowhere','Angela')
greet_with(name='Angela',location='London')