from sys import stdin
from collections import deque


def solution(N, ants, edges):
    ROOT = 1
    graph = {}
    for a, b, c in edges:
        graph.setdefault(a, {})[b] = c
        graph.setdefault(b, {})[a] = c

    tree, visited = [(0, float('inf')) for _ in range(N+1)], [0 for _ in range(N+1)]
    visited[ROOT] = 1
    que = deque([ROOT])
    while que:
        at = que.popleft()
        for child, cost in graph[at].items():
            if not visited[child]:
                visited[child] = 1
                tree[child] = (at, cost)
                que.append(child)

    answers = []
    for i in range(1, N+1):
        at, energy = i, ants[i-1]
        while True:
            parent, to_parent = tree[at]
            if to_parent <= energy:
                at = parent
                energy -= to_parent
            else:
                answers.append(at)
                break

    return answers


N = int(stdin.readline())
ants = [int(stdin.readline()) for i in range(N)]
edges = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N-1)]

for a in solution(N, ants, edges):
    print(a)