import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

TOP_BORDER = 300
BOTTOM_BORDER = -300
LEFT_BORDER = -400
RIGHT_BORDER = 400

canvas = t.Screen()
canvas.setup(width= (RIGHT_BORDER*2), height= (TOP_BORDER*2))
canvas.bgcolor("black")
canvas.title("PONG")

left_paddle_pos = (LEFT_BORDER + 20, 0)
right_paddle_pos = (RIGHT_BORDER - 20, 0)
left_score_pos = (-80, TOP_BORDER - 80)
right_score_pos = (50, TOP_BORDER - 80)


canvas.tracer(0)
# Draws centre line.
centre_line = t.Turtle()
centre_line.penup()
centre_line.hideturtle()
centre_line.pencolor("white")
centre_line.pensize(2)
centre_line.goto(0, BOTTOM_BORDER)
centre_line.setheading(90)
centre_line.speed("fastest")
while centre_line.ycor() <= TOP_BORDER:
    centre_line.pendown()
    centre_line.forward(20)
    centre_line.penup()
    centre_line.forward(20)

score_left = Scoreboard(left_score_pos)
score_right = Scoreboard(right_score_pos)
left_paddle = Paddle(left_paddle_pos)
right_paddle = Paddle(right_paddle_pos)
ball = Ball()

canvas.listen()
canvas.onkeypress(left_paddle.move_up, "w")
canvas.onkeypress(left_paddle.move_down, "s")
canvas.onkeypress(right_paddle.move_up, "Up")
canvas.onkeypress(right_paddle.move_down, "Down")

canvas.update()
game_is_on = True
time.sleep(3)
while game_is_on:
    # time.sleep(0.1)
    canvas.update()
    ball.move()

    # Detect ball collision with wall.
    if  ball.ycor() >= (TOP_BORDER - 20):
        ball.floor_bounce()
    if  ball.ycor() < (BOTTOM_BORDER + 20):
        ball.floor_bounce()

    # Detect ball collision with left paddle.
    if ball.xcor() < (LEFT_BORDER + 40) and left_paddle.distance(ball) < 50:
        ball.paddle_bounce()

    # Detect ball collision with right paddle.
    if (ball.xcor() > (RIGHT_BORDER - 40)) and right_paddle.distance(ball) < 50:
        ball.paddle_bounce()

    # Detect ball collision with left border.
    if ball.xcor() < LEFT_BORDER:
        score_right.increase_score()
        left_paddle.reset_position()
        right_paddle.reset_position()
        ball.reset_position()

    # Detect ball collision with right border
    if ball.xcor() > RIGHT_BORDER:
        score_left.increase_score()
        left_paddle.reset_position()
        right_paddle.reset_position()
        ball.reset_position()

    # Detect game over condition.
    if score_left.score == 10 or score_right.score == 10:
        ball.hideturtle()
        left_paddle.hideturtle()
        right_paddle.hideturtle()
        score_left.game_over()
        game_is_on = False

    # Detect paddle collisions with borders.
    if right_paddle.ycor() < (BOTTOM_BORDER + 20):
        right_paddle.goto(right_paddle.xcor(), BOTTOM_BORDER+20)
    if right_paddle.ycor() > (TOP_BORDER - 20):
        right_paddle.goto(right_paddle.xcor(), TOP_BORDER-20)

    if left_paddle.ycor() < (BOTTOM_BORDER + 20):
        left_paddle.goto(left_paddle.xcor(), BOTTOM_BORDER+20)
    if left_paddle.ycor() > (TOP_BORDER - 20):
        left_paddle.goto(left_paddle.xcor(), TOP_BORDER-20)



canvas.exitonclick()
