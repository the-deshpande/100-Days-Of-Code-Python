from turtle import Turtle, Screen
import random


def draw_square(timmy: Turtle, side: int):
    for i in range(4):
        timmy.forward(side)
        timmy.right(90)


def draw_dashed_line(timmy: Turtle, size: int):
    for i in range(15):
        timmy.forward(size)
        timmy.penup()
        timmy.forward(size)
        timmy.pendown()


def draw_multiple_shapes(timmy: Turtle, side: int):
    for i in range(3, 11):
        angle = 360/i
        for j in range(i):
            timmy.forward(side)
            timmy.right(angle)
        timmy.pencolor(random.random(), random.random(), random.random())


def random_walk(timmy: Turtle, number_of_moves: int):
    for i in range(number_of_moves):
        timmy.pencolor(random.random(), random.random(), random.random())
        timmy.width(random.randint(1, 15))
        timmy.speed(random.randint(1, 10))
        timmy.forward(random.randint(1, 100))
        timmy.setheading(random.choice((0, 90, 180, 270)))


def draw_spirograph(timmy: Turtle, radius: int, gap: int):
    timmy.speed(0)
    timmy.pencolor(random.random(), random.random(), random.random())
    for _ in range(360//gap):
        timmy.circle(radius)
        timmy.left(gap)


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

# draw_square(timmy_the_turtle, 100)
# draw_dashed_line(timmy_the_turtle,10)
# draw_multiple_shapes(timmy_the_turtle, 100)
# random_walk(timmy_the_turtle, 100)
draw_spirograph(timmy_the_turtle, 100, 5)


screen = Screen()
screen.exitonclick()
