import colorgram
import turtle as t
import random

rgb_colors = []
colour_list = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_colour = (r, g, b)
    colour_list.append(new_colour)

#print(rgb_colors)
#print(colour_list)

ttl = t.Turtle()
canvas = t.Screen()
canvas.colormode(255)

dots = 100
rows = int(dots ** 0.5)
columns = int(dots ** 0.5)


for row in range(1, rows):
    for column in range(1, columns):
        ttl.penup()
        x_coor = row * 50
        y_coor = column * 50
        colour = random.choice(colour_list)
        ttl.setx(x_coor)
        ttl.sety(y_coor)
        ttl.pendown()
        ttl.dot(10, colour)


canvas.exitonclick()
