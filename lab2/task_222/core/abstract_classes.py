from abc import ABC


class Bus(ABC):
    def get_purchase_cost(self) -> float:
        raise NotImplemented

    def get_operation_cost(self, miles_run: float) -> float:
        raise NotImplemented

    def total_bus_cost(self, miles_run: float) -> float:
        return self.get_purchase_cost() + self.get_operation_cost(miles_run)


class Trolley(ABC):
    def get_purchase_cost(self) -> float:
        raise NotImplemented

    def get_operation_cost(self, miles_run: float) -> float:
        raise NotImplemented

    def total_trolley_cost(self, miles_run: float) -> float:
        return self.get_purchase_cost() + self.get_operation_cost(miles_run)


class TrolleyBus(ABC):
    def get_purchase_cost(self) -> float:
        raise NotImplemented

    def get_operation_cost(self, miles_run: float) -> float:
        raise NotImplemented

    def total_trolleybus_cost(self, miles_run: float) -> float:
        return self.get_purchase_cost() + self.get_operation_cost(miles_run)


class VehicleFactory(ABC):

    @property
    def name(self) -> str:
        raise NotImplemented

    def create_bus(self) -> Bus:
        raise NotImplemented

    def create_trolleybus(self) -> TrolleyBus:
        raise NotImplemented

    def create_trolley(self) -> Trolley:
        raise NotImplemented
