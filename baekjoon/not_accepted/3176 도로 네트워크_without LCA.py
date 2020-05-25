# didn't know what LCA is
# time over
from sys import stdin
from math import inf
from collections import deque


def solution(N, roads, K, travels):
    routes = {}
    for a, b, c in roads:
        routes.setdefault(a, {})[b] = c
        routes.setdefault(b, {})[a] = c

    answers = []
    for start, end in travels:
        global_min, global_max = inf, -inf
        visited = {start}
        que = deque([(start, inf, -inf)])
        while que:
            current, local_min, local_max = que.popleft()
            if current == end:
                global_min = min([global_min, local_min])
                global_max = max([global_max, local_max])

            for go_to, cost in routes[current].items():
                if go_to not in visited:
                    visited.add(go_to)
                    que.append((go_to, min([local_min, cost]), max([local_max, cost])))
        answers.append((global_min, global_max))

    return answers

N, roads, K, travels = 0, [], 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    elif i < N:
        roads.append([int(c) for c in row.strip().split(' ')])
    elif i == N:
        K = int(row)
    else:
        travels.append([int(c) for c in row.strip().split(' ')])

for mi, ma in solution(N, roads, K, travels):
    print(f'{mi} {ma}')
