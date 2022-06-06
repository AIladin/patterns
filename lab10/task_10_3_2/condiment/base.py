from bevrage.base import Bevrage


class CondimentDecorator(Bevrage):
    def __init__(self, bevrage: Bevrage):
        self.bevrage: Bevrage = bevrage
