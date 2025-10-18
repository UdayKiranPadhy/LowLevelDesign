"""

Abstract Factory Pattern

Abstract Factory Pattern is a creational design pattern that lets you produce families of related objects without
specifying their concrete classes.

We can use this pattern when we have multiple super classes with multiple subclasses and based on input, we need to
return one of the sub-class.

"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class BMW(Vehicle):
    def drive(self):
        print("Driving BMW")


class Audi(Vehicle):
    def drive(self):
        print("Driving Audi")


class Mercedes(Vehicle):
    def drive(self):
        print("Driving Mercedes")


class Hundai(Vehicle):
    def drive(self):
        print("Driving Hundai")


class Swift(Vehicle):
    def drive(self):
        print("Driving Swift")


class Alto(Vehicle):
    def drive(self):
        print("Driving Alto")


class VehicleFactory(ABC):
    @abstractmethod
    def get_vehicle(self, vehicle_type: str) -> Vehicle | None:
        pass


class LuxuryVehicleFactory(VehicleFactory):
    def get_vehicle(self, vehicle_type: str) -> Vehicle | None:
        if vehicle_type is None:
            return None
        if vehicle_type == "BMW":
            return BMW()
        elif vehicle_type == "AUDI":
            return Audi()
        elif vehicle_type == "MERCEDES":
            return Mercedes()
        return None


class NonLuxuryVehicleFactory(VehicleFactory):
    def get_vehicle(self, vehicle_type: str) -> Vehicle | None:
        if vehicle_type is None:
            return None
        if vehicle_type == "HUNDAY":
            return Hundai()
        elif vehicle_type == "SWIFT":
            return Swift()
        elif vehicle_type == "ALTO":
            return Alto()
        return None
