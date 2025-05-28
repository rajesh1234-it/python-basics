# Snake game

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

'''sagment_1 = Turtle("square")
sagment_1.color("white")
sagment_1.goto(0, 0)

sagment_2 = Turtle("square")
sagment_2.color("white")
sagment_2.goto(20, 0)

sagment_3 = Turtle("square")
sagment_3.color("white")
sagment_3.goto(40, 0)'''


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
# the screen tracer use in order to turn off the animation
screen.tracer(0)


start_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
        
    # detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()
        
    # # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()




