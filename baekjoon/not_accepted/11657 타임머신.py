from sys import stdin
import heapq
from math import inf, isinf


def solution(N, edges):
    tree = {}
    for s, e, c in edges:
        # !KILLER CASE! for implicit description
        # almost always use this pattern to store best out of duplicate
        d = tree.setdefault(s, {})
        d[e] = min([d.get(e, inf), c])

    costs = {i: [inf, 0] for i in range(1, N+1)}    # {idx: [cost, renewal count]}
    costs[1] = [0, 0]
    heap = [(0, 1)]

    while heap:
        _, node = heapq.heappop(heap)

        for next_node, time in tree.get(node, {}).items():
            if costs[next_node][0] > costs[node][0] + time:
                # max renewal count in N-1
                # trying one more time means a loop!
                if costs[next_node][1] == N:
                    return [-1]
                costs[next_node][1] += 1

                costs[next_node][0] = costs[node][0] + time
                heapq.heappush(heap, (costs[next_node][0], next_node))

    result = []
    for i in range(2, N+1):
        if isinf(costs[i][0]):
            result.append(-1)
        else:
            result.append(costs[i][0])
    return result


N, M, edges = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, M = row
    else:
        edges.append(row)

for a in solution(N, edges):
    print(a)