# Easy peasy lemon squeezy
# My implementation of the quicksort(default)
# Gabriel Fernandes

def sort(array, lbound=0, rbound=None):
    if rbound == None:
        rbound = len(array)-1

    if lbound < rbound:
        pivot = partition(array, lbound, lbound, rbound-1, rbound)
        sort(array, lbound, pivot-1)
        sort(array, pivot+1, rbound)


def partition(array, lbound, lhand, rhand, rbound):
    if lhand < rhand:
        if array[lhand] > array[rbound] and array[rhand] < array[rbound]:
            array[lhand], array[rhand] = array[rhand], array[lhand]
            return partition(array, lbound, lhand+1, rhand-1, rbound)
        elif array[lhand] > array[rbound]:
            return partition(array, lbound, lhand, rhand-1, rbound)
        elif array[rhand] < array[rbound]:
            return partition(array, lbound, lhand+1, rhand, rbound)
        else:
            return partition(array, lbound, lhand+1, rhand-1, rbound)

    else:
        if array[rhand] >= array[rbound]:
            array[rhand], array[rbound] = array[rbound], array[rhand]
            return rhand
        else:
            array[rhand+1], array[rbound] = array[rbound], array[rhand+1]
            return rhand+1


if __name__=='__main__':
    array = [3,8,1,0,2,5,1,7,3]
    print('Before: {0}'.format(array))
    sort(array)
    print('After: {0}'.format(array))
