import turtle as t

ttl = t.Turtle()
canvas = t.Screen()


for x in range(50):
    ttl.forward(10)
    ttl.pen(pendown=False)
    ttl.forward(10)
    ttl.pen(pendown=True)



canvas.exitonclick()


