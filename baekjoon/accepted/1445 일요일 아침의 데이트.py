from sys import stdin
from collections import deque


def solution(N, M, board):
    TRASH, NEAR, EMPTY = 'g', 'n', '.'

    D = ((-1, 0), (0, -1), (1, 0), (0, 1))
    # find start, finish
    start, finish = None, None
    for x in range(N):
        for y in range(M):
            if board[x][y] == 'S':
                start = (x, y)
            elif board[x][y] == 'F':
                finish = (x, y)
            elif board[x][y] == TRASH:
                for dx, dy in D:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == EMPTY:
                        board[nx][ny] = NEAR

    rec = [[(float('inf'), float('inf')) for _ in range(M)] for _ in range(N)]
    rec[start[0]][start[1]] = (0, 0)

    que = deque([start])
    while que:
        x, y = que.popleft()
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                t = rec[x][y]
                if board[nx][ny] == NEAR:
                    t = t[0], t[1]+1
                elif board[nx][ny] == TRASH:
                    t = t[0]+1, t[1]
                if t < rec[nx][ny]:
                    rec[nx][ny] = t
                    que.append((nx, ny))

    return rec[finish[0]][finish[1]]



N, M = map(int, stdin.readline().strip().split(' '))
board = [list(stdin.readline().strip()) for _ in range(N)]

print(' '.join(map(str, solution(N, M, board))))

"""
4 1
F
g
g
S
"""