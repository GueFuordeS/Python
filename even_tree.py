def yield_leaf(tree):
    for node in tree:
        if(tree[node][1] == []):
            return node


def cut_subtree(tree, leading):
    childs = tree[leading][1][:]
    for child in childs:
        cut_subtree(tree, child)
    if leading != tree[leading][0]:
        tree[tree[leading][0]][1].remove(leading)
    tree.pop(leading)


def reach_even_tree(tree, leaf):
    reached = False
    node_counting = 1
    node = leaf
    while not reached:
        node = tree[node][0]
        node_counting += 1
        for child in tree[node][1]:
            node_counting += 1
        node_counting -= 1
        if (node_counting % 2 == 0):
            reached = True
    cut_subtree(tree, node)


def main():
    nodes, edges = map(lambda e: int(e), input().split())

    tree = {}
    tree.update({n:[1, []] for n in range(1, nodes+1)})

    for i in range(1, edges+1):
        edge = tuple(map(lambda e: int(e), input().split()))
        tree[edge[0]][0] = edge[1]
        tree[edge[1]][1].append(edge[0])

    cuts_counting = -1
    while (tree != {}):
        reach_even_tree(tree, yield_leaf(tree))
        cuts_counting += 1
    print(cuts_counting)


if __name__ == '__main__':
    main()
