from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Ariel', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)

    def game_over(self, score: int):
        self.goto(0, 0)
        if score == 0:
            self.write("Game Over! You Won!", align=ALIGNMENT, font=FONT)
            return
        self.write("Game Over! You Lost!", align=ALIGNMENT, font=FONT)
