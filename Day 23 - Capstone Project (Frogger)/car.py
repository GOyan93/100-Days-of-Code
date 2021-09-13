from turtle import Turtle
import random, time

colors = ["red", "yellow", "blue", "green", "purple", "pink", "orange", "black"]
y_positions = []
for y_coor in range(-230, 200, 20):
    y_positions.append(y_coor)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        car_color = random.choice(colors)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(car_color)
        #y_pos = random.choice(y_positions)
        self.setheading(180)
        self.start_level()
        self.car_speed = 0.5

    def move(self):
        self.forward(self.car_speed)


    def speed_up(self):
        self.car_speed *= 1.2

    def reset_car(self):
        self.clear()
        y_posit = random.choice(y_positions)
        self.goto(300, y_posit)

    def start_level(self):
        self.clear()
        x_posit = random.randint(-300, 300)
        y_posit = random.choice(y_positions)
        self.goto(x_posit, y_posit)
