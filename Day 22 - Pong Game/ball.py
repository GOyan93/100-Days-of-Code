from turtle import Turtle
import random
import time

BALL_SPEED = 0.04
BALL_SIZE = 1
BALL_COLOR = "white"
BALL_SHAPE = "circle"


# START_ANGLES = [30, 45, 135, 150, 210, 225, 315, 330]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.reset_position()
        self.ball_speed = BALL_SPEED


    def move(self):
        new_y = self.ycor() + self.move_y
        new_x = self.xcor() + self.move_x
        self.goto(new_x, new_y)
        time.sleep(self.ball_speed)

    def paddle_bounce(self):
        self.move_x *= -1
        self.ball_speed *= 0.9

    def floor_bounce(self):
        self.move_y *= -1

    def reset_position(self):
        self.move_x *= -1
        self.clear()
        self.goto(0, 0)
        self.ball_speed = BALL_SPEED
        time.sleep(1)
