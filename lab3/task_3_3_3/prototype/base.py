from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T", bound="BasePrototype")


class BasePrototype(ABC):
    def clone(self) -> T:
        pass
