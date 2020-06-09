# Python 3 timeover
from sys import stdin


def solution(N, board):
    VALS = '-1', '0', '1'   # order as given by instruction

    def domain_length(domain):
        return domain[1] - domain[0]

    def check_values(row_domain, col_domain):
        # gradual conditioning saves some time
        ref_value = board[row_domain[0]][col_domain[0]]
        ref_row = board[row_domain[0]][col_domain[0]:col_domain[1]]
        for v in ref_row:
            if v != ref_value:
                return False

        for x in range(*row_domain):
            if board[x][col_domain[0]:col_domain[1]] != ref_row:
                return False
        # !KILLER CASE! without casting into 'int' answer can be series of 'bool's thus violating output format
        return [int(ref_value == v) for v in VALS]

    def count(row_domain, col_domain):
        is_mono_value = check_values(row_domain, col_domain)
        if is_mono_value:
            return is_mono_value

        counts = 0, 0, 0
        third_domain_len = domain_length(row_domain)//3

        for i in range(9):
            row_part = row_domain[0] + third_domain_len*(i//3), row_domain[0] + third_domain_len*(i//3+1)
            col_part = col_domain[0] + third_domain_len*(i%3), col_domain[0] + third_domain_len*(i%3+1)
            counts = list(map(lambda x, y: x+y, counts, count(row_part, col_part)))
        return counts

    return count((0, N), (0, N))


N = int(stdin.readline())
board = [stdin.readline().strip().split(' ') for _ in range(N)]

for a in solution(N, board):
    print(a)

"""
3
0 0 0
0 0 0
0 0 0
"""
