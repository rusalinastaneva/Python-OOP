def squares(n):
    for x in range(1, n + 1):
        yield x * x


print(list(squares(5)))
# GENERATOR EXPRESSION
print(list(x * x for x in range(1, 6)))