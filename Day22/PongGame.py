from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time
import paddle

game_screen = Screen()
game_screen.setup(800, 600)
game_screen.bgcolor("black")
game_screen.title("Pong")
game_screen.tracer(0)

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


game_screen.listen()
game_screen.onkey(r_paddle.go_up ,"Up")
game_screen.onkey(r_paddle.go_down ,"Down")
game_screen.onkey(l_paddle.go_up ,"w")
game_screen.onkey(l_paddle.go_down ,"s")


game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.009)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

game_screen.exitonclick()
