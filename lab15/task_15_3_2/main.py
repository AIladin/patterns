import commands
import lights
from controller import Controller


def main():
    kitchen = lights.Lamp("Kitchen lights")
    hall = lights.Lamp("Hall lights")
    bedroom = lights.Lamp("Bedroom lights")
    bathroom = lights.Lamp("Bathroom lights")
    home_lights = lights.HomeLights([kitchen, hall, bathroom, bedroom])

    kitchen_controller = Controller(
        commands.OnCommand(kitchen), commands.OffCommand(kitchen)
    )
    hall_controller = Controller(commands.OnCommand(hall), commands.OffCommand(hall))
    bedroom_controller = Controller(
        commands.OnCommand(bedroom), commands.OffCommand(bedroom)
    )
    bathroom_controller = Controller(
        commands.OnCommand(bathroom), commands.OffCommand(bathroom)
    )
    universal_controller = Controller(
        commands.OnCommand(home_lights), commands.OffCommand(home_lights)
    )

    bathroom_controller.on()
    kitchen_controller.on()
    hall_controller.on()
    bedroom_controller.on()
    universal_controller.off()


if __name__ == "__main__":
    main()
