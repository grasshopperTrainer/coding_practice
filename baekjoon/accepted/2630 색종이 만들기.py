from sys import stdin
from itertools import product


def solution(N, board):
    WHITE, BLUE = '0', '1'

    def color_check(row_bound, col_bound):
        # check whether block is mono colored
        rep_color = board[row_bound[0]][col_bound[0]]   # first color
        for x, y in product(range(*row_bound), range(*col_bound)):
            if board[x][y] != rep_color:
                return False
        # cause counting white and blue separately
        return rep_color == WHITE, rep_color == BLUE

    def search(row_bound, col_bound):
        is_mono = color_check(row_bound, col_bound)
        if is_mono: # if not False means its mono colored
            return is_mono

        # find mid index
        row_mid = row_bound[0] + (row_bound[1] - row_bound[0])//2
        col_mid = col_bound[0] + (col_bound[1] - col_bound[0])//2
        counts = [0, 0]
        for i in range(4):
            # selection of parts
            row_part = ((row_bound[0], row_mid), (row_mid, row_bound[1]))[i%2]
            col_part = ((col_bound[0], col_mid), (col_mid, col_bound[1]))[i//2]
            new_counts = search(row_part, col_part)
            # count white, blue separately
            counts = list(map(lambda x, y: x+y, counts, new_counts))

        return counts

    return search((0, N), (0, N))


N = int(stdin.readline())
board = []
for _ in range(N):
    board.append(stdin.readline().strip().split(' '))

for n in solution(N, board):
    print(n)
