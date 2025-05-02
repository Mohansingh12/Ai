#inheritance is a way to create a new class that is based on an existing class. The new class, called the derived class or child class, inherits attributes and methods from the existing class, called the base class or parent class. This allows for code reuse and the creation of a hierarchical relationship between classes.

class engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
class car(engine):
    def power(self):
        print(f"Engine horsepower: {self.horsepower}")

car1=car(500)
car1.power()

     