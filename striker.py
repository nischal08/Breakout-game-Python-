from turtle import Turtle

STICKER_Y_POSITION = -230
STRIKER_SPEED = 25


class Striker(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto((self.xcor(), STICKER_Y_POSITION))

    def go_left(self):
        self.penup()
        if (self.xcor() - STRIKER_SPEED) > (-360):
            self.goto((self.xcor() - STRIKER_SPEED, STICKER_Y_POSITION))

    def go_right(self):
        self.penup()
        if (self.xcor() + STRIKER_SPEED) < 360:
            self.goto((self.xcor() + STRIKER_SPEED, STICKER_Y_POSITION))
