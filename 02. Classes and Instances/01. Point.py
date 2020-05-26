from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, other_x, other_y):
        dist = sqrt((self.x - other_x) ** 2 + (self.y - other_y) ** 2)
        return dist


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
