import turtle
import random

# Setup turtle screen and color mode
screen = turtle.Screen()
screen.bgcolor("black")
turtle.colormode(255)

# Create turtle
spiro = turtle.Turtle()
spiro.speed("fastest")

# Function to generate random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Function to draw a spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spiro.color(random_color())
        spiro.circle(100)
        spiro.setheading(spiro.heading() + size_of_gap)

# Draw the spirograph
draw_spirograph(5)  # 5-degree gap creates a full circle with many colored rings

# Exit on click
screen.exitonclick()
