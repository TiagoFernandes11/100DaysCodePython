import turtle
from prettytable import PrettyTable
from turtle import Turtle, Screen

john = Turtle()
turtle.color("CadetBlue")
turtle.shape("turtle")
turtle.forward(200)

screen = Screen()
screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
table.align = "l"

print(table)
