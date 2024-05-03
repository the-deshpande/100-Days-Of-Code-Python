from turtle import Turtle

HOME = (0, -250)


class Paddle(Turtle):
    def __init__(self):
        super().__init__('square')
        self.color('white')
        self.setheading(0)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(HOME)

    def move_right(self):
        if self.xcor() < 300:
            self.forward(20)

    def move_left(self):
        if self.xcor() > -300:
            self.backward(20)

