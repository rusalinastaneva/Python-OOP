def number_increment(numbers):
    def increase():
        nonlocal numbers
        numbers = [x + 1 for x in numbers]

    def get():
        return numbers
    return {
        'increase': increase,
        'get': get
    }


operations = number_increment([1, 2, 3])
operations['increase']()
print(operations['get']())
operations['increase']()
operations['increase']()
print(operations['get']())

