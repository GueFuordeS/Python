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


def find_even_tree(tree):
    pass

def main():
    nodes, edges = map(lambda e: int(e), input().split())

    tree = {}
    tree.update({n:[1, []] for n in range(1, nodes+1)})

    for i in range(1, edges+1):
        edge = tuple(map(lambda e: int(e), input().split()))
        tree[edge[0]][0] = edge[1]
        tree[edge[1]][1].append(edge[0])


if __name__ == '__main__':
    main()
