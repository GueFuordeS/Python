#! /usr/bin/python3
# Gabriel Fernandes

from multiprocessing import Pool
from time import sleep


def pin(id):
    print('Hello, i\'m the', id)
    sleep(5)
    print('Goodbye, i\'m the', id)


if __name__ == '__main__':
    with Pool(10) as p:
        p.map(pin, range(10))
