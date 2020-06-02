from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):
    def __str__(self):
        return f'Area: {self.area()}; Perimeter: {self.perimeter()}'

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * pi

    def perimeter(self):
        return self.radius * 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
       return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        p = self.perimeter()
        return sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

def print_shape(s: Shape):
    print(s)

shapes = [
    Circle(4),
    Circle(5),
    Rectangle(4, 6),
    Rectangle(5, 2),
    Triangle(2, 2, 3)
]
[print_shape(s) for s in shapes]
