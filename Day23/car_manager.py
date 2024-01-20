from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# Create cars that are 20px high by 40px wide that are randomly generated along
# the y-axis and move to the left edge of the screen. No cars should be generated
# in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle)
# . Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough.

class CarManager:
    def __init__(self):
        self.all_cars = []

    def generate_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.color(COLORS[randint(0, 5)])
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(300, randint(-260, 300))
        self.all_cars.append(new_car)

    def clean(self):
        for car in self.all_cars:
            car.color("white")
            car.goto(500, 500)
        self.all_cars = []


    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
