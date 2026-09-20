""" same method name but different implementation is called polymorphism. It is used to achieve code reusability and to make the code 
more readable and maintainable. It is also used to achieve method overloading and method overriding. """

class hoda_car:
    def specs(self):
        print("Brand: honda, Model: city, Color: white")

class toyota_car:
    def specs(self):
        print("Brand: toyota, Model: camry, Color: black")

car1=hoda_car()
car2=toyota_car()
cars=[car1,car2]
for car in cars:
    car.specs()