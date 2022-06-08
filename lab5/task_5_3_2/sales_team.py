from expenses_payer import ExpensesPayer


class SalesTeam(ExpensesPayer):
    def __init__(self):
        self.team = set()

    def remove_person(self, person: ExpensesPayer):
        self.team.discard(person)

    def add_person(self, person: ExpensesPayer):
        self.team.add(person)

    def pay_expenses(self, amount):
        for person in self.team:
            person.pay_expenses(amount)
