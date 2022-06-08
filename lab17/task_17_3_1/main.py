from mediator import Plane, PlanesInFlight, PlanesOnGround, Runway, Watchtower


def main():
    plane_1 = Plane(1)
    plane_2 = Plane(2)
    plane_3 = Plane(3)

    planes_on_ground = PlanesOnGround()
    runway = Runway()
    planes_in_flight = PlanesInFlight()

    watchtower = Watchtower(planes_in_flight, planes_on_ground, runway)

    planes_on_ground.register_plane(plane_1)
    planes_on_ground.register_plane(plane_2)
    planes_on_ground.register_plane(plane_3)

    plane_1.take_off()
    print()
    plane_2.take_off()
    print()
    plane_1.land()
    print()
    plane_3.take_off()
    print()
    plane_2.land()
    print()
    plane_3.land()


if __name__ == "__main__":
    main()
