import compunds


class CarFasade:
    def __init__(self):
        self.ignition = compunds.Ignition()
        self.clutch = compunds.Clutch()
        self.accelerator = compunds.Accelerator()
        self.gear_stick = compunds.GearStick()
        self.hand_brake = compunds.Handbrake()

    def drive(self):
        self.ignition.turn_on()
        self.hand_brake.press()
        self.clutch.press()
        self.gear_stick.change_gear(1)
        self.clutch.lift()
        self.hand_brake.lift()
        self.accelerator.press()
