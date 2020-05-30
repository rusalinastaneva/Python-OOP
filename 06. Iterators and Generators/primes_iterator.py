from math import sqrt


def is_prime(value):
    for x in range(2, int(sqrt(value) + 1)):
        if value % x == 0:
            return False
    return True


class PrimesIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.last_prime = 0

    def __next__(self):
        current_prime = self.last_prime + 1
        while current_prime <= self.max_value and \
            not is_prime(current_prime):
            current_prime += 1

        if current_prime > self.max_value:
            raise StopIteration
        self.last_prime = current_prime
        return current_prime


class Primes:
    def __init__(self, max_value):
        self.max_value = max_value

    def __iter__(self):
        return PrimesIterator(self.max_value)


primes = Primes(12)
it = iter(primes)
print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
print(next(it)) # 5
print(next(it)) # 7
print(next(it)) # 11

[print(x) for x in primes]