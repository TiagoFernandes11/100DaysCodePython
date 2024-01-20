from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos_tupple):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1, 1)
        self.goto(pos_tupple[0], pos_tupple[1])
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + 20.0
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20.0
        self.goto(self.xcor(), new_y)
