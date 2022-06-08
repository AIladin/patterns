import military
import visitor


def main():
    generalStaff = military.GeneralStaff(10, 20)
    print(generalStaff)

    militaryBase = military.MilitaryBase(10, 2000, 150, 30)
    print(militaryBase)

    agent = visitor.SecretAgent()
    saboteur = visitor.Saboteur()

    generalStaff.accept(agent)
    generalStaff.accept(saboteur)

    militaryBase.accept(agent)
    militaryBase.accept(saboteur)


if __name__ == "__main__":
    main()
