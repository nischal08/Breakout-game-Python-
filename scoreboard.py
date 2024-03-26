from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(self.score, align="center", font=("Courier", 32, "normal"))

    def update_points(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.update_scoreboard()
