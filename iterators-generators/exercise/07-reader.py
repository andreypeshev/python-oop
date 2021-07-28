def read_next(*args):
    for current_iter in args:
        for item in current_iter:
            yield item


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
