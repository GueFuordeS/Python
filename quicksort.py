# Easy peasy lemon squeezy
# My implementation of the quicksort(default)
# Gabriel Fernandes

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
    array = [5, 4, 3, 6, 4]
    print('Before: {0}'.format(array))
    sort(array)
    print('After:  {0}'.format(array))
