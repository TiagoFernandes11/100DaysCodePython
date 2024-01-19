from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()

my_screen.listen()


def move_fowards():
    my_turtle.forward(10)


def turn_right():
    my_turtle.right(90)

def turn_left():
    my_turtle.left(90)


my_screen.onkey(key="Up", fun=move_fowards)
my_screen.onkey(key="Right", fun=turn_right)
my_screen.onkey(key="Left", fun=turn_left)
my_screen.exitonclick()