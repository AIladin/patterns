from abc import ABC, abstractmethod

import military


class Visitor(ABC):
    @abstractmethod
    def visit_base(self, base: military.MilitaryBase):
        pass

    @abstractmethod
    def visit_staff(self, staff: military.GeneralStaff):
        pass


class SecretAgent(Visitor):
    def visit_staff(self, staff: military.GeneralStaff):
        print(f"Stealing {staff.secretPaper} secret papers.")

    def visit_base(self, base: military.MilitaryBase):
        print(f"Collected information '{base}'")


class Saboteur(Visitor):
    def visit_base(self, base: military.MilitaryBase):
        print(f"{base.soldiers} soldiers are wounded.")
        base.soldiers = 0

    def visit_staff(self, staff: military.GeneralStaff):
        print(f"Destroyning {staff.secretPaper} secret papers.")
        staff.secretPaper = 0
