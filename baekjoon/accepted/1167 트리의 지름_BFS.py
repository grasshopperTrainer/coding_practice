from sys import stdin
from collections import deque


def solution(N, routes):
    tree = {}
    for r in routes:
        depart = r[0]
        it = iter(r[1:])
        for n in it:
            tree.setdefault(depart, {})[n] = next(it)

    def bfs(x, tree):
        farthest = [0, 0]
        visited = {x}
        que = deque([(x, 0)])
        while que:
            depart, sum_cost = que.popleft()
            for dest, cost in tree[depart].items():
                if dest not in visited:
                    visited.add(dest)
                    if farthest[1] < sum_cost + cost:
                        farthest = dest, sum_cost + cost
                    que.append((dest, sum_cost + cost))
        return farthest

    far = bfs(1, tree)
    far_of_far = bfs(far[0], tree)
    return far_of_far[1]


N, routes = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        routes.append([int(c) for c in row.strip().split(' ')[:-1]])

print(solution(N, routes))
