import creatures


def main():
    print("Troll actions:")
    troll = creatures.Troll()
    troll.defend_against_attack()
    print()
    print("Pirate actions:")
    pirate = creatures.Pirate()
    pirate.defend_against_attack()


if __name__ == "__main__":
    main()
