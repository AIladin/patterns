from commands import OffCommand, OnCommand


class Controller:
    def __init__(self, on_command: OnCommand, off_command: OffCommand):
        self.on_command = on_command
        self.off_command = off_command

    def on(self):
        self.on_command.execute()

    def off(self):
        self.off_command.execute()
