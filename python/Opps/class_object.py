# Class- class is a blue print of any object 
#object -object is a instance of a class with propeties 
#__init__ - its same as costructor intislise as soon as an bject is created

class bank:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    
    def withdrawl(self, amount):
        if self.balance <= amount:
            self.balance=self.balance-amount
            print(self.balance)
        else:
            print("inceficent amount")
    def credit(self,amount):
        self.balance=self.balance+amount
        print(self.balance)

user1=bank('mohan',500)
user1.credit(500)