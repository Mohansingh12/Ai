from dataclasses import dataclass


book=[]
@dataclass
class Transaction:
    id :int
    category: str
    amount: float
    description: str
    type: str

@dataclass
class Expense(Transaction):
    pass

@dataclass
class Income(Transaction):
    pass

class Debit:
    def __init__(self, transaction: Transaction):
        book.append(transaction)
        print(f"Transaction added: {transaction}")
class Credit:
    def __init__(self, transaction: Transaction):
        book.append(transaction)
        print(f"Transaction added: {transaction}")

while True:
    option = input("Choose your option 1. Add expense 2. Add income 3. View transactions 4. balance 5. Exit")
    match option:
        case "1":
            id = len(book) + 1
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            transaction = Expense(id, category, -amount, description, "Expense")
            debit = Debit(transaction)
        case "2":
            id = len(book) + 1
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            transaction = Income(id, category, amount, description, "Income")
            credit = Credit(transaction)
        case "3":
            for transaction in book:
                print(f"ID: {transaction.id}, Category: {transaction.category}, Amount: {transaction.amount}, Description: {transaction.description}, Type: {transaction.type}")
        case "4":
            for transaction in book:
                if transaction.type == "Expense":
                    balance=0
                    balance-=transaction.amount
                else:
                    balance+=transaction.amount
                print(f"Your balance: {balance}")
        case "5":
            print("Exiting the program.")
            break