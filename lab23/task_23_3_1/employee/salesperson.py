from .base import BaseEmployee


class SalesPerson(BaseEmployee):
    def __init__(self, salary: float):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def accept(self, visitor):
        visitor.visit_salesperson(self)
