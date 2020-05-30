class custom_range_iterator:
    def __init__(self, start, end):
        self.end = end
        self.index = start

    def __next__(self):
        if self.index > self.end:
            raise StopIteration
        index = self.index
        self.index += 1
        return index


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return custom_range_iterator(self.start, self.end)

cr = custom_range(1, 4)

it1 = iter(cr)
print(next(it1)) # 1
print(f'Index: {it1.index}')
it2 = iter(cr)
print(f'Index: {it1.index}')
print(next(it1)) # 2
print(next(it2)) # 1