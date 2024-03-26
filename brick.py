from turtle import Turtle


class Brick(Turtle):

    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=2.7, stretch_wid=1)
        self.penup()
        self.goto(coordinate)


