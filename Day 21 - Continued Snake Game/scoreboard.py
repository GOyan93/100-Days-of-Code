from turtle import Turtle

FONT = "arial"
SIZE = 12
STYLE = "bold"
font_details = (FONT, SIZE, STYLE)



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.write(f"Score = {self.score}", align = "center", font= font_details)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align = "center", font= font_details)

    def get_score(self):
        return self.score

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font= font_details)
        self.goto(0, -20)
        self.write(f"Final Score: {self.get_score()}", align="center", font=font_details)

