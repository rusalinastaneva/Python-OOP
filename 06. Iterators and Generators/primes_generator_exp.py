from math import sqrt


def is_prime(value):
    for x in range(2, int(sqrt(value) + 1)):
        if value % x == 0:
            return False
    return True


def primes_generator(max_prime):
    return (x for x in range(1, max_prime + 1) if is_prime(x))

primes = primes_generator(12)
it = iter(primes)
# OR
# it = primes_generator(12)

print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
print(next(it)) # 5
print(next(it)) # 7
print(next(it)) # 11

[print(x) for x in primes_generator(12)]