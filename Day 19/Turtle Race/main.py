from turtle import Turtle, Screen
import random

racing, winner = False, False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title='Make your bet!', prompt='Which turtle would you bet on?')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
racers = list()

for i in range(len(colors)):
    racers.append(Turtle(shape='turtle'))
    racers[i].penup()
    racers[i].color(colors[i])
    racers[i].goto(x=-230, y=-125+(i*50))

if bet:
    racing = True

while racing:

    for timmy in racers:
        if timmy.xcor() > 230:
            racing = False
            winner = timmy.pencolor()
        timmy.forward(random.randint(0, 20))

if winner:
    if winner == bet:
        print(f'You won! {winner} won the race')
    else:
        print(f'You lost! {winner} won the race')

screen.exitonclick()
