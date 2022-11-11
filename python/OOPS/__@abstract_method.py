from abc import ABCMeta, abstractmethod, ABC
import math


class ShapeConfig(metaclass=ABCMeta):
    @abstractmethod
    def returns_statement(self):
        return 0


class Rectangle(ShapeConfig, ABC):
    type = "Rectangle"

    def __init__(self, _length, _breadth):
        self.length = _length
        self.breadth = _breadth

    def returns_statement(self):
        return self.length * self.breadth

    def __repr__(self):
        return str(self.returns_statement())


rectangle_variable = Rectangle(90, 30)
print(rectangle_variable)
