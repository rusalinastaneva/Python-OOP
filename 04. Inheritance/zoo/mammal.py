from zoo.animal import Animal


class Mammal(Animal):
    def __init__(self):
        super(Mammal, self).__init__(self.name)
