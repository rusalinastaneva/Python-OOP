class Animal:
    def eat(self):
        return "eating..."

class Dog(Animal):
    def bark(self):
        return "barking..."

class Cat(Animal):
    def meow(self):
        return "meowing..."

cat = Cat()
dog = Dog()
print(dog.eat())
print(dog.bark())
print(cat.eat())
print(cat.meow())