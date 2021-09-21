import turtle as t

ttl = t.Turtle()
canvas = t.Screen()

def move_forward():
    ttl.forward(10)

def move_back():
    ttl.back(10)

def turn_left():
    ttl.left(10)

def turn_right():
    ttl.right(10)

def reset_screen():
    global ttl, canvas
    ttl.clear()
    ttl.penup()
    ttl.home()
    ttl.pendown()

canvas.listen()
canvas.onkeypress(fun=move_forward, key="Up")
canvas.onkeypress(fun=move_back, key="Down")
canvas.onkeypress(fun=turn_left, key= "Left")
canvas.onkeypress(fun=turn_right, key="Right")
canvas.onkeypress(fun=reset_screen, key= "space")

canvas.exitonclick()
