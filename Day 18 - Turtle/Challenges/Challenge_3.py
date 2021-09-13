import turtle as t
import random

tim = t.Turtle()
canvas = t.Screen()
colour_list = ["red", "blue", "green", "yellow", "purple", "pink", "black", "magenta", "grey", "orange"]

for x in range(3, 11):
    colour = random.choice(colour_list)
    tim.pencolor(colour)
    sides = x
    angle = 360 / sides
    for lines in range(x):
        tim.forward(100)
        tim.right(angle)

canvas.exitonclick()