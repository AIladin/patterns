from typing import List

from listener.base import BaseListener


class Publisher:
    def __init__(self, file_path: str):
        self.listeners: List[BaseListener] = []
        self.file_path = file_path
        self.file_obj = None

    def __enter__(self):
        # no need to wrap with FileReader class
        self.file_obj = open(self.file_path, "r")

    def __exit__(self, *args, **kwargs):
        self.file_obj.close()
        self.file_obj = None

    def subscribe(self, listener: BaseListener):
        self.listeners.append(listener)

    def notify(self, line: str):
        for listener in self.listeners:
            listener.update(line)

    def update(self):
        assert self.file_obj is not None
        if line := self.file_obj.readline().strip():
            self.notify(line)
            return True
        return False
