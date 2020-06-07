# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#
# p = Person('Gosho')
# print(p.name)


def uppercase(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper

@uppercase
def say_hi():
    return 'Hello'

@uppercase
def log():
    return 'error'

print(log())
print(say_hi())

def exception_logger(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            with open('decorators.log', 'a') as file:
                file.write(f'{ex} thrown from {func.__name__}\n')
                raise ex
    return wrapper

@exception_logger
def my_multiply(x, y):
    return x * y

@exception_logger
def throws():
    raise ValueError

throws()
print(my_multiply(5, 3))
print(my_multiply('Gosho', 'Pesho'))
# uppercase_say_hi = uppercase(say_hi)
# uppercase_log = uppercase(log)
# uppercase_say_hi()
