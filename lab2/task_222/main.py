from typing import List
from core.abstract_classes import VehicleFactory, Bus, Trolley, TrolleyBus
from core.manufacturers.hundai import HyundaiFactory
from core.manufacturers.skoda import SkodaFactory
from core.manufacturers.volvo import VolvoFactory


def main():
    total_miles: int = 100_000

    num_buses: int = 20
    num_trolleys: int = 10
    num_trolleybuses: int = 15

    manufacturer_factories: List[VehicleFactory] = [HyundaiFactory(), SkodaFactory(), VolvoFactory()]

    for concrete_factory in manufacturer_factories:
        buses: List[Bus] = [concrete_factory.create_bus() for _ in range(num_buses)]
        trolleys: List[Trolley] = [concrete_factory.create_trolley() for _ in range(num_trolleys)]
        trolleybuses: List[TrolleyBus] = [concrete_factory.create_trolleybus() for _ in range(num_trolleybuses)]

        total_busses_cost = sum(bus.total_bus_cost(total_miles) for bus in buses)
        total_trolleys_cost = sum(trolley.total_trolley_cost(total_miles) for trolley in trolleys)
        total_trolleybuses_cost = sum(trolleybus.total_trolleybus_cost(total_miles) for trolleybus in trolleybuses)

        final_cost = total_busses_cost + total_trolleys_cost + total_trolleybuses_cost
        print(f"Total {concrete_factory.name} cost is {final_cost}")


if __name__ == "__main__":
    main()
