from turtle import Turtle
import random

class PlayerTurtle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.start_position = start_position
        self.reset_position()

    def reset_position(self):
        self.clear()
        self.goto(self.start_position)

    def move_forward(self):
        self.forward(35)

    def move_back(self):
        self.back(20)

    def move_left(self):
        x_pos = self.xcor()
        x_pos -= 20
        self.goto(x_pos, self.ycor())

    def move_right(self):
        x_pos = self.xcor()
        x_pos += 20
        self.goto(x_pos, self.ycor())