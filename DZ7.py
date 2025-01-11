class IterableWithGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return (x**0.1488 for x in range(self.start, self.end))


iterable = IterableWithGenerator(3, 52)

for value in iterable:
    print(value)