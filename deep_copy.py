def deep_copy(src_list):
    new_list = []

    stack = [[new_list, src_list]]
    while len(stack) > 0:
        new, src = stack.pop()
        for e in src:
            if isinstance(e, list):
                l = []
                new.append(l)
                stack.append([l, e])
            else:
                new.append(e)

    return new_list


def deep_copy_recur(src_list):
    new_list = []

    for e in src_list:
        if isinstance(e, list):
            new_list.append(deep_copy_recur(e))
        else:
            new_list.append(e)

    return new_list
