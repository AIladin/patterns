from abc import ABC, abstractmethod
from typing import List

from employee import Employee
from staff_list_iterator import EmployeeIterator


class IterableCollection(ABC):
    @abstractmethod
    def __iter__(self):
        pass


class StaffList:
    def __init__(self, employees: List[Employee]):
        self.employees = employees

    def __iter__(self):
        return EmployeeIterator(self.employees)
