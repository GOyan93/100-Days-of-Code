import turtle as t
import random

tim = t.Turtle()
canvas = t.Screen()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turns = [0, 90, 180, 270]
tim.speed(20)
tim.pensize(7)

while True:
    direction = random.choice(turns)
    pen_colour = random.choice(colours)
    tim.pencolor(pen_colour)
    tim.setheading(direction)
    tim.forward(20)
