from sys import stdin
from collections import deque


def rotate(board, sx, sy, size):
    b, s = board, size - 1
    for x in range(size // 2):
        for y in range(size // 2):
            b[sx + x][sy + y], b[sx + y][sy + s - x], b[sx + s - x][sy + s - y], b[sx + s - y][sy + x] \
                = b[sx + s - y][sy + x], b[sx + x][sy + y], b[sx + y][sy + s - x], b[sx + s - x][sy + s - y]


DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)


def update_ice(board):
    L = len(board)

    minused = [[False] * L for _ in range(L)]
    for x, row in enumerate(board):
        for y, v in enumerate(board):
            count = 0
            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if 0 <= nx < L and 0 <= ny < L:
                    if nx <= x and ny <= y:
                        if minused[nx][ny] or board[nx][ny]:
                            count += 1
                    elif board[nx][ny]:
                        count += 1
            if count < 3 and board[x][y]:
                minused[x][y] = True
                board[x][y] -= 1


def calc_biggest_chunk(board):
    L = len(board)

    biggest = 0
    checked = [[False] * L for _ in range(L)]
    for x in range(L):
        for y in range(L):
            if checked[x][y]:
                continue
            checked[x][y] = True
            if not board[x][y]:
                continue

            count = 0
            que = deque([(x, y)])
            while que:
                x, y = que.popleft()
                count += 1
                for dx, dy in DELTA:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < L and 0 <= ny < L and not checked[nx][ny] and board[nx][ny]:
                        checked[nx][ny] = True
                        que.append((nx, ny))
            biggest = max(biggest, count)
    return biggest


def count_ice(board):
    return sum(sum(row) for row in board)


def board_divide(spell, N):
    size = 2 ** spell
    for x in range(0, 2 ** N, size):
        for y in range(0, 2 ** N, size):
            yield x, y, size


def solution(N, Q, board, spells):
    for spell in spells:
        for args in board_divide(spell, N):
            rotate(board, *args)
        update_ice(board)

    return count_ice(board), calc_biggest_chunk(board)


lexer = lambda: list(map(int, stdin.readline().strip().split(' ')))
N, Q = lexer()
board = [lexer() for _ in range(2 ** N)]
spells = lexer()

for a in solution(N, Q, board, spells):
    print(a)

"""
2 1
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
0
"""
