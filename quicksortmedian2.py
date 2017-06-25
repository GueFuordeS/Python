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
    middle = (rbound-lbound)//2
    lesser = rbound
    for i in range(lbound, middle+1):
        lesser = i
        for j in range(i, rbound+1):
            if array[j] < array[lesser]:
                lesser = j
        swap(array, i, lesser)
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
