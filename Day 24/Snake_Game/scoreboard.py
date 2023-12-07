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

        with open('data.txt') as file:
            self.high_score = int(file.read())

        self.score = 0
        self.update()

    def scored(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score : {self.score} | HighScore : {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()
