from turtle import Turtle

class LevelTracker(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270, 270)
        self.color("black")
        self.write(f"Level: {self.level}", align= "center", font= ("arial", 10))

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align= "center", font= ("arial", 10))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font=("arial", 30, "bold"))