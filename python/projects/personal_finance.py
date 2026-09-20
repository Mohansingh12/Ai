from dataclasses import dataclass
expenses = []
@dataclass
class Expense:
    id: int
    category: str
    amount: float
    date: str
class AddExpense(Expense):
    def __init__(self, id: int, category: str, amount: float, date: str):
        super().__init__(id, category, amount, date)
        expenses.append(self)
class ViewExpenses:
    def __init__(self):
        for expense in expenses:
            print(f"ID: {expense.id}, Category: {expense.category}, Amount: {expense.amount}, Date: {expense.date}")
class SearchExpenses:
    def __init__(self, category: str):
        found = False
        for expense in expenses:
            if expense.category == category:
                print(f"ID: {expense.id}, Category: {expense.category}, Amount: {expense.amount}, Date: {expense.date}")
                found = True
        if not found:
            print("No expenses found in this category.")
class DeleteExpense:
    def __init__(self, id: int):
        global expenses
        expenses = [expense for expense in expenses if expense.id != id]
        print(f"Expense with ID {id} has been deleted.")
class ShowStatistics:
    def __init__(self):
        total_expenses = sum(expense.amount for expense in expenses)
        print(f"Total Expenses: {total_expenses}")
        total_income = sum(expense.amount for expense in expenses if expense.amount > 0)
        print(f"Total Income: {total_income}")
class AddIncome(Expense):
    def __init__(self, id: int, category: str, amount: float, date: str):
        super().__init__(id, category, amount, date)
        expenses.append(self)
class ShowBalance:
    def __init__(self):
        total_balance = sum(expense.amount for expense in expenses)
        print(f"Total Balance: {total_balance}")

    

option = input("choise you option 1. Add expense 2. View expenses 3. Search expenses 4. Delete expense 5. Show statistics 6. Add income 7. Show balance 8. Exit")

match option:
    case "1":
        id = len(expenses) + 1
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))*-1
        date = input("Enter expense date: ")
        expense = AddExpense(id, category, amount, date)
    case "2":
        view = ViewExpenses()
    case "3":
        category = input("Enter category to search: ")      
        search = SearchExpenses(category)
    case "4":
        id = int(input("Enter expense ID to delete: "))
        delete = DeleteExpense(id)
    case "5":
        stats = ShowStatistics()    
    case "6":
        id = len(expenses) + 1
        category = input("Enter income category: ")
        amount = float(input("Enter income amount: "))
        date = input("Enter income date: ")
        income = AddIncome(id, category, amount, date)
    case "7":
        balance = ShowBalance()
    case "8":
        print("Exiting...")