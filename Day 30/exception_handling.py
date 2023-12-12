try:
    print('Hello')
except FileNotFoundError:
    print("there was an error")
except KeyboardInterrupt:
    print("Okay, Bye")
else:
    print("Success")
finally:
    print("After all this")

height = float(input("Enter your height : "))
weight = int(input("Enter your weight : "))


