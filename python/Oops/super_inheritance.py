class engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
class car(engine):
    def __init__(self,brand,model,color,horsepower):
        super().__init__(horsepower)
        
        self.brand=brand
        self.model=model
        self.color=color
    def specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Horsepower: {self.horsepower}")

car1=car('honda','city','white',500)
car1.specs()


     