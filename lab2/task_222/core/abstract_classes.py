from abc import ABC, abstractmethod


class Bus(ABC):
    @abstractmethod
    def get_purchase_cost(self) -> float:
        pass

    @abstractmethod
    def get_operation_cost(self, miles_run: float) -> float:
        pass

    def total_bus_cost(self, miles_run: float) -> float:
        return self.get_purchase_cost() + self.get_operation_cost(miles_run)


class Trolley(ABC):
    @abstractmethod
    def get_purchase_cost(self) -> float:
        pass

    @abstractmethod
    def get_operation_cost(self, miles_run: float) -> float:
        pass

    def total_trolley_cost(self, miles_run: float) -> float:
        return self.get_purchase_cost() + self.get_operation_cost(miles_run)


class TrolleyBus(ABC):
    @abstractmethod
    def get_purchase_cost(self) -> float:
        pass

    @abstractmethod
    def get_operation_cost(self, miles_run: float) -> float:
        pass

    def total_trolleybus_cost(self, miles_run: float) -> float:
        return self.get_purchase_cost() + self.get_operation_cost(miles_run)


class VehicleFactory(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def create_bus(self) -> Bus:
        pass

    @abstractmethod
    def create_trolleybus(self) -> TrolleyBus:
        pass

    @abstractmethod
    def create_trolley(self) -> Trolley:
        pass
