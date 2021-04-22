from sys import stdin
from math import floor


def solution(N, board):
    MOVEDELTA = (0, -1), (1, 0), (0, 1), (-1, 0)
    FLYDELTA = (((-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (1, -1), (1, 0), (1, 1), (2, 0)),
                ((0, -2), (1, -1), (0, -1), (-1, -1), (2, 0), (1, 1), (0, 1), (-1, 1), (0, 2)),
                ((2, 0), (1, 1), (1, 0), (1, -1), (0, 2), (-1, 1), (-1, 0), (-1, -1), (-2, 0)),
                ((0, 2), (-1, 1), (0, 1), (1, 1), (-2, 0), (-1, -1), (0, -1), (1, -1), (0, -2)),
                )
    FLYRATE = (0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02)

    outside = 0
    x = y = N // 2
    offset, facing, move_count, rotate_count = 1, 0, 0, 0
    while True:
        # calc next pos
        dx, dy = MOVEDELTA[facing]
        x, y = x + dx, y + dy

        fly_sum = 0
        for (fx, fy), r in zip(FLYDELTA[facing], FLYRATE):
            fly = floor(board[x][y] * r)
            fly_sum += fly
            nx, ny = x + fx, y + fy
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] += fly
            else:
                outside += fly

        # calc alpha
        fly_left = board[x][y] - fly_sum
        board[x][y] = 0
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] += fly_left
        else:
            outside += fly_left

        # control next move
        move_count += 1
        if move_count == offset:
            move_count = 0
            facing = (facing + 1) % 4
            rotate_count += 1
            if rotate_count == 2:
                offset += 1
                rotate_count = 0
        if (x, y) == (0, 0):
            break
    return outside


N = int(stdin.readline())
board = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

print(solution(N, board))
