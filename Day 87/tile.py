from turtle import Turtle
from ball import Ball

COLS, ROWS = 5, 3


class Tiles:
    def __init__(self):
        self.tiles = [[Turtle('square') for i in range(COLS)] for i in range(ROWS)]
        self.positions = [[(-200, 250), (-100, 250), (0, 250), (100, 250), (200, 250)],
                          [(-200, 200), (-100, 200), (0, 200), (100, 200), (200, 200)],
                          [(-200, 150), (-100, 150), (0, 150), (100, 150), (200, 150)]]
        for i in range(ROWS):
            for j in range(COLS):
                self.tiles[i][j].penup()
                self.tiles[i][j].shapesize(stretch_len=2, stretch_wid=1)
                self.tiles[i][j].goto(self.positions[i][j])
                self.tiles[i][j].color('red')

    def check_collision(self, ball: Ball) -> bool:
        for row in range(ROWS):
            for col in range(COLS):
                if self.tiles[row][col].distance(ball) < 30:
                    ball.bounce()
                    self.tiles[row][col].goto(400, 400)
                    ball.speed_up()
                    return True

        return False
