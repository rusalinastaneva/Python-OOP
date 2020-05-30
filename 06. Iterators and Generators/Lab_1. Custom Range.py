class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start

    def __iter__(self):
        self.index = self.start
        return self

    def __next__(self):
        if self.index > self.end:
            raise StopIteration
        index = self.index
        self.index += 1
        return index

cr = custom_range(1, 10)
[print(x) for x in cr]
