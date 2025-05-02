#class variable- shared by all instances
class car:
    engine__power=500
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color
    def specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Engine Power: {self.engine__power}")

car1=car('honda','city','white')
car2=car('audi','a4','black')
car1.specs()
car2.specs()
