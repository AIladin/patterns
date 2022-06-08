from mediator import Chat
from mediator import ChatGroup, ConcreteUser


def main():
    user_1 = ConcreteUser("user 1")
    user_2 = ConcreteUser("user 2")
    user_3 = ConcreteUser("user 3")
    user_4 = ConcreteUser("user 4")
    user_5 = ConcreteUser("user 5")
    user_6 = ConcreteUser("user 6")

    chat = Chat()

    group = ChatGroup("Admins")
    chat.add_user(group)

    group.add_user(user_1)
    group.add_user(user_2)

    chat.add_user(user_3)
    chat.add_user(user_4)
    chat.add_user(user_5)
    chat.add_user(user_6)

    user_1.send_message_all("hello, world!")
    user_2.send_message("Hi there!", user_1)
    user_6.send_message("Hello admins!", group)


if __name__ == "__main__":
    main()
