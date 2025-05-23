import another_module
print(another_module.name)

# import turtle

# jimmy = turtle.Turtle()
# print(jimmy)

from turtle import Turtle, Screen
# craete object
# simmy = Turtle()
# print(simmy)

# # turtle module
# simmy.shape("turtle")
# simmy.color("red")
# simmy.forward(100)
# # turtle module
# my_screen = Screen()
# # object attribute
# print(my_screen.canvheight)
# # object method
# my_screen.exitonclick()

# Python Turtle Star Pattern Program
import turtle
# Create screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color

star = turtle.Turtle()
star.color("yellow")     # Set turtle color
star.speed(10)           # Set drawing speed

# Draw a colorful starburst pattern
for i in range(50):  # 36 lines to make a full circle (360° / 10°)
    star.forward(100)
    star.right(144)  # Angle for a 5-pointed star
    star.forward(100)
    star.speed(5)
    star.left(170)   # Turn to make the starburst shape
    star.color("orange" if i % 2 == 0 else "red")  # Alternate colors

# Hide the turtle
star.hideturtle()

# Exit on click
screen.exitonclick()
