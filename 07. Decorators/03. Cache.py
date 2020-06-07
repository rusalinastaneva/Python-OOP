def cache(func):
    def wrapper(number):
        result = func(number)
        wrapper.log[number] = result
        return result
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(3)
print(fibonacci.log)
