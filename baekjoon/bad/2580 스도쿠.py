# works well but not accepted by BJOJ
from sys import stdin
from itertools import product


def solution(board):
    EMPTY = 0

    def group_of(x, y):
        return x//3*3 + y//3

    empties = []
    pools = [[set(range(1, 10)) for _ in range(9)] for _ in range(3)]
    for x, y in product(range(9), repeat=2):
        v = board[x][y]
        if v == EMPTY:
            empties.append([x, y])
            continue

        if v in pools[0][x]:
            pools[0][x].remove(v)
        if v in pools[1][y]:
            pools[1][y].remove(v)
        if v in pools[2][group_of(x, y)]:
            pools[2][group_of(x, y)].remove(v)

    def fill(empties):
        if not empties:  # no empty left means success in filling
            return True

        x, y = empties.pop()

        # len candidates being 0 is inconsistency function is looking for
        # and will skip for loop automatically resulting returning False
        candidates = pools[0][x] & pools[1][y] & pools[2][group_of(x, y)]
        for c in candidates:
            board[x][y] = c
            pools[0][x].remove(c)
            pools[1][y].remove(c)
            pools[2][group_of(x, y)].remove(c)
            if fill(empties):
                return True
            # return into pool for next try
            pools[0][x].add(c)
            pools[1][y].add(c)
            pools[2][group_of(x, y)].add(c)
        # need to return this position for next try
        empties.append((x, y))
        return False

    fill(empties)
    return board


# board = []
# for row in stdin.readlines():
#     board.append([int(c) for c in row.strip().split(' ')])

# test
board = [[0]*9 for _ in range(9)]

for row in solution(board):
    print(' '.join([str(i) for i in row]))
