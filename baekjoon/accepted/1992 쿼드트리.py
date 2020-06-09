from sys import stdin
from itertools import product


def solution(N, board):

    def domain_length(domain):
        return domain[1] - domain[0]

    def color_check(row_domain, col_domain):
        ref_color = board[row_domain[0]][col_domain[0]]
        for x, y in product(range(*row_domain), range(*col_domain)):
            if board[x][y] != ref_color:
                return False
        return ref_color

    def compress(row_domain, col_domain):
        is_mono = color_check(row_domain, col_domain)
        if is_mono:
            return is_mono

        string = '('
        half_row_len, half_col_len = domain_length(row_domain)//2, domain_length(col_domain)//2
        for i in range(4):
            # check how output should be ordered and decide placing 'i//2', 'i%2'
            row_part = row_domain[0] + half_row_len*(i//2), row_domain[0] + half_row_len*(i//2+1)
            col_part = col_domain[0] + half_col_len*(i%2), col_domain[0] + half_col_len*(i%2+1)
            string += compress(row_part, col_part)
        return string + ')'

    return compress((0, N), (0, N))


N = int(stdin.readline())
board = [list(stdin.readline().strip()) for _ in range(N)]

print(solution(N, board))
