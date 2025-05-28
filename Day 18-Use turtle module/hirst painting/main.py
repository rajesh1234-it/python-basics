# use to generate color from image
# import colorgram

# # Extract 10 colors from an image
# colors = colorgram.extract('hirst-severed-spots.jpg', 30)  # Make sure this image exists in your project folder

# # Print the RGB values of the extracted colors
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     print((r, g, b))

import turtle
import random

# Color list (paste from colorgram result or use sample)
color_list = [
    (239, 245, 241), (240, 233, 210), (202, 158, 109),
    (237, 241, 247), (150, 75, 49), (140, 184, 171),
    (222, 202, 137), (135, 86, 105), (60, 95, 122),
    (199, 144, 160), (147, 156, 176), (15, 33, 61),
    (163, 80, 47), (13, 22, 33), (89, 147, 126)
]

# Setup turtle
turtle.colormode(255)
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

# Starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Draw 10x10 grid of dots
for dot_count in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Keep window open
screen = turtle.Screen()
screen.exitonclick()
