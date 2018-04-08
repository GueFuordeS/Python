#!/usr/bin/python


from sys import argv
from time import time
from numba import jit


@jit(cache=True)
def prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, num//2, 2):
        if num % i == 0:
            return False

    return True


@jit(cache=True)
def yieldprime(target):
    count = 1
    primes = 2
    while True:
        if count == target:
            return primes
        primes += 1
        if prime(primes):
            count += 1


def main():
    start = time()

    try:
        target = int(argv[1])
        if target <= 0:
            raise ValueError
    except(IndexError, ValueError):
        print('Needed a positive integer as command line argument')
        return

    prime = yieldprime(target)

    print('Taken %.12f seconds to fetch' %(time() - start))
    print(prime)


if __name__=='__main__':
    main()
