from sys import stdin
from math import inf, isinf
import heapq


def solution(N, buses):
    board = [[inf]*N for _ in range(N)]
    for s, e, c in buses:
        s, e = s-1, e-1
        board[s][e] = min([board[s][e], c])

    for m in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                t = board[i][m] + board[m][j]
                if t < board[i][j]:
                    board[i][j] = t
    for i in range(N):
        for j in range(N):
            if isinf(board[i][j]):
                board[i][j] = 0
    return board


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