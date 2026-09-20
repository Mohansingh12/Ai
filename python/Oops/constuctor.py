""" constructor  is method that call it self when we create an object of the class. It is used to initialize the attributes of the class. 
It is called automatically when we create an object of the class. It is defined using the __init__() method. It is a special method that is 
called when an object is created."""

class car:
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color

car1=car('honda','city','white')
print(f"Brand: {car1.brand}, Model: {car1.model}, Color: {car1.color}")

