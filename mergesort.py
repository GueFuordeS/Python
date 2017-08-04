#!/usr/bin/python
# Gabriel Fernandes


from time import time
import random


def sort(array, lbound=0, rbound=None):
    if rbound == None:
        rbound = len(array)-1

    if lbound < rbound:
        mid = (lbound+rbound)//2
        sort(array, lbound, mid)
        sort(array, mid+1, rbound)
        merge(array, lbound, mid, rbound)

    return array


def merge(array, lbound, mid, rbound):
    aux = array[lbound:rbound+1]
    mid -= lbound
    rbound -= lbound
    i, j, k = 0, mid+1, lbound

    while i <= mid and j <= rbound:
        if aux[i] <= aux[j]:
            array[k] = aux[i]
            i += 1
            k += 1
        else:
            array[k] = aux[j]
            j += 1
            k += 1

    while i <= mid:
        array[k] = aux[i]
        i += 1
        k += 1
    while j <= rbound:
        array[k] = aux[j]
        j += 1
        k += 1


def test():
    assert sort([4,3,2,1]) == [1,2,3,4]
    assert sort([4,2,3,1]) == [1,2,3,4]
    assert sort([4,5,3,2,1]) == [1,2,3,4,5]

    arr = list(range(100))
    for _ in arr:
        tmp = arr[:]
        random.shuffle(tmp)
        assert id(arr) != id(tmp)
        assert sort(tmp) == arr

    return 'test pass!'


def benchmark():
    start = time()
    arr = [i for i in range(1000000)]
    arr2 = arr[:]
    random.shuffle(arr)
    assert arr != arr2
    sort(arr)
    assert arr == arr2

    print('Taked time: {:.9f} secs'.format(time()-start))


if __name__=='__main__':
    #test()
    benchmark()
