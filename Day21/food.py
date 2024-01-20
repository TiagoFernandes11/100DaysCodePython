from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        rand_x_cord = random.randint(-280, 280)
        rand_y_cord = random.randint(-280, 280)
        self.goto(rand_x_cord, rand_y_cord)

    def change_food_position(self):
        rand_x_cord = random.randint(-250, 250)
        rand_y_cord = random.randint(-250, 250)
        self.goto(rand_x_cord, rand_y_cord)