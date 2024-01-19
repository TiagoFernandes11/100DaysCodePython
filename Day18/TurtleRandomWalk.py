import turtle
import random


# Function to generate a random color
def random_color():
    return random.random(), random.random(), random.random()


# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Tartaruguinha doidinha")

# Create a turtle
walker = turtle.Turtle()
walker.speed(2)


# Function to perform a random walk with 90-degree angles
def random_walk_90_degrees(steps):
    for _ in range(steps):
        walker.color(random_color())  # Set a random color
        direction = random.choice([0, 90, 180, 270])  # Choose a random 90-degree angle
        walker.setheading(direction)
        walker.forward(20)


# Set the number of steps for the random walk
num_steps = 100

# Perform the random walk
random_walk_90_degrees(num_steps)

# Close the window on click
screen.exitonclick()
