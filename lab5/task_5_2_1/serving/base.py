from abc import ABC, abstractmethod


class Serving(ABC):
    @classmethod
    @property
    @abstractmethod
    def SERVING_NAME(self) -> str:
        pass

    def serve(self):
        print(f"This bevrage will be served {self.SERVING_NAME}s.")
