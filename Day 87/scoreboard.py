from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Ariel', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score = 16
        self.goto(0, 270)
        self.update()

    def update(self):
        self.score -= 1
        self.clear()
        self.write(f"Tiles: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        if self.score == 0:
            self.write("Game Over! You Won!", align=ALIGNMENT, font=FONT)
            return
        self.write("Game Over! You Lost!", align=ALIGNMENT, font=FONT)
