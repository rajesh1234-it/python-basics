# Introduce Loop 
# for loop
for num in range(1, 11):
    print(num)

student_score = [150,124,234,123,90,80,70,60,50,40,30,20,10]
#sum score
total_sum = 0
for score in student_score:
    total_sum += score

print(total_sum)

#use sum() function
total_score = sum(student_score)
print(total_score)

# max score
highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(highest_score)

# use max() function
highest_score = max(student_score)
print(highest_score)

# while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# find max score
student_score = [150,124,234,123,90,80,70,60,50,40,30,20,10]
highest_score = 0
i = 0
while i < len(student_score):
    if student_score[i] > highest_score:
        highest_score = student_score[i]
    i += 1
print(highest_score)

# range() function
for num in range(1, 11):
    print(num * 2)

sum = 0
for num in range(1, 101):
    sum += num
print(sum)    

# fizz buzz game
for num in range(1, 101):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)  


 #  password generator
import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91 
for num in range(1, nr_letters + 1):
    random_letters = random.choice(letters)
    print(random_letters, end="")

for num in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    print(random_symbols, end="")

for num in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    print(random_numbers, end="")

# hard level
password = []
for num in range(1, nr_letters + 1):
    random_letters = random.choice(letters)
    password.append(random_letters)

for num in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    password.append(random_symbols)

for num in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password.append(random_numbers)

random.shuffle(password)
password = "".join(password)
print(password)