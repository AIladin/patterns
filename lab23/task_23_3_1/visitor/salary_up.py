import employee

from .base import BaseVisitor


class SalaryUpVisitor(BaseVisitor):
    def __init__(self, rate: float):
        self.rate = rate

    def visit_manager(self, manager: employee.Manager):
        manager.set_salary(manager.get_salary() * (1 + self.rate))

    def visit_salesperson(self, salesperson: employee.SalesPerson):
        salesperson.set_salary(salesperson.get_salary() * (1 + self.rate))

    def visit_salesteam(self, salesteam: employee.EmployeeCollection):
        salesteam.set_salary(salesteam.get_salary() * (1 + self.rate))

    def visit_itsupport(self, itsupport: employee.ITSupport):
        itsupport.set_salary(itsupport.get_salary() * (1 + self.rate))
