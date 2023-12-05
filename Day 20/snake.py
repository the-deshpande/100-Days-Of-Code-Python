from turtle import Turtle

MOVE_SPEED = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:

    def __init__(self):
        self.snake = list()
        for i in range(3):
            self.snake.append(Turtle(shape='square'))
            self.snake[-1].color('white')
            self.snake[-1].penup()
            self.snake[-1].goto(x=-i * 20, y=0)
        self.head = self.snake[0]

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].pos())
        self.head.forward(MOVE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)