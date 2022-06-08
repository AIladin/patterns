import commands

import device
from controller import Controller, Multicontroller


def main():
    tv = device.Television()
    remote = Controller(
        commands.OnCommand(tv),
        commands.OffCommand(tv),
        commands.VolumeUpCommand(tv),
        commands.VolumeDownCommand(tv),
        commands.NextChanelCommand(tv),
        commands.PrevChanelCommand(tv),
    )

    radio = device.Radio()

    multi_remote = Multicontroller(
        [tv, radio],
        commands.OnCommand,
        commands.OffCommand,
        commands.VolumeUpCommand,
        commands.VolumeDownCommand,
        commands.NextChanelCommand,
        commands.PrevChanelCommand,
    )

    multi_remote.device_on()
    multi_remote.device_volume_down()
    multi_remote.device_next_chanel()
    remote.device_volume_down()
    remote.device_off()


if __name__ == "__main__":
    main()
