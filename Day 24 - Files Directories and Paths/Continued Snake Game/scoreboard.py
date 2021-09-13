from turtle import Turtle
import time

FONT = "arial"
SIZE = 12
STYLE = "bold"
font_details = (FONT, SIZE, STYLE)




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-50, 280)
        self.write(f"Score = {self.score}", align = "center", font= font_details)
        self.goto(50, 280)
        self.write(f"Highscore = {self.highscore}", align="center", font= font_details)

    def add_score(self):
        self.score += 1
        self.clear()
        self.goto(-50, 280)
        self.write(f"Score = {self.score}", align = "center", font= font_details)
        self.goto(50, 280)
        self.write(f"Highscore = {self.highscore}", align="center", font=font_details)

    def get_score(self):
        return self.score

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font= font_details)
        self.goto(0, -20)
        self.write(f"Final Score: {self.get_score()}", align="center", font=font_details)
        time.sleep(2)
        self.clear()

    def get_highscore(self):
        return self.highscore

    def update_highscore(self):
        with open("data.txt", mode= "w") as file:
            file.write(f"{self.score}")
        with open("data.txt", mode= "r") as file:
            self.highscore = int(file.read())

    def reset_score(self):
        self.clear()
        self.score = 0
        self.goto(-50, 280)
        self.write(f"Score = {self.score}", align="center", font=font_details)
        self.goto(50, 280)
        self.write(f"Highscore = {self.highscore}", align="center", font=font_details)
