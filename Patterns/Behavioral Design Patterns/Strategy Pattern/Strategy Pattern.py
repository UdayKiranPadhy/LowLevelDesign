"""

In Strategy pattern, a class behavior or its algorithm can be changed at run time.
This type of design pattern comes under behavior pattern.

In Strategy pattern, we create objects which represent various strategies and a
context object whose behavior varies as per its strategy object.
The strategy object changes the executing algorithm of the context object.

Instead of hardcoding which algorithm to use, you pick the right “strategy” dynamically.


Context
   └── uses → Strategy (interface)
                 ├── ConcreteStrategyA
                 ├── ConcreteStrategyB
                 └── ConcreteStrategyC


"""
from abc import ABC, abstractmethod


##########################
# Without Strategy Pattern
##########################

class Vehicle(ABC):
    @abstractmethod
    def drive_strategy(self):
        pass


class Car(Vehicle):
    def drive_strategy(self):
        print("Normal Driving Strategy")


class Bus(Vehicle):
    def drive_strategy(self):
        print("Normal Driving Strategy")


class SportsCar(Vehicle):
    def drive_strategy(self):
        print("Sports Driving Strategy")


class Bike(Vehicle):
    def drive_strategy(self):
        print("Slow Driving Strategy")


# As we can see the drive method is different for each vehicle type
# and we can't change it at runtime without changing the code of the class
# and this is not a good practice
# So we will use the Strategy Pattern to solve this problem


##########################
# With Strategy Pattern
##########################

class Vehicle(ABC):
    def __init__(self, strategy):
        self.strategy = strategy

    def drive_strategy(self):
        self.strategy.drive()


class DrivingStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass


class NormalDrivingStrategy(DrivingStrategy):
    def drive(self):
        print("Normal Driving Strategy")


class SportsDrivingStrategy(DrivingStrategy):
    def drive(self):
        print("Sports Driving Strategy")


class SlowDrivingStrategy(DrivingStrategy):
    def drive(self):
        print("Slow Driving Strategy")


# Now we can change the strategy at runtime
# without changing the code of the class
car = Vehicle(NormalDrivingStrategy())
car.drive_strategy()
car.strategy = SportsDrivingStrategy()
car.drive_strategy()
car.strategy = SlowDrivingStrategy()
car.drive_strategy()
