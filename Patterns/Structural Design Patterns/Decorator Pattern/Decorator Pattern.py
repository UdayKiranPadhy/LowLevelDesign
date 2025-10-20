"""

Decorator Pattern

The Decorator pattern is used to dynamically add a new feature to an object without changing its implementation. It
differs from inheritance because the new feature is added only to that particular object, not to the entire subclass.

The Decorator pattern is also known as Wrapper.

"""

from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class PlainPizza(Pizza):
    def get_cost(self):
        return 100

    def get_description(self):
        return 'Plain Pizza'

class MediumPizza(Pizza):
    def get_cost(self):
        return 200

    def get_description(self):
        return 'Medium Pizza'


class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost()

    def get_description(self):
        return self.pizza.get_description()


class Mozzarella(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_cost(self):
        return super().get_cost() + 10

    def get_description(self):
        return super().get_description() + ', Mozzarella'


class TomatoSauce(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_cost(self):
        return super().get_cost() + 20

    def get_description(self):
        return super().get_description() + ', Tomato Sauce'


class Paneer(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_cost(self):
        return super().get_cost() + 30

    def get_description(self):
        return super().get_description() + ', Paneer'


if __name__ == '__main__':
    base_pizza = PlainPizza()
    print(base_pizza.get_cost())
    print(base_pizza.get_description())

    pizza = Mozzarella(base_pizza)
    print(pizza.get_cost())
    print(pizza.get_description())

    pizza = TomatoSauce(base_pizza)
    print(pizza.get_cost())
    print(pizza.get_description())

    pizza = Paneer(pizza)
    print(pizza.get_cost())
    print(pizza.get_description())



"""
Example 2

"""

from abc import ABC, abstractmethod

# The Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


# The Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 50

    def description(self):
        return "Simple Coffee"


# The Decorator Base Class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 20

    def description(self):
        return self._coffee.description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 10

    def description(self):
        return self._coffee.description() + ", Sugar"


class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 30

    def description(self):
        return self._coffee.description() + ", Whipped Cream"
