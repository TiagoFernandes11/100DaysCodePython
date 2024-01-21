from turtle import Screen
from state_name import StateName
import pandas

data = pandas.read_csv("50_states.csv")

my_screen = Screen()
my_screen.tracer(0)
my_screen.setup(725, 491)
my_screen.bgpic("blank_states_img.gif")

for i in range(0, len(data["state"])):
    new_state_name = StateName()
    new_state_name.write_name(data["state"][i], (data["x"][i], data["y"][i]))
    my_screen.update()

my_screen.exitonclick()
