from turtle import Screen
from spaceship import Spaceship
from aliens import Aliens
from scoreboard import Scoreboard
from time import sleep

window = Screen()
window.setup(width=500, height=700)
window.bgcolor('black')
window.title('Alien Shooter')
window.tracer(0)

ship = Spaceship()
aliens = Aliens()
scoreboard = Scoreboard()

window.listen()
window.onkeypress(ship.move_right, 'Right')
window.onkeypress(ship.move_left, 'Left')

tick = 0
game_is_on = True
while game_is_on:
    window.update()

    if tick % 5 == 0:
        ship.move_bullet()
        aliens.collision(ship.bullets)
        ship.collision()

        if aliens.check_won():
            scoreboard.game_over(0)
            game_is_on = False

    if tick % 80 == 0:
        ship.shoot()

    if tick % 100 == 0:
        aliens.vibrate()

    if tick == 500:
        aliens.advance()
        if aliens.check_lost():
            scoreboard.game_over(1)
            game_is_on = False

        tick = 0

    tick += 1
    sleep(0.01)

window.mainloop()
