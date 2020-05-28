from zoo.animal import Animal


class Reptile(Animal):
    def __init__(self):
        super(Reptile, self).__init__(self.name)