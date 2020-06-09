# tested speed and think last thing bothers is divisions of 'i//3' and 'i%3'
# it can be eliminated by using indexing of '0,0' not domain of '0, N'
from sys import stdin


def solution(N, board):
    VALS = '2', '0', '1'   # order as given by instruction and change -1 to 2 to make all chars singular

    def count(row_domain, col_domain, N):
        if N == 1:
            return board[row_domain[0]][col_domain[0]]

        results = []
        is_singular = True
        third_domain_len = N//3
        for i in range(9):
            row_part = row_domain[0] + third_domain_len*(i//3), row_domain[0] + third_domain_len*(i//3+1)
            col_part = col_domain[0] + third_domain_len*(i%3), col_domain[0] + third_domain_len*(i%3+1)
            result = count(row_part, col_part, third_domain_len)

            if not results:
                results.append(result)
            else:
                if len(result) != 1 or results[-1] != result:
                    is_singular = False
                results.append(result)

        if is_singular:
            return results[0]
        return ''.join(results)

    answer = count((0, N), (0, N), N)
    return [answer.count(v) for v in VALS]


N = int(stdin.readline())
board = [stdin.readline().replace('-1', '2').replace(' ', '').strip() for _ in range(N)]

for a in solution(N, board):
    print(a)
