def merge(l1, l2):
    i, j, l3 = 0, 0, []
    l1f = len(l1)-1; l2f = len(l2)-1

    while i <= l1f and j <= l2f:
        if l1[i] <= l2[j]:
            l3.append(l1[i])
            i += 1

        else:
            l3.append(l2[j])
            j += 1

    while i <= l1f:
        l3.append(l1[i])
        i += 1

    while j <= l2f:
        l3.append(l2[j])
        j += 1

    return l3

if __name__ == '__main__':
    print(merge([-2,7,12], [3,4,6,9,11]))
