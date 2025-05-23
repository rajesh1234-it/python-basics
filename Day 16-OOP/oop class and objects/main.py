# Example of class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def full_info(self):
        return f"{self.name} is {self.age} years old"
            

person_1 = Person("Rajesh", 20)
person_2 = Person("Rahul", 22)

# print(person_1.name)
# print(person_1.age)
# print(person_2.name)
# print(person_2.age)
print(person_1.full_info())
print(person_2.full_info())

# Challenge
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


calc_1 = Calculator(10, 5)
print(calc_1.add())               # Output: 15
print(calc_1.subtract())          # Output: 5
print(calc_1.multiply())          # Output: 50
print(calc_1.divide())            # Output: 2                       