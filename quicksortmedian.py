#!/usr/bin/python3
# Easy peasy lemon squeezy
# My implementation of the quicksort(with median to find a best pivot)
# Gabriel Fernandes

from random import randint
from random import shuffle
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


# Sem array auxiliar e sem mexer na posicao de ninguem
def median(array, lbound, rbound):
    med = lbound
    ocurr = 1
    for i in range(lbound + 1, rbound + 1):
        if array[i] < array[med]:
            med = i
            ocurr = 1
        elif array[i] == array[med]:
            ocurr += 1

    middle = (lbound + rbound) // 2
    total = lbound + ocurr
    while total <= middle:
        minor = minorafter(array, med, lbound, rbound)
        med = minor[0]
        total += minor[1]

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


def mediantest():
    array = [3, 6, 7, 1, 4, 2, 5]
    med = median(array, 0, len(array) - 1)
    assert array[med] == 4

    array = [1, 1, 1]
    med = median(array, 0, len(array) - 1)
    assert array[med] == 1

    array = [1]
    med = median(array, 0, len(array) - 1)
    assert med == 0

    array = [2, 1, 2, 1]
    med = median(array, 0, len(array) - 1)
    assert med == 1

    array = [3, 1, 2]
    med = median(array, 0, len(array) - 1)
    assert med == 2
    assert array[med] == 2

    array = [3, 1, 2]
    med = median(array, 0, len(array) - 1)
    assert med == 2
    assert array[med] == 2

    array = [7, 5, 1, 3, 6, 4, 2]
    med = median(array, 0, len(array) - 1)
    assert med == 5
    assert array[med] == 4

    array = [4, 1, 5, 6, 3, 2, 4]
    med = median(array, 0, len(array) - 1)
    arr_sorted = array.copy()
    arr_sorted.sort()
    del arr_sorted[:len(arr_sorted)//2]
    assert med == array.index(arr_sorted[0])
    assert array[med] == arr_sorted[0]

    array = [3, 1, 5, 6, 3, 2, 4]
    med = median(array, 0, len(array) - 1)
    arr_sorted = array.copy()
    arr_sorted.sort()
    del arr_sorted[:len(arr_sorted)//2]
    assert med == array.index(arr_sorted[0])
    assert array[med] == arr_sorted[0]

    array = [randint(0, 9) for i in range(randint(1, 100))]
    med = median(array, 0, len(array) - 1)
    arr_sorted = array.copy()
    arr_sorted.sort()
    middle = len(arr_sorted)//2 if len(arr_sorted) % 2 == 1 else len(arr_sorted)//2 - 1
    del arr_sorted[:middle]
    assert med == array.index(arr_sorted[0])
    assert array[med] == arr_sorted[0]


if __name__ == '__main__':
    start = time()

    test()
    test2()
    test3()

    minortest()
    mediantest()

    print('Success!')
    print('Passed time: {:.9f} secs'.format(time()-start))
