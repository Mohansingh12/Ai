# Class - A class is a blueprint of any object.
# Object - An object is an instance of a class with properties.
# __init__ - It's the same as a constructor, initialized as soon as an object is created.

class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(self.balance)
        else:
            print("Insufficient amount")
    
    def credit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)

user1 = Bank('Mohan', 500)
user1.credit(500)