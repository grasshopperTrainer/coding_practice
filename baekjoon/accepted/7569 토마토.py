from sys import stdin
from collections import deque
from itertools import product


def solution(XN, YN, ZN, board):
    EMPTY, NORIPE, RIPE = -1, 0, 1
    DELTAS = ((0, 1, 0), (1, 0, 0),
              (0, -1, 0), (-1, 0, 0),
              (0, 0, 1), (0, 0, -1))

    toripe = 0
    que = deque()
    for x, y, z in product(*map(range, (XN, YN, ZN))):
        if board[z][y][x] == RIPE:
            que.append((x, y, z, 0))   # x, y, z, day
        elif board[z][y][x] == NORIPE:
            toripe += 1

    day_passed = 0
    while que:
        x, y, z, day = que.popleft()
        for dx, dy, dz in DELTAS:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < XN and 0 <= ny < YN and 0 <= nz < ZN and board[nz][ny][nx] == NORIPE:
                toripe -= 1
                day_passed = day + 1
                board[nz][ny][nx] = RIPE
                que.append((nx, ny, nz, day + 1))

    if toripe:
        return -1
    return day_passed


XN, YN, ZN, board = 0, 0, 0, []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        XN, YN, ZN = row
        board.append([])
    else:
        if len(board[-1]) != YN:
            board[-1].append(row)
        else:
            board.append([])
            board[-1].append(row)

print(solution(XN, YN, ZN, board))
