from sys import stdin


def ds_root(ds_tree, i):
    if ds_tree[i] == i:
        return i
    root = ds_root(ds_tree, ds_tree[i])
    ds_tree[i] = root
    return root


def ds_union(ds_tree, a, b):
    roots = ds_root(ds_tree, a), ds_root(ds_tree, b)
    if roots[0] == roots[1]:
        return
    ds_tree[roots[1]] = roots[0]


def solution(N, rects):
    ds_tree = [i for i in range(N)]
    rects.sort()

    init_reachable = False
    for i in range(N):
        x, y, xx, yy = rects[i]
        if (x <= 0 <= xx and (y == 0 or yy == 0)) or (y <= 0 <= yy and (x == 0 or xx == 0)):
            init_reachable = True

        for j in range(i + 1, N):
            a, b, c, d = rects[j]
            # touching
            if not ((x < a and c < xx and y < b and d < yy) or xx < a or c < x or yy < b or d < y):
                ds_union(ds_tree, i, j)

    roots = set()
    for i in range(N):
        roots.add(ds_root(ds_tree, i))

    count = len(roots) - 1
    if not init_reachable:
        count += 1
    return count


N = int(stdin.readline())
rects = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

print(solution(N, rects))

"""
3
1 1 4 4
-10 -10 4 5
-1 -1 100 100
"""