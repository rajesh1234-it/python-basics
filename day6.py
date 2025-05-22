# function in python
def greet(name):
    print("Hello " + name)

greet("Rajesh")

def add(num1, num2):
    print(num1 + num2)

add(2, 3)       

# A simple project base on fuction, loop and if-else statement

def tip_calculator():
    bill = float(input("Enter the total amount: "))
    tip = int(input("How much tip you want to give ? (10, 12, 15)% of total amount: "))
    total = bill *(tip/100) + bill
    divide_into_persons = int(input("How many people to split the bill: "))
    each_person_pay = round(total / divide_into_persons, 2)
    print(f"Each person should pay {each_person_pay}")
    
tip_calculator()
