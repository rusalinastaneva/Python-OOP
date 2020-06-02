def fibonacci():
    current_num = 1
    previous_num = 0
    yield previous_num
    yield current_num

    while True:
        next_num = previous_num + current_num
        yield next_num
        previous_num = current_num
        current_num = next_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
