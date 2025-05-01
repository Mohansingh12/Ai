#using attribute of diffrent classes in each other without inheritance
class car_rent:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
class users:
    def __init__(self,name,):
        self.name=name
    def rent(self,car):
        print(f"{self.name} is renting {car.name} for {car.price} per day")

car1=car_rent('audi',5000)
car2=car_rent('bmw',6000)       
car3=car_rent('mercedes',7000)
user1=users('mohan')    
user1.rent(car1)
