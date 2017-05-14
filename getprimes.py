#!/usr/bin/python3

from sys import argv
from time import time

def prime(num):
    if num < 2:
        return False

    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, num, 2):
        if num % i == 0:
            return False

    return True

def yieldprimes(total):
    result = []
    count = 2
    
    while len(result) < total:
        if prime(count):
            result.append(count)
        count += 1
    
    return result

def main():
    start = time()
    
    try:
        total = int(argv[1])
        if int(argv[1]) < 0:
            raise ValueError
    except(IndexError, ValueError):
        print('Needed a integer as command line argument')
        return

    primes = yieldprimes(total)

    print('fetched %d primes in %.12f seconds' %(total, time() - start))
    print(primes)

if __name__=='__main__':
    main()
