from sys import stdin
from collections import deque


def solution(N, M, board):
    SPACE, WALL = 'S', 'W'
    DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for x in range(N):
        for y in range(M):
            if board[x][y] == 0:
                board[x][y] = WALL
            elif board[x][y] == 1:
                board[x][y] = SPACE
    board[0][0] = 1

    que = deque([(0,0)])
    while que:
        x, y = que.popleft()
        for dx, dy in DELTAS:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == SPACE:
                board[nx][ny] = board[x][y] + 1
                que.append((nx, ny))
    
    return board[N-1][M-1]


N, M, board = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N, M = [int(c) for c in row.strip().split(' ')]
    else:
        board.append([int(c) for c in row.strip()])

print(solution(N, M, board))