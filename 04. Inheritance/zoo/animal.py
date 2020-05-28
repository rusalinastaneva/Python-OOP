class Animal:
    def __init__(self, name):
        self.name = name

    @property
    def getter(self):
        return self.name

