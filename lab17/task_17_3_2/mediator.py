from abc import ABC, abstractmethod
from typing import Dict


class User(ABC):
    @abstractmethod
    def send_message_all(self, message: str):
        pass

    @abstractmethod
    def send_message(self, message: str, reciever: "User"):
        pass

    @abstractmethod
    def receive_message(self, message: str, sender: "User"):
        pass


class Mediator(ABC):
    @abstractmethod
    def send_message_all(self, message: str, sender: User):
        pass

    @abstractmethod
    def send_message(self, message, sender: User, reciever: User):
        pass


class ConcreteUser(User):
    def __init__(self, id: str):
        self.id = id
        self.chat = None

    def send_message(self, message: str, reciever: User):
        self.chat.send_message(message, self, reciever)

    def receive_message(self, message: str, sender: User):
        print(f"User '{self.id}' receives message: '{message}' from user '{sender.id}'")

    def send_message_all(self, message):
        self.chat.send_message_all(message, self)


class ChatGroup(ConcreteUser):
    def __init__(self, id):
        super().__init__(id)
        self.group = set()

    def add_user(self, user: ConcreteUser):
        self.group.add(user)
        self.chat.add_user(user)

    def receive_message(self, message: str, sender: User):
        for user in self.group:
            user.receive_message(message, sender)


class Chat(Mediator):
    def __init__(self):
        self.users: Dict[str, ConcreteUser] = {}

    def add_user(self, user: ConcreteUser):
        self.users[user.id] = user
        user.chat = self

    def send_message_all(self, message, sender: ConcreteUser):
        for reciever_id, reciever in self.users.items():
            if reciever_id != sender.id:
                reciever.receive_message(message, sender)

    def send_message(self, message, sender: User, reciever: User):
        self.users[reciever.id].receive_message(message, sender)
