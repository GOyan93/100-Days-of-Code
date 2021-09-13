import turtle as t
import random

tim = t.Turtle()
canvas = t.Screen()
direction = 0
passes = 100
tim.speed(15)
canvas.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


for one_pass in (range(passes)):
    tim.color(random_colour())
    direction += (360 / passes)
    tim.setheading(direction)
    tim.circle(100)


canvas.exitonclick()