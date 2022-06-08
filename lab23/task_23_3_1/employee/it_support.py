from .base import BaseEmployee


class ITSupport(BaseEmployee):
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def accept(self, visitor):
        visitor.visit_itsupport(self)
