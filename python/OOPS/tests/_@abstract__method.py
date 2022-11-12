from abc import ABC, abstractmethod, ABCMeta


class ShapeConfig(metaclass=ABCMeta):
    @abstractmethod
    def _config_shape_returns__(self):
        return 0


class Rectangle(ShapeConfig, ABC):
    type = "Rectangle"

    def __init__(self, _shape_name, _shape_length, _shape_breadth):
        self.shape_name = _shape_name
        self.length = _shape_length
        self.breadth = _shape_breadth

    def _config_shape_returns__(self):
        print(f"Shape name : {self.shape_name} \n"
              f"Shape Length : {self.length} \n"
              f"Shape Breadth : {self.breadth} \n"
              )
        return self.shape_name, ":", self.length * self.breadth


Rect = Rectangle(_shape_name="Rectangle", _shape_breadth=20, _shape_length=90)
print(Rect._config_shape_returns__())
