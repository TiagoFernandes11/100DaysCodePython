import turtle, time
my_screen = turtle.Screen()
my_screen.bgcolor("black")
my_screen.setup(600, 600)
my_screen.tracer(0)
my_screen.title("Snake game")

snake_starting_position = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []

for position in snake_starting_position:
    snake_part = turtle.Turtle()
    snake_part.penup()
    snake_part.shape("square")
    snake_part.color("white")
    snake_part.goto(position)
    snake_segments.append(snake_part)

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    for i in range(len(snake_segments) - 1, 0, -1):
        snake_x_cord = snake_segments[i-1].xcor()
        snake_y_cord = snake_segments[i - 1].ycor()
        snake_segments[i].goto(snake_x_cord, snake_y_cord)
    snake_segments[0].forward(20)

my_screen.exitonclick()
