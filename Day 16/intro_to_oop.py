import turtle

timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color('coral')
timmy.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)

my_screen.exitonclick()
