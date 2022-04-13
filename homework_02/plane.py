"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0, cargo=0, max_cargo=0):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self):
        if self.cargo + self.load_cargo() <= self.max_cargo:
            self.cargo = self.cargo + self.max_cargo
        else:
            raise CargoOverload(self.max_cargo)

samolet_1 = Plane(weight=0, started=False, fuel=0, fuel_consumption=0, cargo=10, max_cargo=7)
print(vars(samolet_1))

samolet_1.load_cargo()

print(samolet_1)