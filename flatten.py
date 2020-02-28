def flatten(src_list):
    new_list = []

    stack = [[src_list, 0]]
    while len(stack) > 0:
        broke = False
        l, i = stack[-1]
        for j in range(i, len(l)):
            if isinstance(l[j], list):
                stack[-1][1] = j + 1
                stack.append([l[j], 0])
                broke = True
                break
            new_list.append(l[j])
        if not broke:
            stack.pop()

    return new_list


def flatten_recur(src_list):
    new_list = []

    for e in src_list:
        if isinstance(e, list):
            new_list.extend(flatten_recur(e))
        else:
            new_list.append(e)

    return new_list
