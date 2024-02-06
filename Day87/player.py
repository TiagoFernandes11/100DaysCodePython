from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(0, -280)


    def go_right(self):
        new_x = self.xcor() + 40.0
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 40.0
        self.goto(new_x, self.ycor())
