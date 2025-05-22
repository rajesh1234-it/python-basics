print("Hello World")
# Next Line
print("Hello World\nHello World\nHello rajesh")
# Srtin concatenation
print("Hello" + " " + "Rajesh")

# input() function
print("Hello " + input("Enter your name: "))

# variable
name = input("Enter your name: ")
print("Byee " + name)

# len() function
print(len(input("Enter your village name: ")))

# chalenge
village_name = input("Enter your village name: ")
char_count = len(village_name)
print(char_count)

# Program to add two numbers
print("This program take numbers from user and add them")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum of " + str(num1) + " and " + str(num2) + " is " + str(sum))

# Another program 
print("The info about a Employee")
name = input("Enter your name:\n ")
Email = input("Enter your email:\n ")
age = input("Enter your age:\n ")
print("Your name is " + name + " and your email is " + Email + " and your age is " + age)

# calculate percentage
number = int(input("Enter a number which you want to calculate percentage: "))
percentage = int(input("How many percentage you want to calculate: "))
print(str(percentage) + " % of " + str(number) + " is " + str((percentage * number) / 100))
