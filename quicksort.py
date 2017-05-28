# Easy peasy lemon squeezy
# My implementation of the quicksort(default)
# Gabriel Fernandes

from random import randint
from pprint import pprint
from time import time

def sort(array, lbound=0, rbound=None):
    if rbound == None:
        rbound = len(array)-1

    if lbound < rbound:
        pivot = partition(array, lbound, rbound-1, rbound)
        sort(array, lbound, pivot-1)
        sort(array, pivot+1, rbound)


def partition(array, lhand, rhand, rbound):
    if lhand < rhand:
        if array[lhand] <= array[rbound]:
            return partition(array, lhand+1, rhand, rbound)
        
        if array[rhand] >= array[rbound]:
            return partition(array, lhand, rhand-1, rbound)

        swap(array, lhand, rhand)
        return partition(array, lhand+1, rhand-1, rbound)

    if array[rhand] >= array[rbound]:
        swap(array, rhand, rbound)
        return rhand

    swap(array, rhand+1, rbound)
    return rhand+1


def swap(array, lindex, rindex):
    array[lindex], array[rindex] = array[rindex], array[lindex]


if __name__=='__main__':
    start = time()
    array = [randint(0,10000) for i in range(1000)]
    print('Before:')
    pprint(array, compact=True, width=50)
    sort(array)
    print('\nAfter:')
    pprint(array,  compact=True, width=50)
    print('\nTime passed: {:.9f}'.format(time()-start))
