"""

Factory Pattern

Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.

We can use this pattern when we have a super class with multiple subclasses and based on input, we need to return one of the sub-class.

"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")


class ShapeFactory:
    def get_shape(self, shape_type: str) -> Shape | None:
        if shape_type is None:
            return None
        if shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "RECTANGLE":
            return Rectangle()
        elif shape_type == "SQUARE":
            return Square()
        return None
