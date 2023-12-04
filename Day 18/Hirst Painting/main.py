import turtle

import colorgram
from turtle import Turtle, Screen
import random


colors = colorgram.extract('./hirst_painting.jpg', 64)
rgb_colors = list()
for i in colors[4:]:
    rgb_colors.append(tuple(i.rgb))

turtle.colormode(255)

timmy = Turtle()
timmy.penup()
timmy.goto(-250, -200)
y_coordinate = -200
for row in range(10):
    for column in range(10):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.forward(50)
    y_coordinate += 50
    timmy.goto(-250, y_coordinate)
timmy.hideturtle()

screen = Screen()
screen.exitonclick()
