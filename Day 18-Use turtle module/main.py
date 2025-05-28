from turtle import Turtle, Screen
import random

jimmy = Turtle()

jimmy.shape("turtle")
jimmy.pensize(5)
# jimmy.color("red")
jimmy.speed(10)


# using while loop
'''i = 0
while True:
    if i == 4:
        break
    jimmy_a_turtle.forward(100)
    jimmy_a_turtle.right(90)
    i += 1
    
# using for loop
for _ in range(4):
    jimmy.forward(100)
    jimmy.right(90)

# dashes line

def new_func(jimmy):
    for _ in range(4):
        for _ in range(10):
          jimmy.forward(10)
          jimmy.penup()
          jimmy.forward(10)
          jimmy.pendown()
        jimmy.left(90)

new_func(jimmy)   

for _ in range(4):
   for _ in range(10):
     jimmy.forward(10)
     jimmy.color("red")
     jimmy.forward(10)
     jimmy.color("blue")
   jimmy.left(90)


# Draw different shapes
# manual method
for _ in range(3):
    jimmy.forward(100)
    jimmy.right(120)
    jimmy.color("red")
for _ in range(4):    
    jimmy.forward(100)
    jimmy.right(90)
    jimmy.color("blue")
for _ in range(5):    
    jimmy.forward(100)
    jimmy.right(72)
    jimmy.color("yellow")
for _ in range(6):    
    jimmy.forward(100)
    jimmy.right(60)
    jimmy.color("green")
for _ in range(7):    
    jimmy.forward(100)
    jimmy.right(51.43)
    jimmy.color("black")
for _ in range(8):    
    jimmy.forward(100)
    jimmy.right(45)
    jimmy.color("orange")
for _ in range(9):    
    jimmy.forward(100)
    jimmy.right(40)
    jimmy.color("pink")  

# draw a circle
for _ in range(360):
    jimmy.forward(1)
    jimmy.left(1)
    jimmy.color("red")
jimmy.right(90)'''

jimmy.circle(100)

#Using functions
# colors = ["red", "blue", "yellow", "green", "black", "orange", "pink"]
# def draw_shape(num_sides):
#    angle = 360 / num_sides
#    for _ in range(num_sides):
#       jimmy.forward(100)
#       jimmy.right(angle)  
   
# for shape_side_n in range(3,11):
# #    jimmy.color(colors[shape_side_n - 3])
#    jimmy.color(random.choice(colors))
#    draw_shape(shape_side_n)    


Screen = Screen()
Screen.exitonclick()
