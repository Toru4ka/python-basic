from homework_02.exceptions import LowFuelError,NotEnoughFuel
from abc import ABC


class Vehicle(ABC):
    started = False

    def __init__(self, weight=1000, fuel=0, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started:
            pass
        elif self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError()

    def move(self, distance):
        fuel = self.fuel - (distance * self.fuel_consumption)
        if fuel < 0:
            raise NotEnoughFuel()
        else:
            self.fuel = fuel
            return self.fuel
