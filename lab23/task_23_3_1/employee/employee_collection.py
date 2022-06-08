from .base import BaseEmployee


class EmployeeCollection(BaseEmployee):
    def __init__(self, *args: BaseEmployee):
        self.employees = list(args)

    def add_employee(self, employee: BaseEmployee):
        self.employees.append(employee)

    def get_salary(self):
        return sum(employee.get_salary() for employee in self.employees)

    def accept(self, visitor):
        for employee in self.employees:
            employee.accept(visitor)
