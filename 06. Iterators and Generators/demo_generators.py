def custom_range(min, max):
    for i in range(min, max + 1):
        yield i


# [print(x) for x in custom_range(1, 5)]

it = custom_range(1, 5)
print(next(it))
print(next(it))
print(next(it))