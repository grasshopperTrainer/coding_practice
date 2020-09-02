from sys import stdin
from math import sqrt


def ds_root(node, tree):
    if tree[node] == node:
        return node
    root = ds_root(tree[node], tree)
    tree[node] = root
    return root


def ds_union(a, b, tree, tree_height):
    roots = [ds_root(node, tree) for node in (a, b)]
    if roots[0] == roots[1]:
        return False

    heights = [tree_height[root] for root in roots]
    if heights[0] < heights[1]:
        tree[roots[0]] = roots[1]
    else:
        tree[roots[1]] = roots[0]
        if heights[0] == heights[1]:
            tree_height[roots[0]] += 1
    return True


def solution(N, coords):
    # draw tree
    tree = [i for i in range(N)]
    tree_height = [1 for _ in range(N)]

    dists = []
    for i in range(N):
        for j in range(i + 1, N):
            a, b = coords[i], coords[j]
            d = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
            dists.append((d, i, j))
    dists.sort()

    cost = 0
    for c, a, b in dists:
        if ds_union(a, b, tree, tree_height):
            cost += c
    return cost


N = int(stdin.readline())
coords = []
for _ in range(N):
    coords.append([float(c) for c in stdin.readline().strip().split(' ')])

print(solution(N, coords))
