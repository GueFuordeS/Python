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
        pindex = median(array, lbound, rbound)
        swap(array, pindex, rbound)
        pivot = partition(array, lbound, rbound-1, rbound)
        sort(array, lbound, pivot-1)
        sort(array, pivot+1, rbound)

    return array


def median(array, lbound, rbound):
    middle = (lbound + rbound) // 2

    med = rbound
    for i in range(lbound, rbound):
        if array[i] < array[med]:
            med = i

    index = lbound
    ocurr = 0

    while index + ocurr <= middle:
        lesser = lbound if med != lbound else lbound + 1
        for i in range(lbound, rbound + 1):
            if array[i] > array[med]:
                if array[i] < array[lesser]:
                    lesser = i
                if array[i] == array[med] and i != med:
                    ocurr += 1
        med = lesser
        index += 1

        return med


def minorafter(array, index):
    minor = None
    for i in range(len(array)):
        if array[i] >= array[index] and i != index:
            if minor == None:
                minor = i
            elif array[i] < array[minor]:
                minor = i
    return minor


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
    copy = array.copy()


    sort(array)
    copy.sort()

    assert array == copy
    print('Passed time: {:.9f} secs'.format(time()-start))


def test3():
    arr = [0,1,2,3,4,5,6]
    shuffle(arr)
    #print(arr)
    sort(arr)
    #print(arr)
    assert arr == [0,1,2,3,4,5,6]


def minortest():
    length = randint(0,20)
    l = [randint(0,9) for i in range(length)]
    for i in range(len(l)):
        try:
            index = minorafter(l, i)
            assert l[i] <= l[index] and i != index
        except TypeError:
            assert l[i] == max(l) and index == None


if __name__ == '__main__':
    test()
    test2()
    test3()
    minortest()
