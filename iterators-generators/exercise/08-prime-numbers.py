def is_prime(num):
    return num > 1 and all(num % i for i in range(2, num))


def get_primes(seq):
    primes = filter(lambda x: is_prime(x), seq)
    for num in primes:
        yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))