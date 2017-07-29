# Easy peasy lemon squeezy
# My implementation of the quicksort(with median to find a best pivot)
# Gabriel Fernandes

from random import randint
from random import shuffle
from pprint import pprint
from time import time

def sort(array, lbound=0, rbound=None):
    if rbound == None:
        rbound = len(array)-1

    if lbound < rbound:
        pindex = halfSelectionSort(array, lbound, rbound)
        swap(array, pindex, rbound)
        pivot = partition(array, lbound, rbound-1, rbound)
        sort(array, lbound, pivot-1)
        sort(array, pivot+1, rbound)

    return array


def halfSelectionSort(array, lbound, rbound):
    middle = (rbound - lbound) // 2
    lesser = rbound

    return lesser


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


def test():
    assert sort([4,3,2,1]) == [1,2,3,4]
    assert sort([4,2,3,1]) == [1,2,3,4]
    assert sort([4,5,3,2,1]) == [1,2,3,4,5]

    for _ in range(100):
        tmp = list(range(100))
        shuffle(tmp)
        assert sort(tmp) == list(range(100))

    return 'test pass!'


def test2():
    start = time()
    array = [randint(0,10000) for i in range(100)]
    #print('Before:')
    #pprint(array, compact=True)
    sort(array)
    #print('\nAfter:')
    #pprint(array,  compact=True)
    print('Passed time: {:.9f} secs'.format(time()-start))


def test3():
    arr = [0,1,2,3,4,5,6]
    shuffle(arr)
    #print(arr)
    sort(arr)
    #print(arr)
    assert arr == [0,1,2,3,4,5,6]


if __name__ == '__main__':
    test()
    test2()
    test3()
