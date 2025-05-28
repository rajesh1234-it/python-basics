# Turtlrs racing game

from turtle import Turtle, Screen
import random


screen = Screen()

all_turtles = []
is_race_on = False
screen.setup(width = 600, height = 600)
user_bet = screen.textinput(title = "Make a bet", prompt = "Which turtle will win the race? Enter a color: ")
# print(user_bet)
t_colors = ["red", "pink", "orange", "yellow", "green", "blue", "purple"]
y_positions = [150, 100, 50, 0, -50, -100, -150]
# all_turtles = []

# this is the object oriented approach
for index in range(len(t_colors)):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(t_colors[index])
    new_turtle.penup()
    new_turtle.goto(x = -290, y = y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


'''# this is the procedural approach
pim = Turtle()
pim.shape("turtle")
pim.color("black")
pim.penup()
pim.goto(x = -290, y = 100)


tim = Turtle()
tim.shape("turtle")
tim.color("pink")
tim.penup()
tim.goto(x = -290, y = 50)


tom = Turtle()
tom.shape("turtle")
tom.color("green")
tom.penup()
tom.goto(x = -290, y = 0)


jerry = Turtle()    
jerry.shape("turtle")
jerry.color("yellow")
jerry.penup()
jerry.goto(x = -290, y = -50)


bob = Turtle()
bob.shape("turtle")
bob.color("orange")
bob.penup()
bob.goto(x = -290, y = -100)


lili = Turtle()
lili.shape("turtle")
lili.color("gray")
lili.penup()
lili.goto(x = -290, y = -150)'''





screen.exitonclick()