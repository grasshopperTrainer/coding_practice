# reducing memory usage
# time out
from sys import stdin


def solution(N, routes):
    MAX = 10_000
    tree = {}
    for r in routes:
        depart = r[0]
        it = iter(r[1:])
        for n in it:
            tree[(depart, n)] = next(it)

    for m in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i != j and (i, m) in tree and (m, j) in tree:
                    t = tree[(i, m)] + tree[(m, j)]
                    if tree.setdefault((i, j), MAX) > t:
                        tree[(i, j)] = t

    return max(tree.values())



N, routes = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        routes.append([int(c) for c in row.strip().split(' ')[:-1]])

print(solution(N, routes))