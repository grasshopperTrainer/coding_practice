from sys import stdin
from collections import deque


def solution(R, C, board):
    DELTA = ((0, 1), (0, -1), (1, 0), (-1, 0))
    # dfs
    best_score = 0
    que = deque([(0, 0, board[0][0])])
    while que:
        x, y, alpha_used = que.pop()
        for dx, dy in DELTA:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in alpha_used:
                que.append((nx, ny, alpha_used+board[nx][ny]))
        best_score = max(best_score, len(alpha_used))
    return best_score


R, C = [int(c) for c in stdin.readline().strip().split(' ')]
board = [stdin.readline().strip() for _ in range(R)]
print(solution(R, C, board))

"""
2 4
CAKB
ADLQ
"""
