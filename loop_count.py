#!usr/bin/python3

from sys import argv
from time import time, sleep


def looping(secs):
        start = time()
        count = 0
        while True:
                if(time()-start > secs):
                        break
                count += 1
                print('%9d loops paste' %(count))

if __name__=='__main__':
        try:
               looping(float(argv[1]))
        except Exception:
                print('NaN: not a number as a argument')

