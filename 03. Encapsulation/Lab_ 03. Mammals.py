class Mammal:
    __kingdom = "animals"
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"

dog = Mammal("Dog", "Domestic", "Bark")
cat = Mammal("Cat", "Siam", "Meau")
print(dog.make_sound())
print(cat.make_sound())
print(dog.get_kingdom())
print(cat.get_kingdom())
print(dog.info())
print(cat.info())

