import os.path as osp
from abc import ABC, abstractmethod

from handler.base import BaseHandler


class FileHandler(BaseHandler, ABC):
    @classmethod
    @property
    @abstractmethod
    def SUPPORTED_EXTENSION(cls) -> str:
        """Definition of abstract class variable."""
        pass

    def open(self, file_name: str) -> None:
        extension = osp.splitext(file_name)[-1]
        if extension == f".{self.SUPPORTED_EXTENSION}":
            print(f"{self.__class__.__name__} is opening {file_name}.")
        else:
            print(
                f"{self.__class__.__name__} not supported extension {extension} passing to next handler."
            )
            super().open(file_name)
