from turtle import Turtle


class Spaceship(Turtle):

    def __init__(self):
        super().__init__('triangle')
        self.color('white')
        self.right(30)
        self.penup()
        self.goto(0, -300)
        self.bullets = []

    def move_right(self):
        if self.xcor() < 250:
            self.goto(self.xcor()+5, self.ycor())

    def move_left(self):
        if self.xcor() > -250:
            self.goto(self.xcor()-5, self.ycor())

    def shoot(self):
        self.bullets.append(Bullet())
        self.bullets[-1].goto(self.xcor(), self.ycor()+25)

    def move_bullet(self):
        for index, bullet in enumerate(self.bullets):
            bullet.forward(10)

            if bullet.ycor() > 350:
                bullet.hit = True

    def collision(self):
        for bullet in self.bullets:
            if bullet.hit:
                bullet.hideturtle()
                self.bullets.remove(bullet)


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.seth(90)
        self.shapesize(stretch_wid=0.1, stretch_len=0.5)
        self.hit = False

