# PyPy3 accepted
# Python3 time over. can it be faster?
from sys import stdin
from math import inf, isinf


def solution(V, edges):
    board = [[inf]*V for _ in range(V)]
    for s, e, c in edges:
        board[s-1][e-1] = c

    min_dist = inf
    for m in range(V):
        for i in range(V):
            for j in range(V):
                if i == m == j:
                    continue
                t = board[i][m] + board[m][j]
                if t < board[i][j]:
                    board[i][j] = t
                    if i == j:
                        min_dist = min([min_dist, t])

    return min_dist if not isinf(min_dist) else -1


V, E, edges = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        V, E = row
    else:
        edges.append(row)

print(solution(V, edges))