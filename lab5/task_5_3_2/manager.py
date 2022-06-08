from expenses_payer import ExpensesPayer


class Manager(ExpensesPayer):
    def __init__(self, name: str):
        self.name = name

    def pay_expenses(self, amount):
        print(self.name + f" paid {amount}$")
