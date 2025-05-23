# check data type to help of type() function
print(type("Hello World"))
print(type(1))
print(type(1.1))
print(type(True))

# type conversion
print(type(str(1)))
print(type(int("20")))
print(type(float("1.1")))
print(type(bool("True")))

# Tip Calculator
bill = float(input("Enter the total amount: "))
print(bill)
tip = int(input("How much tip you want to give ? (10, 12, 15)% of total amount: "))
print(tip)
total = bill *(tip/100) + bill
print(total)
divide_into_persons = int(input("How many people to split the bill: "))
print(divide_into_persons)
each_person_pay = round(total / divide_into_persons, 2)
print(f"Each person should pay {each_person_pay}")