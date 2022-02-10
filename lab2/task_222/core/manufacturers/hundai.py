from core.abstract_classes import Bus, Trolley, TrolleyBus, VehicleFactory


class HyundaiBus(Bus):
    def get_purchase_cost(self) -> float:
        return 219

    def get_operation_cost(self, miles_run: float) -> float:
        return 31 * miles_run


class HyundaiTrolley(Trolley):
    def get_purchase_cost(self) -> float:
        return 419

    def get_operation_cost(self, miles_run: float) -> float:
        return 11 * miles_run


class HyundaiTrolleyBus(TrolleyBus):
    def get_purchase_cost(self) -> float:
        return 319

    def get_operation_cost(self, miles_run: float) -> float:
        return 21 * miles_run


class HyundaiFactory(VehicleFactory):

    @property
    def name(self) -> str:
        return "Hundai"

    def create_bus(self) -> HyundaiBus:
        return HyundaiBus()

    def create_trolleybus(self) -> HyundaiTrolleyBus:
        return HyundaiTrolleyBus()

    def create_trolley(self) -> HyundaiTrolley:
        return HyundaiTrolley()
