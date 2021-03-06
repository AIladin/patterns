from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def prev(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class PlayState(State):
    def play(self):
        pass

    def pause(self):
        print("Paused.")
        self.player.set_state(PauseState(self.player))

    def next(self):
        current = self.player.get_current_track_num()
        self.player.set_track_num(current + 1)
        print(f"Playing next track: {self.player.get_current_track()}")

    def prev(self):
        current = self.player.get_current_track_num()
        self.player.set_track_num(current - 1)
        print(f"Playing prev track: {self.player.get_current_track()}")

    def stop(self):
        print("Stopped.")
        self.player.set_state(StopState(self.player))


class StopState(State):
    def play(self):
        self.player.set_state(PlayState(self.player))
        print(f"Playing from the beginning: {self.player.get_current_track()}")

    def next(self):
        current = self.player.get_current_track_num()
        self.player.set_track_num(current + 1)
        print(f"Next track: {self.player.get_current_track()}")

    def prev(self):
        current = self.player.get_current_track_num()
        self.player.set_track_num(current - 1)
        print(f"Prev track: {self.player.get_current_track()}")

    def stop(self):
        pass

    def pause(self):
        pass


class PauseState(State):
    def play(self):
        print(f"Resumed playing : {self.player.get_current_track()}")
        self.player.set_state(PlayState(self.player))

    def next(self):
        current = self.player.get_current_track_num()
        self.player.set_track_num(current + 1)
        print(f"Next track: {self.player.get_current_track()}")
        self.player.set_state(StopState(self.player))

    def prev(self):
        current = self.player.get_current_track_num()
        self.player.set_track_num(current - 1)
        print(f"Prev track: {self.player.get_current_track()}")
        self.player.set_state(StopState(self.player))

    def stop(self):
        pass

    def pause(self):
        pass
