# use of *args

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  

# use of **kwargs

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# Another exapmle
def get_info(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f'{key}: {value}')

get_info(name="Rajesh", age=21, city="Pune", email="Vp4dM@example.com")


# another example

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Toyota", model="Camry", color="Blue", seats=5) 
print(my_car.make)       