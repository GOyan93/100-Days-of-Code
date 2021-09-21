from turtle import Turtle

FONT= "arial"
FONT_SIZE= 50
FONT_STYLE= "bold"
FONT_COLOR = "white"
FONT_DETAILS = (FONT, FONT_SIZE, FONT_STYLE)


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.pencolor(FONT_COLOR)
        self.write(f"{self.score}", font= FONT_DETAILS)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", font= FONT_DETAILS)

    def game_over(self ):
        self.goto(0, 0)
        self.write("GAME OVER",align= "center", font= FONT_DETAILS)