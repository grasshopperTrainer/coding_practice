from sys import stdin
from math import inf, isinf


def solution(N, board, status, P):
    MASK = (1 << N) - 1
    alive = set()
    for i, c in enumerate(status):
        if c == 'Y':
            alive.add(i)
    status = int(''.join(reversed(status.replace('Y', '1').replace('N', '0'))), 2)

    if P <= len(alive):
        return 0
    if not alive:
        return -1

    dp = {}

    def search(cost, status):
        if status in dp:
            return cost + dp[status]

        if len(alive) == P:
            return cost

        min_cost = inf
        for d in range(N):
            if d not in alive:
                c = min([board[a][d] for a in alive])
                alive.add(d)
                status |= 1 << d
                min_cost = min(min_cost, cost + search(c, status))
                status &= MASK ^ (1 << d)
                alive.remove(d)
        dp[status] = min_cost - cost
        return min_cost

    r = search(0, status)
    return -1 if isinf(r) else r


N = int(stdin.readline())
board = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]
status = stdin.readline().strip()
P = int(stdin.readline())

print(solution(N, board, status, P))

"""
3
0 10 11
10 0 12
12 13 0
YNN
0
"""

"""
3
0 10 11
10 0 12
12 13 0
NNN
3
"""

"""
1
0
N
0
"""
