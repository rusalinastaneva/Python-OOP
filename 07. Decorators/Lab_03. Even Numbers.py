def even_numbers(function):
    def wrapper(numbers):
        result = list(filter(lambda x: x % 2 == 0, numbers))
        return function(result)

    return wrapper



@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5, 10, 11]))
