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

        self.left_score = 0
        self.right_score = 0
        self.update()

    def left_scored(self):
        self.left_score += 1
        self.update()

    def right_scored(self):
        self.right_score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f'{self.left_score} : {self.right_score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over!', align=ALIGNMENT, font=FONT)
        self.goto(0, -40)
        if self.left_score > self.right_score:
            self.write(f'Left Won', align=ALIGNMENT, font=FONT)
        elif self.left_score < self.right_score:
            self.write(f'Right Won', align=ALIGNMENT, font=FONT)
        else:
            self.write(f'Draw', align=ALIGNMENT, font=FONT)
