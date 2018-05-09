from itertools import islice, count


def find_primes():
    thousand_primes = islice(( x for x in count() if is_prime(x)), 1000)
    print(list(thousand_primes))

    s = sum(islice(( x for x in count() if is_prime(x)), 1000))
    print(s)


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True


if __name__ == '__main__':
    # run_take()
    # run_distinct()
    find_primes()