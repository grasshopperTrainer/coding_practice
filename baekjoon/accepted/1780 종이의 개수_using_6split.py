# Python 3 timeover
from sys import stdin


def solution(N, board):
    VALS = '-1', '0', '1'   # order as given by instruction

    def domain_length(domain):
        return domain[1] - domain[0]

    def check_values(row_domain, col_domain):
        # for 2x2
        if domain_length(row_domain) == 2 and domain_length(col_domain) == 2:
            count = {v:0 for v in VALS}
            for x in range(*row_domain):
                for y in range(*col_domain):
                    count[board[x][y]] += 1
            return [count[v] for v in VALS]
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
        domain_len = domain_length(row_domain)
        if domain_len%2 == 0:
            half_domain_len = domain_len//2
            for i in range(4):
                row_part = row_domain[0] + half_domain_len*(i//2), row_domain[0] + half_domain_len*(i//2+1)
                col_part = col_domain[0] + half_domain_len*(i%2), col_domain[0] + half_domain_len*(i%2+1)
                counts = list(map(lambda x, y: x+y, counts, count(row_part, col_part)))
        else:
            third_domain_len = domain_len//3
            # five close-edge segments
            for i in (0, 1, 2, 3, 6):
                row_part = row_domain[0] + third_domain_len*(i//3), row_domain[0] + third_domain_len*(i//3+1)
                col_part = col_domain[0] + third_domain_len*(i%3), col_domain[0] + third_domain_len*(i%3+1)
                counts = list(map(lambda x, y: x+y, counts, count(row_part, col_part)))
            # sixth diagonal segment
            row_part = row_domain[0] + third_domain_len, row_domain[1]
            col_part = col_domain[0] + third_domain_len, col_domain[1]
            counts = list(map(lambda x, y: x+y, counts, count(row_part, col_part)))
        return counts

    return count((0, N), (0, N))


N = int(stdin.readline())
board = [stdin.readline().strip().split(' ') for _ in range(N)]

for a in solution(N, board):
    print(a)