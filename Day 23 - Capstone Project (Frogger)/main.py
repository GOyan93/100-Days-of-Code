import turtle as t
import time
import player_turtle
import level_tracker
from car import Car

WIDTH = 600
HEIGHT = 600
TOP_BORDER = HEIGHT/2
BOTTOM_BORDER = (WIDTH/2) * -1
LEFT_BORDER = (WIDTH/2) * -1
RIGHT_BORDER = WIDTH/2

canvas = t.Screen()
canvas.tracer(0)
canvas.setup(width=WIDTH, height=HEIGHT)
canvas.title("Turtle Crossing Game")


ttl = player_turtle.PlayerTurtle((0, BOTTOM_BORDER+20))
level_tracker = level_tracker.LevelTracker()


cars_list = []
for car_obj in range(0, 5):
    car = Car()
    cars_list.append(car)

canvas.listen()
canvas.onkeypress(fun= ttl.move_forward, key= "Up")
canvas.onkeypress(fun= ttl.move_back, key= "Down")
canvas.onkeypress(fun= ttl.move_left, key= "Left")
canvas.onkeypress(fun= ttl.move_right, key= "Right")
ttl.reset_position()

game_is_on = True

while game_is_on:
    #time.sleep(0.5)
    canvas.update()
    for vehicle in cars_list:
        vehicle.move()

    # Stops player from moving backward off screen
    if ttl.ycor() <= (BOTTOM_BORDER + 20):
        ttl.sety(BOTTOM_BORDER + 20)

    # Detects end of level.
    if ttl.ycor() >= (TOP_BORDER - 30):
        time.sleep(2)
        level_tracker.level_up()
        ttl.reset_position()
        for new_cars in range(0, 2):
            new_car = Car()
            cars_list.append(new_car)
        for vehicle in cars_list:
            vehicle.start_level()
        time.sleep(1)
        ttl.reset_position()

    #Reset car after reaching end.
    for vehicle in cars_list:
        if vehicle.xcor() <= -270:
            vehicle.reset_car()

    # Detects turtle collision with car:
    for vehicle in cars_list:
        if ttl.distance(vehicle) < 20:
            level_tracker.game_over()
            game_is_on = False






canvas.exitonclick()
