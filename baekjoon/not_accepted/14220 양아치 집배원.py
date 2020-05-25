# memory over
from sys import stdin
from math import inf, isinf
import heapq


def solution(N, board):
    L = len(board)
    min_cost = inf

    for origin in range(L):
        record = {i: inf for i in range(L)}
        record[origin] = 0
        heap = [(0, 1, origin)]
        while heap:
            cost, visited, node = heapq.heappop(heap)
            if cost > record[node] or record[node] > min_cost:
                continue
            if visited == N:
                min_cost = min([min_cost, record[node]])
                break
            for next_node, next_cost in enumerate(board[node]):
                if next_cost == 0:
                    continue
                if record[next_node] > record[node] + next_cost or visited < N:
                    record[next_node] = record[node] + next_cost
                    heapq.heappush(heap, (record[next_node], visited+1, next_node))

    return min_cost if not isinf(min_cost) else -1


N, board = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        board.append([int(c) for c in row.strip().split(' ')])

print(solution(N, board))
"""
2
0 1
1 0
"""
"""
10
0 1
1 0
"""