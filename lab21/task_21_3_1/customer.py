from strategies import Strategy


class Customer:
    def __init__(self):
        self.strategy: Strategy = None

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def make_payment(self, amount: float):
        self.strategy.execute(amount)
