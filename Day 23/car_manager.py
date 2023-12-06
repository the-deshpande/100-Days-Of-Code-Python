from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
MAX_CARS = 30


class CarManager:

    def __init__(self):
        self.cars = list()
        self.move_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        if len(self.cars) == MAX_CARS:
            self.cars = self.cars[1:]
        self.cars.append(Turtle('square'))
        self.cars[-1].shapesize(stretch_wid=1, stretch_len=2)
        self.cars[-1].setheading(180)
        self.cars[-1].color(random.choice(COLORS))
        self.cars[-1].penup()
        self.cars[-1].goto((300, random.randint(-250, 250)))

    def move(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT

    def collide(self, player: Turtle):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
