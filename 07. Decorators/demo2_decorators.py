from time import time


def measure_performance(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__} executed for {end - start} seconds')
        return result
    return wrapper


def exception_logger(file='logs.log'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as ex:
                # with open(file, 'a') as log_file:
                #     log_file.write(f'{ex} thrown from {func.__name__}\n')
                print(f'{ex} thrown from {func.__name__}')
                raise ex
        return wrapper
    return decorator

@exception_logger(file = './decorators.log')
@measure_performance
def my_multiply(x, y):
    return x * y

# Record the exception logs in the default file logs.log
@exception_logger()
def throws():
    raise ValueError

# throws()
print(my_multiply(5, 3))
print(my_multiply('Gosho', 'Pesho'))
