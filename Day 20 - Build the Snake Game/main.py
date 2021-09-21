import turtle as t
import time, snake


canvas = t.Screen()
canvas.setup(width = 600, height = 600)
canvas.bgcolor("black")
canvas.title("My Snake Game")
canvas.tracer(0)

snake_1 = snake.Snake()

canvas.listen()
canvas.onkeypress(fun= snake_1.move_left, key= "Left")
canvas.onkeypress(fun= snake_1.move_right, key= "Right")
canvas.onkeypress(fun= snake_1.move_up, key= "Up")
canvas.onkeypress(fun= snake_1.move_down, key= "Down")

game_is_on = True
while game_is_on:
    canvas.update()
    time.sleep(0.1)

    snake_1.move()






canvas.exitonclick()