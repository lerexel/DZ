class IterableWithGenerator:
    def __init__(self, start, end):
        self.starting = start
        self.ending = end

    def __iter__(self):
        return (x**0.5 for x in range(self.starting, self.ending))


iterable = IterableWithGenerator(1, 52)

for value in iterable:
    print(value)



