from abc import ABC, abstractmethod


class BaseListener(ABC):
    @property
    @abstractmethod
    def update(self, line: str):
        pass
