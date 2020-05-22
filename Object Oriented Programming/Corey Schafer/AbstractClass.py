# abc stands for "abstract base class"
from abc import ABC, abstractmethod


class Shape(ABC):
    # inherit from ABC class
    # add @abstractmethod decorator to the methods
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Square(Shape):
    """docstring for Square"""

    def __init__(self, side):
        super(Square, self).__init__()
        self.__side = side

    @property
    def area(self):
        return self.__side**2

    @property
    def perimeter(self):
        return self.__side * 4


square = Square(5)

print(square.area)
print(square.perimeter)

print(id(Square))
