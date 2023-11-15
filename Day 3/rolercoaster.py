print("Welcome to the rolercoaster")
height = int(input("What is your height in cm : "))
if (height>120):
    print("You can ride the rolercoaster")
    age = int(input("What is your age : "))
    total=0
    if (age < 12):
        print("Child tickets are $5")
        total = 5
    elif (age <= 18):
        print("Youth tickets are $7")
        total = 7
    elif (age>=45 and age<=55):
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult tickets are $12")
        total = 12
    photo = input("Do you want a photo taken (y=yes, n=no) : ")
    if(photo == 'y'):
        total+=3
    print(f'Your total bill is ${total}')
else:
    print("Sorry, you have to grow taller before you can ride")
