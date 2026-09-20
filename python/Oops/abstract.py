""" Abstraction is basicly hiding the working mecnasim of a class and only showing the necessary details to the user. 
It allows users to interact with an object without needing to understand its internal complexities. 
Abstraction is achieved through abstract classes and interfaces, which define a blueprint for other classes to implement. 
This promotes code reusability and simplifies the interaction with complex systems by providing a clear and simplified interface. """

from abc import ABC, abstractmethod 

class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class credit_card_payment(payment):
    def pay(self, amount):
        print(f"Paid {amount} using credit card.")
class upi_payment(payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")


class payment_processor:
    def process_payment(self, payment_method: payment, amount):
        payment_method.pay(amount)

payment_processor = payment_processor()
credit_card = credit_card_payment()
upi = upi_payment() 
payment_processor.process_payment(credit_card, 100)
payment_processor.process_payment(upi, 200)