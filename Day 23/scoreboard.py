from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-280, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.curr_level = 1
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f'Level : {self.curr_level}', align='left', font=FONT)

    def level_up(self):
        self.curr_level += 1
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=FONT)
