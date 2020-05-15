from sys import stdin
from math import inf, isinf
import heapq


def solution(N, E, edges, prior):
    tree = {}
    for a, b, c in edges:
        tree.setdefault(a, {})[b] = c
        tree.setdefault(b, {})[a] = c

    def shortest_path(n, tree, origin):
        costs = {i:inf for i in range(1, n+1)}
        costs[origin] = 0
        heap = [(0, origin)]
        while heap:
            _, node = heapq.heappop(heap)
            for next_node, cost in tree.get(node, {}).items():
                if costs[next_node] > costs[node] + cost:
                    costs[next_node] = costs[node] + cost
                    heapq.heappush(heap, (costs[next_node], next_node))
        return costs

    start_to_middle = shortest_path(N, tree, 1)
    middle_to_middle = shortest_path(N, tree, prior[0])
    end_to_middle = shortest_path(N, tree, N)
    a = start_to_middle[prior[0]] + middle_to_middle[prior[1]] + end_to_middle[prior[1]]
    b = start_to_middle[prior[1]] + middle_to_middle[prior[1]] + end_to_middle[prior[0]]
    shortest = min([a, b])
    # !KILLER CASE! impossible route is possible when there are more than one independent branches
    if isinf(shortest):
        return -1
    return shortest


N, E, edges, prior = 0, 0, [], []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, E = row
    elif i < E+1:
        edges.append(row)
    else:
        prior = row

print(solution(N, E, edges, prior))