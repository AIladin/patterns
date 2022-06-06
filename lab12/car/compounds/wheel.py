from dataclasses import dataclass
from enum import Enum


class WheelMaterial(Enum):
    STEEL = "steel"
    ALLOY = "alloy"


@dataclass(frozen=True)
class Wheel:
    diameter: int
    material: WheelMaterial
