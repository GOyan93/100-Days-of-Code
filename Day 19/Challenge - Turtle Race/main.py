import turtle as t
import random



SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
canvas = t.Screen()
canvas.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)





user_bet = canvas.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

for index in range(0, len(colors)):
    ttl = t.Turtle(shape = "turtle")
    ttl.color(colors[index])
    ttl.penup()
    y_pos = ((index - 3) * 20) + (10*index)
    ttl.goto(x = -230, y = y_pos)
    all_turtles.append(ttl)

if user_bet:
    is_race_on = True

while is_race_on:

    for ttl in all_turtles:
        if ttl.xcor() < 230:
            rand_distance = random.randint(0, 10)
            ttl.forward(rand_distance)
        else:
            is_race_on = False
            if user_bet.lower() == ttl.color()[0].lower():
                print("You win!")
            else:
                print("You lose.")
            print(f"The {ttl.color()[0]} turtle has won the race!")





canvas.exitonclick()