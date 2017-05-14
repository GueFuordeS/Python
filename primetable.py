#!/usr/bin/python3

from sys import argv
from time import time

def prime(num):
    start = time()
    
    if num < 2:
        return False

    if num == 2:
        compute(num, time()-start)
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, num, 2):
        if num % i == 0:
            return False

    compute(num, time()-start)
    return True

def compute(inpt, result):

    result = format(result, '.12f')

    SPACE = ' | '
    HEADER = 'Input:'.ljust(12) + SPACE + 'Spent time(in secs):'.ljust(30) + '\n'

    try:
        file = open('printedprimetable.txt', 'r+')
        if file.readline() != HEADER:
            file.write(HEADER)
            file.close()
    except FileNotFoundError:
        open('printedprimetable.txt', 'w').write(HEADER)
    
    file = open('printedprimetable.txt', 'a')
    file.write('-'*45 + '\n')
    file.write(str(inpt).rjust(12) + SPACE + str(result).rjust(30) + '\n')
    file.write('-'*45 + '\n')
    file.close()

def totalprimes():
    total = 0
    file = open('printedprimetable.txt', 'r')
    for line in file.readlines():
        if '.' in line:
            total += 1
    file.close()
    open('printedprimetable.txt', 'a').write('Total prime numbers:'.ljust(39) + str(total).rjust(6) + '\n')

def main(times, start=0):
    if start >= times:
        print('Please, insert a ceiling number greater than the start number')
        return
    
    for i in range(start, times):
        prime(i)

    try:
        totalprimes()
        print('Statistics exported to printedprimetable.txt with success')
    except FileNotFoundError:
        print('Fail when exporting statistics')
        

if __name__=='__main__':
    try:
        if len(argv) == 2:
            main(int(argv[1]))
        else:
            main(int(argv[2]), start=int(argv[1]))
    except(ValueError, IndexError):
        print('Please, include as command line argument the ceiling for your prime numbers calculations')
