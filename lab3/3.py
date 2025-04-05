from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self) :
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width):
