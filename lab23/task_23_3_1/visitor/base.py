from abc import ABC, abstractmethod

import employee


class BaseVisitor(ABC):
    @abstractmethod
    def visit_manager(self, manager: employee.Manager):
        pass

    @abstractmethod
    def visit_salesperson(self, salesperson: employee.SalesPerson):
        pass

    @abstractmethod
    def visit_salesteam(self, salesteam: employee.EmployeeCollection):
        pass

    @abstractmethod
    def visit_itsupport(self, itsupport: employee.ITSupport):
        pass
