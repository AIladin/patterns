from typing import List

import commands
from device import Device


class Controller:
    def __init__(
        self,
        on_comm: commands.OnCommand,
        off_comm: commands.OffCommand,
        vol_up_comm: commands.VolumeUpCommand,
        vol_down_comm: commands.VolumeDownCommand,
        next_ch_comm: commands.NextChanelCommand,
        prev_ch_comm: commands.PrevChanelCommand,
    ):
        self.on_comm = on_comm
        self.off_comm = off_comm
        self.vol_up_comm = vol_up_comm
        self.vol_down_comm = vol_down_comm
        self.next_ch_comm = next_ch_comm
        self.prev_ch_comm = prev_ch_comm

    def device_on(self):
        self.on_comm.execute()

    def device_off(self):
        self.off_comm.execute()

    def device_volume_up(self):
        self.vol_up_comm.execute()

    def device_volume_down(self):
        self.vol_down_comm.execute()

    def device_next_chanel(self):
        self.next_ch_comm.execute()

    def device_prev_chanel(self):
        self.prev_ch_comm.execute()


class Multicontroller:
    def __init__(
        self,
        devices: List[Device],
        on_comm: commands.OnCommand,
        off_comm: commands.OffCommand,
        vol_up_comm: commands.VolumeUpCommand,
        vol_down_comm: commands.VolumeDownCommand,
        next_ch_comm: commands.NextChanelCommand,
        prev_ch_comm: commands.PrevChanelCommand,
    ):
        self.devices = devices
        self.on_comm = on_comm
        self.off_comm = off_comm
        self.vol_up_comm = vol_up_comm
        self.vol_down_comm = vol_down_comm
        self.next_ch_comm = next_ch_comm
        self.prev_ch_comm = prev_ch_comm

    def device_on(self):
        for d in self.devices:
            self.on_comm(d).execute()

    def device_off(self):
        for d in self.devices:
            self.off_comm(d).execute()

    def device_volume_up(self):
        for d in self.devices:
            self.vol_up_comm(d).execute()

    def device_volume_down(self):
        for d in self.devices:
            self.vol_down_comm(d).execute()

    def device_next_chanel(self):
        for d in self.devices:
            self.next_ch_comm(d).execute()

    def device_prev_chanel(self):
        for d in self.devices:
            self.prev_ch_comm(d).execute()
