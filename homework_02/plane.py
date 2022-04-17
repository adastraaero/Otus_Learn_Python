"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0, cargo=5, max_cargo=200):
        self.weight = float(weight)
        self.started = bool(started)
        self.fuel = float(fuel)
        self.fuel_consumption = float(fuel_consumption)
        self.cargo = float(cargo)
        self.max_cargo = float(max_cargo)

    @staticmethod
    def load_cargo(extcargo):
        if Plane.cargo + extcargo <= Plane.max_cargo:
            Plane.cargo = Plane.cargo + extcargo
        else:
            raise CargoOverload()

samolet_1 = Plane(weight=2500, started=False, fuel=0, fuel_consumption=0, cargo=10, max_cargo=7)
print(vars(samolet_1))
print(samolet_1)

samolet_1.load_cargo(10)

print(samolet_1.cargo)