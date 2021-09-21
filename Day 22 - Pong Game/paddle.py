from turtle import Turtle

COLOR = "white"
LENGTH = 1
WIDTH = 5
MOVE_INCREMENT = 60
SHAPE = "square"
SPEED = 20

class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.start_position = start_position
        self.speed(SPEED)

        self.reset_position()

    def reset_position(self):
        self.goto(self.start_position)

    def move_up(self):
        y_coor = self.ycor()
        y_coor += MOVE_INCREMENT
        self.goto(self.xcor(), y_coor)

    def move_down(self):
        y_coor = self.ycor()
        y_coor -= MOVE_INCREMENT
        self.goto(self.xcor(), y_coor)



