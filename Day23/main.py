import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "space")

game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if i == 5:
        car_manager.generate_car()
        i = 0
    i += 1
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 260:
        player.reset_positon()
        scoreboard.add_point()
        car_manager.clean()


screen.exitonclick()
