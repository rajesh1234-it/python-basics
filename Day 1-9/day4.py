# text = "EPIC"

# print(f'{text}')         # EPIC
# print(f'{text:#>20}')     # ################EPIC
# print(f'{text:_^20}')     # _____________EPIC___________
# print(f'{text:.^20}')      #........EPIC........

# use random module
import random
random_integer = random.randint(1, 10)
print(random_integer)

random_float = round((random.random() * 5), 2)
print(random_float)

randon_float = random.uniform(1, 5)
print(randon_float)

# random list
# use of choice function in random module
# choise function return a random item from a list
fruits = ["apple", "banana", "cherry"]
picked_fruit = random.choice(fruits)
print(picked_fruit)

# haeds tails game
heads_or_tails = random.randint(0,1)
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

# dice game
dice = random.randint(1,6)
print(dice)

# choice game with list
friends = ["Alina", "Lily", "Sally", "John", "Mark", "Bob"]
# optoin 1
picked_friends = random.choice(friends)
print(picked_friends)
# option 2
print(friends[random.randint(0 ,5)])