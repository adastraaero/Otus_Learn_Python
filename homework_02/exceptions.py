"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, fuel: float):
        print(f'bak pust, current fuel is: {fuel}')


class NotEnoughFuel(Exception):
    def __init__(self):
        print(f'malo topliva, current fuel is: {fuel}')


class CargoOverload(Exception):
    def __init__(self):
        print(f'samolet peregrujen: {self.max_cargo}')
