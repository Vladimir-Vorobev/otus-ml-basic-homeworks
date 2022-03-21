"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(BaseException):
    def __init__(self, fuel):
        self.fuel = fuel

    def __str__(self):
        return f'{self.fuel} is not enough amount of fuel to start. The amount of fuel must be a positive number.'


class NotEnoughFuel(BaseException):
    def __init__(self, fuel, fuel_need):
        self.fuel = fuel
        self.fuel_need = fuel_need

    def __str__(self):
        return f'The Vehicle needs {self.fuel_need} of fuel more to pass this distance. Now it has {self.fuel} of fuel.'


class CargoOverload(BaseException):
    def __init__(self, cargo, new_cargo, max_cargo):
        self.cargo = cargo
        self.new_cargo = new_cargo
        self.max_cargo = max_cargo
        self.overload = cargo + new_cargo - max_cargo

    def __str__(self):
        return f'The maximum cargo weight is {self.max_cargo}, now the plane has {self.cargo} of cargo, ' \
               f'you want to put {self.new_cargo} of cargo more, the overload is {self.overload}.'
