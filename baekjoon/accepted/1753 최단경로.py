from sys import stdin
from math import inf, isinf
import heapq


def solution(V, E, K, edges):
    tree = {}
    for s, e, c in edges:
        d = tree.setdefault(s, {})
        d[e] = min([d.get(e, inf), c])  # !KILLER_CASE! merge edges into one best

    costs = {i:inf for i in range(1, V+1)}
    costs[K] = 0
    heap = [(0, K)]
    while heap:
        _, node = heapq.heappop(heap)
        for next_node, cost in tree.get(node, {}).items():
            if costs[next_node] > costs[node] + cost:
                costs[next_node] = costs[node] + cost
                heapq.heappush(heap, (costs[next_node], next_node))

    return costs


V, E, K, edges = 0, 0, 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        V, E = [int(c) for c in row.strip().split(' ')]
    elif i == 1:
        K = int(row)
    else:
        edges.append([int(c) for c in row.strip().split(' ')])

result = solution(V, E, K, edges)

for i in range(1, V+1):
    if isinf(result[i]):
        print('INF')
    else:
        print(result[i])

"""
3 2
3
1 3 10
2 1 4
"""
"""
4 8
1
1 2 3
2 1 5
4 3 4
2 3 10
1 3 10
2 4 1
3 1 1
"""
"""
5 6
5
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""
"""
5 8
5
1 3 6
1 4 3
2 1 3
3 4 2
4 3 1
4 2 1
5 2 4
5 4 2
"""