from core.abstract_classes import Bus, Trolley, TrolleyBus, VehicleFactory


class SkodaBus(Bus):
    def get_purchase_cost(self) -> float:
        return 200

    def get_operation_cost(self, miles_run: float) -> float:
        return 30 * miles_run


class SkodaTrolley(Trolley):
    def get_purchase_cost(self) -> float:
        return 400

    def get_operation_cost(self, miles_run: float) -> float:
        return 10 * miles_run


class SkodaTrolleyBus(TrolleyBus):
    def get_purchase_cost(self) -> float:
        return 300

    def get_operation_cost(self, miles_run: float) -> float:
        return 20 * miles_run


class SkodaFactory(VehicleFactory):

    @property
    def name(self) -> str:
        return "Skoda"

    def create_bus(self) -> SkodaBus:
        return SkodaBus()

    def create_trolleybus(self) -> SkodaTrolleyBus:
        return SkodaTrolleyBus()

    def create_trolley(self) -> SkodaTrolley:
        return SkodaTrolley()
