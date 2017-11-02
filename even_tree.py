def cut_subtree(tree, leading):
    childs = tree[leading][1][:]
    for child in childs:
        cut_subtree(tree, child)
    if leading != tree[leading][0]:
        tree[tree[leading][0]][1].remove(leading)
    tree.pop(leading)


def yield_tree_nvls(tree, max_nvl):
    for nvl in range(max_nvl, 0, -1):
        for node in list(tree.keys()):
            try:
                if tree[node][2] == nvl:
                    yield node
            except KeyError:
                pass


def subtree_size(tree, node):
    size = 1
    for child in tree[node][1]:
        size += subtree_size(tree, child)
    return size


def main():
    max_nvl = 2
    nodes, edges = map(lambda e: int(e), input().split())
    tree = {n:[1, [], 1] for n in range(1, nodes+1)}

    for _ in range(edges):
        edge = tuple(map(lambda e: int(e), input().split()))
        tree[edge[0]][0] = edge[1]
        tree[edge[0]][2] += tree[edge[1]][2]
        if max_nvl < tree[edge[0]][2]:
            max_nvl = tree[edge[0]][2]
        tree[edge[1]][1].append(edge[0])

    cutted_edges = -1
    for node in yield_tree_nvls(tree, max_nvl):
        if subtree_size(tree, tree[node][0]) % 2 == 0:
            cut_subtree(tree, tree[node][0])
            cutted_edges += 1
    print(cutted_edges)


if __name__ == '__main__':
    main()
