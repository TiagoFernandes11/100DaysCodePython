import turtle, time

SNAKE_STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    snake_segments = []

    def __init__(self):
        for position in SNAKE_STARTING_POSITION:
            snake_part = turtle.Turtle()
            snake_part.penup()
            snake_part.shape("square")
            snake_part.color("white")
            snake_part.goto(position)
            self.snake_segments.append(snake_part)

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            snake_x_cord = self.snake_segments[i - 1].xcor()
            snake_y_cord = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(snake_x_cord, snake_y_cord)
        self.snake_segments[0].forward(MOVE_DISTANCE)
