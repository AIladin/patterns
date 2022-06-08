from abc import ABC, abstractmethod


class BasePrototype(ABC):
    def clone(self) -> "BasePrototype":
        pass
