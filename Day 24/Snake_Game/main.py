from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def close_game():
    global game_is_on
    game_is_on = False


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(close_game, 'space')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     Collision detector with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.scored()
        snake.extend()

#     Collision detection with the wall
    if (snake.head.pos()[0] > 290 or snake.head.pos()[0] < -290 or
            snake.head.pos()[1] > 290 or snake.head.pos()[1] < -290):
        scoreboard.reset()
        snake.reset()

#     Collision detection with the tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
