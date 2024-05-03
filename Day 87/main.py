from turtle import Screen
from ball import Ball
from paddle import Paddle
from tile import Tiles
from scoreboard import Scoreboard
from time import sleep


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()
paddle = Paddle()
tiles = Tiles()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.move_right, 'Right')
screen.onkeypress(paddle.move_left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    sleep(ball.ball_speed)
    ball.move()

    if tiles.check_collision(ball):
        scoreboard.update()

    if ball.xcor() > 300 or ball.xcor() < -300:
        ball.reflect()
    if ball.ycor() > 300:
        ball.bounce()

    if ball.distance(paddle) < 50 and (-270 < ball.ycor() < -230):
        ball.bounce()

    if ball.ycor() < -300 or scoreboard.score == 0:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
