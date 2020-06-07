class Logger:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        def wrapper(*args, **kwargs):
            try:
                result = self.function(*args, **kwargs)
                return result
            except Exception as ex:
                # with open(file, 'a') as log_file:
                #     log_file.write(f'{ex} thrown from {func.__name__}\n')
                print(f'{ex} thrown from {self.function.__name__}')
                raise ex
        return wrapper
