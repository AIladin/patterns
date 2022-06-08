from commands import OffCommand, OnCommand
from controller import Controller
from lamp import Lamp


def main():
    lamp = Lamp()
    controller = Controller(OnCommand(lamp), OffCommand(lamp))

    controller.on()
    controller.on()
    controller.on()
    controller.off()
    controller.off()
    controller.on()


if __name__ == "__main__":
    main()
