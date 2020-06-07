from time import time, sleep


def recurring(on_result = None, interval_in_seconds=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                result = func(*args, **kwargs)
                if on_result:
                    on_result(result)
                sleep(interval_in_seconds)
        return wrapper
    return decorator

@recurring(interval_in_seconds=1, on_result=print)
def print_now():
    return time()

print_now()