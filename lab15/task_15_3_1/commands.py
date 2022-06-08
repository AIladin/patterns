from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, app):
        self.app = app

    @abstractmethod
    def execute(self):
        pass


class OnCommand(Command):
    def execute(self):
        self.app.light_on()


class OffCommand(Command):
    def execute(self):
        self.app.light_off()
