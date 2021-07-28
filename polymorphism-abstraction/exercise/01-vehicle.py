from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive():
        pass
    
    @abstractmethod
    def refuel():
        pass


class Car(Vehicle):
    SUMMER_FUEL_INCREASE = 0.9
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        super().__init__()
    
    def drive(self, distance):
        if not (self.fuel_quantity - (self.fuel_consumption + Car.SUMMER_FUEL_INCREASE) * distance) < 0:
            self.fuel_quantity -= (self.fuel_consumption + Car.SUMMER_FUEL_INCREASE) * distance
    def refuel(self, fuel):
        self.fuel_quantity += fuel 

class Truck(Vehicle):
    PERCENT_FUEL_LEFT = 0.95
    SUMMER_FUEL_INCREASE = 1.6
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        super().__init__()
    
    def drive(self, distance):
        if not (self.fuel_quantity - (self.fuel_consumption + Truck.SUMMER_FUEL_INCREASE) * distance) < 0:
            self.fuel_quantity -= (self.fuel_consumption + Truck.SUMMER_FUEL_INCREASE) * distance
            
    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.PERCENT_FUEL_LEFT
