from sys import stdin


def ds_root(node, tree):
    if tree[node] == node:
        return node

    root = ds_root(tree[node], tree)
    tree[node] = root
    return root


def ds_union(a, b, tree, tree_height):
    roots = [ds_root(n, tree) for n in (a, b)]
    if roots[0] == roots[1]:
        return False

    if tree_height[roots[0]] > tree_height[roots[1]]:
        tree[roots[1]] = roots[0]
    else:
        tree[roots[0]] = roots[1]
        if tree_height[roots[0]] == tree_height[roots[1]]:
            tree_height[roots[1]] += 1
    return True


def solution(V, E, edges):
    # use disjoint set
    tree = [i for i in range(V + 1)]  # use 1indexing
    tree_height = [1 for _ in range(V + 1)]
    edges.sort(key=lambda x: x[2])

    total_c = 0
    for a, b, cost in edges:
        if ds_union(a, b, tree, tree_height):
            total_c += cost

    return total_c


V, E = 0, 0
edges = []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        V, E = row
    else:
        edges.append(row)
print(solution(V, E, edges))

"""
4 6
1 2 3
1 3 2
1 4 1
4 2 1
4 3 1
2 3 1
"""
"""
5 5
1 2 1
2 3 3
3 4 2
4 5 2
2 5 3
"""
"""
4 4
1 2 1
2 3 2
3 4 1
4 1 2
"""
"""
5 6
1 2 2
1 3 1
3 2 1
1 4 1
1 5 2
3 5 2
"""
