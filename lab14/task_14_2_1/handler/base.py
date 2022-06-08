from abc import ABC


class BaseHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def open(self, file_name: str) -> None:
        if self.next_handler is not None:
            self.next_handler.open(file_name)

    def set_next(self, handler: "BaseHandler") -> "BaseHandler":
        print(f"{handler.__class__.__name__} is queued after {self.__class__.__name__}")
        self.next_handler = handler
        return handler
