from turtle import Turtle
from brick import Brick


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.all_brick = []

    def create_bricks(self):
        for i in range(1, 13):
            for j in range(1, 6):
                self.all_brick.append(Brick(coordinate=(-420 + i * 70, 35 + j * 40)))
