from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Ariel', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.goto(0, 270)
        self.penup()
        self.hideturtle()

        self.score = 0
        self.update()

    def scored(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score : {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over!', align=ALIGNMENT, font=FONT)
        self.goto(0, -40)
        self.write(f'Your final score : {self.score}', align=ALIGNMENT, font=FONT)
