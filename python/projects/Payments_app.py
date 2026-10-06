from dataclasses import dataclass
import json
from python.projects.personal_finance_2 import transaction


@dataclass
class Transaction:
    amount: int
    account: int
    date: str
    type: str


class User(transaction):
    def payment(self, amount:int, account_no:int, date:str,c_or_d:str):
        super().__init__(amount,account_no,date,c_or_d)


    def deposit(self, amount:int, account_no:int, date:str,c_or_d:str):
        super().__init__(amount, account_no, date,c_or_d)

class Deposit(transaction):
    def payment(self, amount:int, account_no:int, date:str,c_or_d:str):
        super().__init__(amount, account_no, date, c_or_d)



if __name__ == '__main__':
    option=input("1 for login and /n 2 for deposit")
    match option :
        case 1 :
            session=user()
            uses=print("1:payment /n 2: deposit /n 3:balance")
            match option :
                case 1 :
                    user
