# results in exceeding memory limit
from sys import stdin, setrecursionlimit
from collections import deque


def solution(RN, CN, board):
    setrecursionlimit(1_000*1_000)
    EMPTY, NORIPE, RIPE = -1, 0, 1
    DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    toripe = 0
    que = deque()
    for x in range(RN):
        for y in range(CN):
            if board[x][y] == RIPE:
                que.append((x, y))
            elif board[x][y] == NORIPE:
                toripe += 1

    def spread(ripe, day, count):
        if not ripe:
            return day-1, count

        new_que = deque()
        while ripe:
            x, y = ripe.popleft()
            for dx, dy in DELTAS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < RN and 0 <= ny < CN and board[nx][ny] == NORIPE:
                    board[nx][ny] = RIPE
                    new_que.append((nx, ny))

        return spread(new_que, day + 1, count + len(new_que))

    day, riped = spread(que, 0, 0)
    if riped != toripe:
        return -1
    return day


RN, CN, board = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        CN, RN = row
    else:
        board.append(row)

print(solution(RN, CN, board))
