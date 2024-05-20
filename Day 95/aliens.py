from turtle import Turtle

ROWS, COLUMNS = 5, 9
POSITIONS = [
    [(-200, 330), (-150, 330), (-100, 330), (-50, 330), (0, 330), (50, 330), (100, 330), (150, 330), (200, 330)],
    [(-175, 280), (-125, 280), (-75, 280), (-25, 280), (25, 280), (75, 280), (125, 280), (175, 280), (225, 280)],
    [(-200, 230), (-150, 230), (-100, 230), (-50, 230), (0, 230), (50, 230), (100, 230), (150, 230), (200, 230)],
    [(-225, 180), (-175, 180), (-125, 180), (-75, 180), (-25, 180), (25, 180), (75, 180), (125, 180), (175, 180)],
    [(-200, 130), (-150, 130), (-100, 130), (-50, 130), (0, 130), (50, 130), (100, 130), (150, 130), (200, 130)],
]


class ModifiedTurtle(Turtle):
    def __init__(self, shape):
        super().__init__(shape)
        self.hit = False


class Aliens:
    def __init__(self):
        self.aliens = []
        self.location = 0

        for i in range(ROWS):
            self.aliens.append([])
            for j in range(COLUMNS):
                self.aliens[i].append(ModifiedTurtle('square'))
                if i % 2 == 0:
                    self.aliens[i][j].color('blue')
                else:
                    self.aliens[i][j].color('red')
                self.aliens[i][j].penup()
                self.aliens[i][j].setheading(0)
                self.aliens[i][j].goto(POSITIONS[i][j])

    def vibrate(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                if i % 2 == 0:
                    if self.location == 0:
                        self.aliens[i][j].forward(25)
                    elif self.location == 1:
                        self.aliens[i][j].backward(50)
                    else:
                        self.aliens[i][j].forward(25)

                elif i == 1:
                    if self.location != 2:
                        self.aliens[i][j].backward(25)
                    else:
                        self.aliens[i][j].forward(50)

                else:
                    if self.location == 2:
                        self.aliens[i][j].backward(50)
                    else:
                        self.aliens[i][j].forward(25)

        self.location = (self.location + 1) % 3

    def advance(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                self.aliens[i][j].goto(self.aliens[i][j].xcor(), self.aliens[i][j].ycor()-50)

    def check_lost(self):
        for i in range(ROWS-1, 0, -1):
            for j in range(COLUMNS):
                if not self.aliens[i][j].hit and self.aliens[i][j].ycor() < -280:
                    return True

        return False

    def check_won(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                if not self.aliens[i][j].hit:
                    return False

        return True

    def collision(self, bullets: dict):

        for i in range(ROWS):
            for j in range(COLUMNS):
                for bullet in bullets:
                    if not self.aliens[i][j].hit:
                        if bullet.distance(self.aliens[i][j]) < 10:
                            self.aliens[i][j].hideturtle()
                            self.aliens[i][j].hit = True
                            bullet.hit = True

