from turtle import Turtle, Screen, colormode
import random

t = Turtle()
Screen = Screen()

colormode(255)
# colors = ["red", "blue", "yellow", "green", "black", "orange", "pink"]

def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    return (r, g, b)
     


directions = [0, 90, 180, 270]
t.speed("fastest")
t.pensize(10)  

for _ in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))


Screen.exitonclick()