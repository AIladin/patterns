from abc import ABC, abstractmethod
from numbers import Number


class BaseHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def handle(self, *args, **kwargs) -> None:
        if self.next_handler is not None:
            self.next_handler.handle(*args, **kwargs)

    def set_next(self, handler: "BaseHandler") -> "BaseHandler":
        print(f"{handler.__class__.__name__} is queued after {self.__class__.__name__}")
        self.next_handler = handler
        return handler


class BaseOperationHandler(BaseHandler, ABC):
    @classmethod
    @property
    @abstractmethod
    def SUPPORTED_OPERATION(cls) -> str:
        """Definition of abstract class variable."""
        pass

    @abstractmethod
    def _handle(self, a: Number, b: Number) -> Number:
        pass

    def handle(self, a: Number, b: Number, operation: str) -> None:
        if operation == self.SUPPORTED_OPERATION:
            print(
                f"{self.__class__.__name__} is handling operation {operation} for {a} and {b}"
            )
            res = self._handle(a, b)
            print(f"Result: {res}")
        else:
            super().handle(a, b, operation)
