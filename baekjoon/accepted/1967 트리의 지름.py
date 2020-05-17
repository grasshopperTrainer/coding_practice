from sys import stdin
from collections import deque


def solution(N, nodes):
    tree = {}
    for s, e, d in nodes:
        tree.setdefault(s, {})[e] = d
        tree.setdefault(e, {})[s] = d

    def bfs(tree, origin):
        farthest = [0, 0]
        visited = {origin}
        que = deque([(0, origin)])
        while que:
            dist_sum, node = que.popleft()
            for child, dist in tree.get(node, {}).items():
                if child not in visited:
                    visited.add(child)
                    dt = dist_sum + dist
                    que.append([dt, child])
                    if dt > farthest[0]:
                        farthest = dt, child
        return farthest

    to_far = bfs(tree, 1)
    far_to_far = bfs(tree, to_far[1])
    return far_to_far[0]


N, nodes = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        nodes.append([int(c) for c in row.strip().split(' ')])

print(solution(N, nodes))