from sys import stdin
from collections import deque


def solution(RN, CN, board):
    EMPTY, NORIPE, RIPE = -1, 0, 1
    DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    toripe = 0
    que = deque()
    for x in range(RN):
        for y in range(CN):
            if board[x][y] == RIPE:
                que.append((x, y, 0))   # x, y, day
            elif board[x][y] == NORIPE:
                toripe += 1

    day_passed = 0
    while que:
        x, y, day = que.popleft()
        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < RN and 0 <= ny < CN and board[nx][ny] == NORIPE:
                toripe -= 1
                day_passed = day + 1
                board[nx][ny] = RIPE
                que.append((nx, ny, day + 1))

    if toripe:
        return -1
    return day_passed


RN, CN, board = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        CN, RN = row
    else:
        board.append(row)

print(solution(RN, CN, board))
