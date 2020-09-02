from sys import stdin


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
    # calculate min dist
    coords = [(*coord, i) for i, coord in enumerate(coords)]
    min_dist = {}
    for axis in range(3):
        coords.sort(key=lambda x: x[axis])
        for i in range(N - 1):
            here, there = coords[i], coords[i + 1]
            dist = abs(here[axis] - there[axis])
            min_dist[(here[3], there[3])] = min(min_dist.get((here[3], there[3]), float('inf')), dist)
    min_dist = sorted(min_dist.items(), key=lambda x: x[1])
    # search MST
    total_c = 0
    tree = [i for i in range(N)]
    tree_height = [1 for _ in range(N)]
    for (a, b), cost in min_dist:
        if ds_union(a, b, tree, tree_height):
            total_c += cost
    return total_c


N = int(stdin.readline())
coords = []
for _ in range(N):
    coords.append([int(c) for c in stdin.readline().strip().split(' ')])

print(solution(N, coords))
