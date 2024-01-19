import turtle, snake, time
my_screen = turtle.Screen()
my_screen.bgcolor("black")
my_screen.setup(600, 600)
my_screen.tracer(0)
my_screen.title("Snake game")

game_is_on = True

my_snake = snake.Snake()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()


my_screen.exitonclick()
