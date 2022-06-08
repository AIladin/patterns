from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, amount: float):
        pass


class PayPalPayment(Strategy):
    def execute(self, amount: float):
        print(f"Paid {amount}$ using PayPal.")


class BankAccountPayment(Strategy):
    def execute(self, amount):
        print(f"Paid {amount}$ from bank account.")
