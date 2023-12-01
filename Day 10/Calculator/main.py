from resources import logo;
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations = {
    '+':add,
    '-':substract,
    '*':multiply,
    '/':divide
}

print(logo)
num1 = int(input("Enter an Integer : "))
while(True):
    num2 = int(input("Enter another Integer : "))
    for i in operations:
        print(i)
    symbol = input("Pick an operation out of the above : ")
    answer = operations[symbol](num1,num2)
    print(f'{num1} {symbol} {num2} = {answer}')

    if(input("Enter 'y' to chain equations or enter anything else to exit : ") != 'y'):
        break
    num1 = answer