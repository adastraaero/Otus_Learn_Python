from abc import ABC, abstractmethod
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0):
        self.weight = float(weight)
        self.started = bool(started)
        self.fuel = float(fuel)
        self.fuel_consumption = float(fuel_consumption)

    def start(self):
        if self.started is False and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError(self.fuel)

    def move(self, distance):
        if (self.fuel / self.fuel_consumption) * 100 > distance:
            self.fuel = self.fuel - (distance / 100) * self.fuel_consumption
        else:
            raise NotEnoughFuel(self.fuel)



mash = Vehicle(fuel=50, started=False)
jiguli = Vehicle(fuel=50, fuel_consumption=5)

print(mash.weight)
print(mash.fuel)
print(vars(mash))
print(vars(jiguli))

mash.start()
print(mash.started)
jiguli.move(50)
print(jiguli.fuel)
print(vars(jiguli))

