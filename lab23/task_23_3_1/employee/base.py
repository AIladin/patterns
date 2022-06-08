from abc import ABC, abstractmethod


class BaseEmployee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass
