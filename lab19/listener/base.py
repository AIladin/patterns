from abc import ABC, abstractproperty


class BaseListener(ABC):
    @abstractproperty
    def update(self, line: str):
        pass
