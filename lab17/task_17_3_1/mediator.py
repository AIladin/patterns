from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional


class BaseComponent(ABC):
    def __init__(self, mediator: Optional["Mediator"] = None):
        self.mediator = mediator


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: BaseComponent, event: Enum):
        pass


class Event(Enum):
    TAKING_OFF: str = "taking off"
    IN_AIR: str = "in the air"
    LANDING: str = "landing"
    ON_GROUND: str = "on the ground"


class Plane(BaseComponent):
    def __init__(self, id: int):
        self.is_in_the_air = False
        self.id = id

    def take_off(self):
        if not self.is_in_the_air:
            print(f"Plane {self.id} is taking off.")
            self.is_in_the_air = True
            self.mediator.notify(self, Event.TAKING_OFF)

    def land(self):
        if self.is_in_the_air:
            print(f"Plane {self.id} is landing.")
            self.is_in_the_air = False
            self.mediator.notify(self, Event.LANDING)


class Runway(BaseComponent):
    def __init__(self):
        self.is_awailable = True

    def reserve(self):
        self.is_awailable = False
        print("Runway is unavaliable.")

    def free(self):
        self.is_awailable = True
        print("Runway is avaliable.")


class PlanesOnGround(BaseComponent):
    def __init__(self):
        self.planes = set()

    def register_plane(self, plane: Plane):
        self.planes.add(plane)
        plane.mediator = self.mediator

    def add_plane(self, plane: Plane):
        self.planes.add(plane)
        print(f"Plane {plane.id} added to planes on ground.")
        self.mediator.notify(plane, Event.ON_GROUND)

    def remove_plane(self, plane: Plane):
        self.planes.discard(plane)
        print(f"Plane {plane.id} removed from planes on ground.")


class PlanesInFlight(BaseComponent):
    def __init__(self):
        self.planes = set()

    def add_plane(self, plane: Plane):
        self.planes.add(plane)
        print(f"Plane {plane.id} added to planes in flight.")
        self.mediator.notify(plane, Event.IN_AIR)

    def remove_plane(self, plane: Plane):
        self.planes.discard(plane)
        print(f"Plane {plane.id} removed from planes in flight.")


class Watchtower(Mediator):
    def __init__(
        self,
        planes_in_flight: PlanesInFlight,
        planes_on_ground: PlanesOnGround,
        runway: Runway,
    ):
        self.planes_in_flight = planes_in_flight
        self.planes_in_flight.mediator = self
        self.planes_on_ground = planes_on_ground
        self.planes_on_ground.mediator = self
        self.runway = runway
        self.runway.mediator = self

    def notify(self, plane: Plane, event: Event):
        if event == Event.TAKING_OFF:
            self.runway.reserve()
            self.planes_in_flight.add_plane(plane)
            self.planes_on_ground.remove_plane(plane)

        if event == Event.LANDING:
            self.runway.reserve()
            self.planes_on_ground.add_plane(plane)
            self.planes_in_flight.remove_plane(plane)

        if event in (Event.IN_AIR, Event.ON_GROUND):
            self.runway.free()
