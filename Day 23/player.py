from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__('turtle')
        self.penup()
        self.teleport()
        self.setheading(90)

    def move_fwd(self):
        self.forward(MOVE_DISTANCE)

    def move_bwd(self):
        if self.ycor() == STARTING_POSITION[-1]:
            return
        self.backward(MOVE_DISTANCE)

    def teleport(self):
        self.goto(STARTING_POSITION)
