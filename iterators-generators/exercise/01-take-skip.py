class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_step = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_step < self.count:
            current_step = self.current_step
            self.current_step += 1
            return current_step * self.step
        else:
            raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)