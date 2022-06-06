from component import Component


class BaseDecorator(Component):
    def __init__(self, component: Component):
        self.component = component

    def print(self):
        self.component.print()
