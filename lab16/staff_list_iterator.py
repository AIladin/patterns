from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def has_more(self):
        pass


class EmployeeIterator(Iterator):
    def __init__(self, employee_list):
        self.collection = employee_list
        self.iteration_state = 0

    def has_more(self):
        return self.iteration_state < len(self.collection)

    def __next__(self):
        if not self.has_more():
            print(f"EmployeeIterator raised stop iteration.")
            raise StopIteration
        print(
            f"Getting next employee using EmployeeIterator. Current iteration state {self.iteration_state}"
        )
        val = self.collection[self.iteration_state]
        self.iteration_state += 1
        return val
