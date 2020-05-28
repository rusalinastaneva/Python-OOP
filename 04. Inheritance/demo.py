class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_sizes(self):
        print(self.width, self.height)


class Rectangle(Shape):
    @property
    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(side, side)

    # Overwriting
    def print_sizes(self):
        print(self.width)

r = Rectangle(2, 6)
r.print_sizes()
print(r.area)
s = Square(2)
print(s.area)
s.print_sizes()