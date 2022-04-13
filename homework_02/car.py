"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle

class Car(Vehicle):
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0, engine):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine  = engine





