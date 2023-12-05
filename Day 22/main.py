from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("The Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(left_paddle.up, 'w')
screen.onkeypress(left_paddle.down, 's')
screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

#     Collision with the top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

#     Collision with the paddles
    if (left_paddle.distance(ball) < 50 and ball.xcor() < -320) or (
            right_paddle.distance(ball) < 50 and ball.xcor() > 320):
        ball.reflect()

#     Missing the Ball
    if ball.xcor() >= 390:
        scoreboard.left_scored()
        ball.reposition()
    if ball.xcor() <= -390:
        scoreboard.right_scored()
        ball.reposition()

#     Game Over
    if scoreboard.left_score == 5 or scoreboard.right_score == 5:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
