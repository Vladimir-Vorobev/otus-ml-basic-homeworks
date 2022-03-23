from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError(self.fuel)

    def move(self):
        new_fuel = self.fuel - self.weight * self.fuel_consumption
        if new_fuel >= 0:
            self.fuel = new_fuel
        else:
            raise NotEnoughFuel(self.fuel, new_fuel * -1)
