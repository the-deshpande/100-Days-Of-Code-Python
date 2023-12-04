import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def rotate_clockwise():
    timmy.right(10)


def rotate_counter_clockwise():
    timmy.left(10)


def clear():
    timmy.home()
    timmy.clear()


screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(rotate_clockwise, 'd')
screen.onkey(rotate_counter_clockwise, 'a')
screen.onkey(clear, 'c')

screen.exitonclick()
