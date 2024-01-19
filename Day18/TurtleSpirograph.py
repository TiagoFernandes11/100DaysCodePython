import turtle, random

my_turtle = turtle.Turtle()


def random_color():
    return random.random(), random.random(), random.random()


for i in range(8):
    my_turtle.color(random_color())
    my_turtle.circle(50)
    my_turtle.left(45)


input()