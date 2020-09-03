from sys import stdin


def ds_root(node, tree):
    if tree[node] == node:
        return node
    tree[node] = ds_root(tree[node], tree)
    return tree[node]


def ds_union(a, b, tree, tree_height):
    roots = [ds_root(node, tree) for node in (a, b)]
    if roots[0] == roots[1]:
        return False
    heights = [tree_height[node] for node in roots]
    if heights[0] > heights[1]:
        tree[roots[1]] = roots[0]
    else:
        tree[roots[0]] = roots[1]
        if heights[0] == heights[1]:
            tree_height[roots[1]] += 1
    return True


def solution(N, M, K, prices, friends):
    edges = []
    for a, b in friends:
        edges.append((0, a, b))
    for f, p in enumerate(prices, 1):
        edges.append((p, 0, f))
    edges.sort()

    tree = [i for i in range(N+1)]
    tree_height = [1 for _ in range(N+1)]
    spent = 0
    for p, a, b in edges:
        if ds_union(a, b, tree, tree_height):
            spent += p
        if spent > K:
            return "Oh no"
    return spent


N, M, K = 0, 0, 0
prices = []
friends = []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, M, K = row
    elif i == 1:
        prices = row
    else:
        friends.append(row)

print(solution(N, M, K, prices, friends))