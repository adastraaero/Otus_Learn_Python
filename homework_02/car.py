"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle

class Car(Vehicle):
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0, engine='opo'):
        self.weight = float(weight)
        self.started = bool(started)
        self.fuel = float(fuel)
        self.fuel_consumption = float(fuel_consumption)
        self.engine = engine

zil = Car()
print(zil)



