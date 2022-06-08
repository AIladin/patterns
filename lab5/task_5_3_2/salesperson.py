from expenses_payer import ExpensesPayer
from manager import Manager


class SalesPerson(ExpensesPayer):
    def __init__(self, name: str, manager: Manager):
        self.name = name
        self.manager = manager

    def pay_expenses(self, amount):
        print(self.name + f" paid {amount}$")
