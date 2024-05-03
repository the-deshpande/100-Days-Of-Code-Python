import random
from turtle import Turtle

HOME = (0, -200)


class Ball(Turtle):

    def __init__(self):
        super().__init__('circle')
        self.color('blue')
        self.penup()
        self.speed(5)
        self.reposition()
        self.goto(HOME)
        self.ball_speed = 0.1

    def move(self):
        self.forward(20)

    def bounce(self):
        self.setheading(360-self.heading() + random.randint(-10, 10))

    def reflect(self):
        self.setheading(180-self.heading())

    def reposition(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.setheading(random.randint(30, 150))

    def speed_up(self):
        self.ball_speed *= 0.95
