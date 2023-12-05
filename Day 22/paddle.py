from turtle import Turtle

UP = 90


class Paddle(Turtle):

    def __init__(self, position: tuple):
        super().__init__('square')
        self.color('white')
        self.setheading(UP)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
