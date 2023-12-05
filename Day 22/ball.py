from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__('circle')
        self.color('blue')
        self.penup()
        self.speed(5)
        self.reposition()
        self.ball_speed = 0.1

    def move(self):
        self.forward(20)

    def bounce(self):
        self.setheading(360-self.heading())

    def reflect(self):
        self.ball_speed *= 0.9
        self.setheading(180-self.heading())

    def reposition(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.setheading(random.choice([random.randint(-45, 45), random.randint(135, 225)]))

