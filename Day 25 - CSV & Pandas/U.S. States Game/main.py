# DONE Convert the guess to Title case
# DONE Check if the guess is among the 50 states
# DONE Write correct guesses onto the map
# DONE Use a loop to allow the user to keep guessing
# DONE Record the correct guesses in a list
# DONE Keep track of the score


import turtle
import pandas as pd

canvas = turtle.Screen()
canvas.title("U.S. States Game")
image = "blank_states_img.gif"
canvas.addshape(image)
turtle.shape(image)
state_writer = turtle.Turtle()
state_writer.penup()
state_writer.hideturtle()
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.goto(-300, 150)




df = pd.read_csv("50_states.csv")
states_names = df["state"].to_list()
guesses = []


canvas.tracer(0)

while len(guesses) < 50:
    score.write(f"{len(guesses)} / {len(states_names)}", align= "center", font= ("arial", 25, "bold"))
    canvas.update()
    answer_state = canvas.textinput(title="Guess the State", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_names:
            if state not in guesses:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("learn.csv")
        break
    if answer_state in states_names:
        print(f"Answer: {answer_state} is in states_names.")
        x_coor = int(df[df["state"] == answer_state].x)
        y_coor = int(df[df["state"] == answer_state].y)
        state_writer.goto(x_coor, y_coor)
        state_writer.write(answer_state, align= "center", font= ("arial, 8"))
        guesses.append(answer_state)
        score.clear()

# states to learn.csv. SAve missing states to the csv.








canvas.exitonclick()

