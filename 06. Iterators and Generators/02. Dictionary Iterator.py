class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.pairs = list(dictionary.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.pairs):
            raise StopIteration

        idx = self.idx
        current_pair = self.pairs[idx]
        self.idx += 1
        return current_pair

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

