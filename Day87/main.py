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

game_is_on = True
i = 0
while game_is_on:
    ball.forward(10)
    screen.update()

exitonclick()

