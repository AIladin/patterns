from abc import ABC, abstractmethod
from typing import TypeVar, Any

T = TypeVar("T", bound="BaseBuilder")


class BaseBuilder(ABC):
    @abstractmethod
    def append_substring(self, substring: str) -> T:
        pass

    @abstractmethod
    def insert_substring(self, substring: str, position: int) -> T:
        pass

    @abstractmethod
    def reset(self) -> T:
        pass

    @abstractmethod
    def get_result(self) -> Any:
        pass
