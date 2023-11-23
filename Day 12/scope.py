a = 10

def b():
    a = 8
    print('I am B')

b()
print(a)

def a():
    def b():
        print("I am AB")
    print("I am A")
    b()

a()
b()