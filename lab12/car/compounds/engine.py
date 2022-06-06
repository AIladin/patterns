from dataclasses import dataclass
from enum import Enum


class Fuel(Enum):
    PETROL = "petrol"
    DIESEL = "diesel"
    ELECTRIC = "electric"


@dataclass(frozen=True)
class Engine:
    power: int
    fuel: Fuel
