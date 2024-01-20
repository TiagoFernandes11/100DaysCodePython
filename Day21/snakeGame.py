import turtle, snake, time, food, scoreboard
my_screen = turtle.Screen()
my_screen.bgcolor("black")
my_screen.setup(600, 600)
my_screen.tracer(0)
my_screen.title("Snake game")

game_is_on = True

my_snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(food) < 15:
        food.change_food_position()
        my_snake.add_segment()
        scoreboard.increase_score()

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in my_snake.snake_segments:
        if segment == my_snake.head:
            pass
        elif my_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

my_screen.exitonclick()
