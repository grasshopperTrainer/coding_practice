from sys import stdin
from itertools import product


def solution(N, M, board):
    def rotate(mat):
        n, m = len(mat), len(mat[0])
        new_mat = [[0] * n for _ in range(m)]
        for x, row in enumerate(mat):
            for y, val in enumerate(row):
                new_mat[y][n - 1 - x] = val
        return new_mat

    def mirror(mat):
        return [row[::-1] for row in mat]

    TETROMINOS = ([(1, 1, 1, 1)],
                  [(1, 1), (1, 1)],
                  [(1, 1, 1), (1, 0, 0)],
                  [(0, 1, 1), (1, 1, 0)],
                  [(1, 1, 1), (0, 1, 0)])
    INST = ((1, 2), (1, 1), (2, 4), (2, 2), (1, 4))  # typs mirror, typs rotation

    score_high = 0
    for tetro, (mir_n, rot_n) in zip(TETROMINOS, INST):

        for do_mirror in range(mir_n):
            if do_mirror:  # mirror
                tetro = mirror(tetro)

            for do_rotate in range(rot_n):
                if do_rotate:  # rotate
                    tetro = rotate(tetro)

                # search
                n, m = len(tetro), len(tetro[0])
                for dx, dy in product(range(N - n + 1), range(M - m + 1)):
                    score = 0
                    for x, y in product(range(n), range(m)):
                        if tetro[x][y]:
                            score += board[x + dx][y + dy]
                    score_high = max([score_high, score])

    return score_high


N, M, board = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N, M = map(int, row.strip().split(' '))
        continue
    board.append(list(map(int, row.strip().split(' '))))

print(solution(N, M, board))
