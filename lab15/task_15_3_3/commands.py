from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def execute(self):
        pass


class OnCommand(Command):
    def execute(self):
        self.device.on()


class OffCommand(Command):
    def execute(self):
        self.device.off()


class VolumeUpCommand(Command):
    def execute(self):
        self.device.volume_up()


class VolumeDownCommand(Command):
    def execute(self):
        self.device.volume_down()


class NextChanelCommand(Command):
    def execute(self):
        self.device.next_chanel()


class PrevChanelCommand(Command):
    def execute(self):
        self.device.prev_chanel()
