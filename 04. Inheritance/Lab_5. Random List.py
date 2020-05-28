import random

class RandomList(list):
    def get_random_element(self):
        num = random.choice(self)
        self.remove(num)
        return num

r = RandomList()
r.append(6)
r.append(16)
r.append(10)
print(r.get_random_element())
print(r.get_random_element())
print(r.get_random_element())
print(r)