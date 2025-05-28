
# And place a sound file named **`collect.wav`** in the same folder as your script.

# ---

### 🐢 Full Code With `pygame` Sound:

import turtle
import random
import time
import threading
import pygame  # ✅ Replaces playsound

# Initialize pygame mixer for sound
pygame.mixer.init()

# --- Setup screen ---
screen = turtle.Screen()
screen.title("🐢 Turtle Catch Challenge")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off auto animation

# --- Global variables ---
score = 0
time_left = 30  # Game time limit (seconds)
game_running = True

# --- Player (turtle) ---
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# --- Food (animated circle) ---
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# --- Obstacle ---
obstacle = turtle.Turtle()
obstacle.shape("square")
obstacle.color("black")
obstacle.penup()
obstacle.goto(0, 100)

# --- Score display ---
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.color("black")
pen.write("Score: 0  Time: 30", align="center", font=("Arial", 16, "bold"))

# --- Sound function ---
def play_sound():
    try:
        sound = pygame.mixer.Sound("collect.wav")  # ✅ Ensure this file exists
        sound.play()
    except:
        print("Sound file not found or error playing sound.")

# --- Player movement ---
def go_up():
    y = player.ycor()
    player.sety(y + 20)

def go_down():
    y = player.ycor()
    player.sety(y - 20)

def go_left():
    x = player.xcor()
    player.setx(x - 20)

def go_right():
    x = player.xcor()
    player.setx(x + 20)

# --- Keyboard bindings ---
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# --- Timer countdown ---
def countdown():
    global time_left, game_running
    while time_left > 0:
        time.sleep(1)
        time_left -= 1
        pen.clear()
        pen.write(f"Score: {score}  Time: {time_left}", align="center", font=("Arial", 16, "bold"))
    game_running = False
    pen.goto(0, 0)
    pen.write("⏰ Time's up! Game Over!", align="center", font=("Arial", 18, "bold"))

# Start countdown in background
threading.Thread(target=countdown, daemon=True).start()

# --- Game loop ---
while game_running:
    food.right(10)  # Animate food

    if player.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        score += 1
        play_sound()  # ✅ Play sound using pygame
        pen.clear()
        pen.write(f"Score: {score}  Time: {time_left}", align="center", font=("Arial", 16, "bold"))

    if player.distance(obstacle) < 20:
        score -= 1
        player.goto(0, 0)
        pen.clear()
        pen.write(f"Score: {score}  Time: {time_left}", align="center", font=("Arial", 16, "bold"))

    screen.update()

# Keep window open
screen.mainloop()
