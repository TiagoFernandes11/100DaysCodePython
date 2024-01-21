from turtle import Turtle


class StateName(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.1, 0.1)
        self.color("white")

    def write_name(self, state_name, directions):
        self.goto(directions[0], directions[1])
        self.color("black")
        self.write(state_name, align="center")
