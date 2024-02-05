from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("pink")

    def move(self):
        self.left(270)
        self.forward(500)
