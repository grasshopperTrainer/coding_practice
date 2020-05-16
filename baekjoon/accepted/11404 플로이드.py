# was slower than using floyd-warshall
# guessed reasons
# 1. there is waste when tree is not mono directional - has many returning pathes
# 2. there is an overhead initiating dijkstra and merging result

from sys import stdin
from math import inf, isinf
import heapq


def solution(N, buses):
    tree = {}
    for s, e, c in buses:
        d = tree.setdefault(s, {})
        d[e] = min([d.get(e, inf), c])

    answer = [[0]*N for _ in range(N)]
    for origin in range(1, N+1):
        costs = {i: inf for i in range(1, N+1)}
        costs[origin] = 0
        heap = [(0, origin)]
        while heap:
            _, node = heapq.heappop(heap)
            for next_node, cost in tree.get(node, {}).items():
                if costs[next_node] > costs[node] + cost:
                    costs[next_node] = costs[node] + cost
                    heapq.heappush(heap, (costs[next_node], next_node))

        for i in range(1, N+1):
            answer[origin-1][i-1] = 0 if isinf(costs[i]) else costs[i]

    return answer


N, M, buses = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    elif i == 1:
        M = int(row)
    else:
        buses.append([int(c) for c in row.strip().split(' ')])

for row in solution(N, buses):
    print(' '.join([str(i) for i in row]))