from dataclasses import dataclass
from enum import Enum

from . import compounds


class Color(Enum):
    WHITE = "white"
    BLACK = "black"
    RED = "red"
    GRAY = "gray"


class CarType(Enum):
    SEDAN = "sedan"
    HATCHBACK = "hatchback"
    SUV = "SUV"


@dataclass
class Car:
    car_type: CarType
    color: Color
    engine: compounds.Engine
    wheel: compounds.Wheel


class CarBuilder:
    def __init__(self):
        self.car_type = None
        self.color = None
        self.engine = None
        self.wheel = None

        self.engine_cache = {}
        self.wheel_cache = {}
        self.reset()

    def reset(self):
        self.car_type = CarType.SEDAN
        self.color = Color.BLACK
        self.set_engine(10, compounds.Fuel.DIESEL)
        self.set_wheel(10, compounds.WheelMaterial.ALLOY)

    def set_type(self, car_type: CarType):
        self.car_type = car_type

    def set_color(self, color: Color):
        self.color = color

    def set_engine(self, power: int, fuel: compounds.Fuel):
        engine_hash = hash((power, fuel))
        self.engine = self.engine_cache.get(engine_hash)
        if self.engine is None:
            self.engine = compounds.Engine(power, fuel)
            print(f"Creating new engine. {self.engine}")
            self.engine_cache[engine_hash] = self.engine

    def set_wheel(self, diameter: int, material: compounds.WheelMaterial):
        wheel_hash = hash((diameter, material))
        self.wheel = self.wheel_cache.get(wheel_hash)
        if self.wheel is None:
            self.wheel = compounds.Wheel(diameter, material)
            print(f"Creating new wheel. {self.wheel}")
            self.wheel_cache[wheel_hash] = self.wheel

    def build(self) -> Car:
        if (
            self.car_type is None
            or self.color is None
            or self.engine is None
            or self.wheel is None
        ):
            raise ValueError()
        return Car(self.car_type, self.color, self.engine, self.wheel)
