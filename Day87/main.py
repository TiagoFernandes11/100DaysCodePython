import time
from turtle import *

from Day87.player import Player
from Day87.target_manager import TargetManager
from ball import Ball

screen = Screen()
screen.setup(width=800, height=650)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

ball = Ball()

player = Player()

targets = TargetManager()

screen.listen()
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")

game_is_on = True
i = 0
while game_is_on:
    screen.update()
    time.sleep(0.009)
    ball.move()

    if ball.xcor() > 385 or ball.xcor() < -385:
        ball.bounce_x()

    if ball.distance(player) < 30:
        ball.bounce_y()

    for target in targets.all_targets:
        if ball.distance(target) < 30:
            ball.bounce_y()
            target.reset()

exitonclick()

