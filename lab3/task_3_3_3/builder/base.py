from abc import ABC, abstractmethod
from typing import Any


class BaseBuilder(ABC):
    @abstractmethod
    def append_substring(self, substring: str) -> "BaseBuilder":
        pass

    @abstractmethod
    def insert_substring(self, substring: str, position: int) -> "BaseBuilder":
        pass

    @abstractmethod
    def reset(self) -> "BaseBuilder":
        pass

    @abstractmethod
    def get_result(self) -> Any:
        pass
