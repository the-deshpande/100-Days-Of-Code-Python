import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('The Turtle Crossing')
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_fwd, 'Up')
screen.onkeypress(player.move_bwd, 'Down')

new_car, mod_num = 0, 6
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.move()
    if new_car % mod_num == 0:
        new_car = 0
        cars.new_car()
    new_car += 1

    if player.ycor() > 280:
        player.teleport()
        cars.speed_up()
        scoreboard.level_up()
        if scoreboard.curr_level < 12 and scoreboard.curr_level % 2 == 0:
            mod_num -= 1

#     Collision Detection
    if cars.collide(player):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
