# if-else statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")


# if-elif-else statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")


# use of % operator
print(12 % 5)
print(12 / 5)
print(12 // 5)

# check even-odd number
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("THis is even number.")
else:
    print("THis is odd number.")

#nested if-else statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age > 18:
        bill = 5
        print("You can ride the rollercoaster!")
    else:
        print("Sorry, yuor age is less than 18, you can't ride.")
else:
    print("Sorry, you have to grow taller before you can ride.")

#pizza delivery program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"Your final bill is: ${bill}")

# if-else based on logical operators
print("weightlifting program")
height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))
if weight > 90 or weight < 80 and height > 170:
    print("You are eligible for weightlifting in 90kg category.") 
elif weight > 80 or weight < 70 and height > 160:
    print("You are eligible for weightlifting in 80kg category.") 
elif weight > 70 or weight < 60 and height > 150:
    print("You are eligible for weightlifting in 70kg category.")   
else:
    print("You are not eligible for weightlifting.")


#treaseure game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right' ").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:   
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fall into a hole. Game Over.")   