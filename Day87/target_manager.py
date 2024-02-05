from random import randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class TargetManager:
    def __init__(self):
        self.all_targets = []
        self.generate_board()

    def generate_target(self, x: int, y: int):
        new_target = Turtle()
        new_target.penup()
        new_target.shape("square")
        new_target.color(COLORS[randint(0, 5)])
        new_target.shapesize(stretch_wid=0.952380952380952, stretch_len=3.80952380952381)
        new_target.goto(x, y)
        self.all_targets.append(new_target)

    def generate_board(self):
        for j in range(0, 5):
            for i in range(-5, 5):
                self.generate_target((i*80) + 40, 300 - (j*22))
