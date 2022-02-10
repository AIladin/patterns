from core.abstract_classes import Bus, Trolley, TrolleyBus, VehicleFactory


class VolvoBus(Bus):
    def get_purchase_cost(self) -> float:
        return 210

    def get_operation_cost(self, miles_run: float) -> float:
        return 31 * miles_run


class VolvoTrolley(Trolley):
    def get_purchase_cost(self) -> float:
        return 410

    def get_operation_cost(self, miles_run: float) -> float:
        return 11 * miles_run


class VolvoTrolleyBus(TrolleyBus):
    def get_purchase_cost(self) -> float:
        return 310

    def get_operation_cost(self, miles_run: float) -> float:
        return 21 * miles_run


class VolvoFactory(VehicleFactory):
    @property
    def name(self) -> str:
        return "Volvo"

    def create_bus(self) -> VolvoBus:
        return VolvoBus()

    def create_trolleybus(self) -> VolvoTrolleyBus:
        return VolvoTrolleyBus()

    def create_trolley(self) -> VolvoTrolley:
        return VolvoTrolley()
