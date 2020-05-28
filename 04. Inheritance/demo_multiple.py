class Base1:
    def __init__(self):
        self.x1 = '1'

    def f1(self):
        return self.x1


class Base2:
    def __init__(self):
        self.x2 = '2'

    def f2(self):
        return self.x2


class Child(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)



c = Child()
print(c.f1())
print(c.f2())
