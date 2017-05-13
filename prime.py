from sys import argv
from time import time

def prime(num):
    start = time()
    
    if num < 2:
        compute(num, time()-start)
        return False

    if num == 2:
        compute(num, time()-start, isprime=True)
        return True
    
    if num % 2 == 0:
        compute(num, time()-start)
        return False
    
    for i in range(3, num, 2):
        if num % i == 0:
            compute(num, time()-start)
            return False

    compute(num, time()-start, isprime=True)
    return True

def compute(inpt, result, isprime=False):

    result = format(result, '.12f')

    SPACE = ' | '
    HEADER = 'Input:'.ljust(12) + SPACE + 'Spent time(in secs):'.ljust(30) + SPACE + 'Prime number:'.ljust(13) + '\n'

    try:
        file = open('resultsforprimes.txt', 'r+')
        if file.readline() != HEADER:
            file.write(HEADER)
            file.close()
    except FileNotFoundError:
        open('resultsforprimes.txt', 'w').write(HEADER)
    
    isprime = '' if isprime is False else True
    
    file = open('resultsforprimes.txt', 'a')
    file.write('-'*61 + '\n')
    file.write(str(inpt).rjust(12) + SPACE + str(result).rjust(30) + SPACE + str(isprime).rjust(13) + '\n')
    file.write('-'*61 + '\n')
    file.close()

def totalprimes():
    total = 0
    file = open('resultsforprimes.txt', 'r')
    for line in file.readlines():
        if 'True' in line:
            total += 1
    file.close()
    open('resultsforprimes.txt', 'a').write('Total prime numbers:' + ' '*35 + str(total).rjust(6) + '\n')

def main(times, start=0):
    for i in range(start, times):
        prime(i)
    totalprimes()
    print('Statistics exported to resultsforprimes.txt with success')

if __name__=='__main__':
    try:
        if len(argv) == 2:
            main(int(argv[1]))
        else:
            main(int(argv[2]), start=int(argv[1]))
    except(ValueError, IndexError):
        print('Please, include as command line argument the ceiling for your prime numbers calculations')
