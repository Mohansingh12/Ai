""" self is a reference to the current instance of the class. It is used to access variables that belong to the class. It is also 
used to call methods of the class. It is a convention to use self as the first parameter of instance methods in Python. It is not 
a keyword in Python, but it is a convention that is followed by most Python programmers."""

class car:
    def specs(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color
        
car1=car()
car1.specs('honda','city','white')

print(f"Brand: {car1.brand}, Model: {car1.model}, Color: {car1.color}")
    
