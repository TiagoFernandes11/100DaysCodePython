import turtle, snake, time
my_screen = turtle.Screen()
my_screen.bgcolor("black")
my_screen.setup(600, 600)
my_screen.tracer(0)
my_screen.title("Snake game")

game_is_on = True

my_snake = snake.Snake()

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()


my_screen.exitonclick()
