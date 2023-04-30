import numpy
import turtle
import random
wn = turtle.Screen()
wn.title("Box Item")
mu_pen = turtle.Turtle(

)
wn.bgcolor("black")
turtle.colormode(255)
mu_pen.pen()
mu_pen.goto(-100, -100)
mu_pen.pendown()

def my_squ(size):
    color = tuple\
        (numpy.random.randint(0, 255,3))
    mu_pen.pencolor(color)
    for i in range(4):
        mu_pen.fd(size)
        mu_pen.left(90)
        size = size - 5

i = 300
while i > 26:
    my_squ(i)
    i -= 20
turtle.exitonclick()
