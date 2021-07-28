class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.number:
            current_idx = self.count
            self.count += 1
            return self.sequence[current_idx % len(self.sequence)]
        else:
            raise StopIteration()


result = sequence_repeat('a', 5)
for item in result:
    print(item, end ='')
