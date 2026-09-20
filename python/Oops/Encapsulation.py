""" Encapsulation is a fundamental concept in object-oriented programming that refers to the bundling of data and methods that 
operate on that data within a single unit, typically a class. It helps in hiding the internal details of an object and exposing 
only the necessary information through well-defined interfaces. This promotes data integrity and security by preventing direct 
access to the internal state of an object from outside the class. """

class hide:
    
    def __init__(self,account_number,account_balance):
        self.account_number = account_number
        self.__account_balance = account_balance

    def get_account_balance(self):
        return self.__account_balance
        

acount = hide(123456789, 1000)
print(f"Account Number: {acount.account_number}")
print(f"Account Balance: {acount.get_account_balance()}")