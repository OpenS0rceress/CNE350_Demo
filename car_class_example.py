# Make a new python file called Car.py and add the first set of code to it. This will be an additional file to main.py and imported as a library
class Car:
    def __new__(cls, make, model):
        print("Create a new instance of Car")
        return super(Car, cls).__new__(cls)

    def __init__(self, make, model):
        print("Initialize new instance of Car")
        self.make = make
        self.model = model

    def __repr__(self) -> str:
        return f"{type(self).__name__}(Make = {self.make}, Model = {self.model})"

    def getMake(self):
        return self.make

    def setMake(self, make):
        self.make = make
        
   



# Now return to main.py
from car import Car

new_car = Car("Mazda", "Mazda3")
print(new_car)

new_car.setMake("Pontiac")
new_car.getMake()
print(new_car)

