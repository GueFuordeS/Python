#! /usr/bin/python3
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
    lesser = lbound
    ocurr = 1
    for i in range(lbound + 1, rbound + 1):
        if array[i] == array[lesser]:
            ocurr += 1
        elif array[i] < array[lesser]:
            lesser = i
            ocurr = 1

    middle = (lbound + rbound) // 2
    index = lbound
    med = lesser
    while index + ocurr < middle:
        minor = minorafter(array, med, lbound, rbound)
        if array[med] == array[minor]:
            ocurr += 1
        med = minor
        index += 1
    print(ocurr)
    return med


def minorafter(array, index, lbound, rbound):
    minor = None
    ocurr = 0
    i = lbound
    while minor == None and i <= rbound:
        if array[index] < array[i]:
            minor = i
            ocurr += 1
        i += 1
    while minor != None and i <= rbound:
        if array[i] < array[minor] and array[i] > array[index]:
            minor = i
            ocurr = 1
        elif array[i] == array[minor] and i != minor:
            ocurr += 1
        i += 1

    return (minor, ocurr)


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
    l = [9,7,8,2,1,7,0,7]
    minor = minorafter(l, 3, 0, len(l)-1)
    assert l[minor[0]] == 7
    assert minor[1] == l.count(7)

    l = [1,2,3,4,5,6]
    minor = minorafter(l, 4, 0, len(l)-1)
    assert l[minor[0]] == 6
    assert minor[1] == 1

    l = [4,5,1,2,6,3]
    minor = minorafter(l, 4, 0, len(l)-1)
    assert minor[0] == None
    assert minor[1] == 0

    length = randint(1, 100)
    array = [randint(1, 10) for i in range(length)]
    array.sort()
    elem_index = randint(0, length-1)
    minor = minorafter(array, elem_index, 0, length-1)
    '''
    print(array)
    print('elem:', array[elem_index])
    print('minor:', array[minor[0]] if minor[0] != None else None)
    print('ocurr:',minor[1])
    '''
    if minor[0] != None:
        assert array.count(array[minor[0]]) == minor[1]
    else:
        assert max(array) == array[elem_index]


if __name__ == '__main__':
    '''
    test()
    test2()
    test3()
    '''
    minortest()
