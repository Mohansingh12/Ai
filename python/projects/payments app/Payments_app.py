from dataclasses import dataclass,asdict
import json
import datetime




@dataclass
class Transaction:
    amount: int
    account: int
    date: str
    type: str

class Operations:
    def __init__(self,file:str='transaction.json'):
        self.file = file
        with open(self.file, 'w') as f:
            json.dump([], f)

    def _load_all_data(self) -> list:
        """Helper method to read the current array out of the JSON file safely."""
        with open(self.file, 'r') as json_file:
            try:
                return json.load(json_file)
            except json.JSONDecodeError:
                return []


    def save_transaction(self,transaction:Transaction):
        data = self._load_all_data()
        data.append(asdict(transaction))

        with open(self.file, 'w') as f:
            json.dump(data, f, indent=4)


    def check_transaction(self,account:int):
        data = self._load_all_data()
        print("--- Current Transaction History ---")

        transactions=json.dumps(data, indent=2)
        for transaction in data:
            if transaction['account']==account:
                print(transaction)

class User:
    def __init__(self, operator : Operations,account:int):
        self.operator=operator

    def payment(self, amount:int, account_no:int, date,c_or_d:str='debit'):
        date_str = date.isoformat()
        transaction = Transaction(amount=amount,account=account_no,date=date_str,type=c_or_d)

        self.operator.save_transaction(transaction)

    def deposit(self, amount:int, account_no:int, date,c_or_d:str='credit'):
        date_str = date.isoformat()
        transaction = Transaction(amount=amount, account=account_no, date=date_str, type=c_or_d)

        self.operator.save_transaction(transaction)



if __name__ == '__main__':
    manger=Operations()
    new_user = User(manger,100)
    user = new_user.deposit(10000,110,datetime.date.today())
    user = new_user.payment(1000,100,datetime.date.today())
    manger.check_transaction(100)


