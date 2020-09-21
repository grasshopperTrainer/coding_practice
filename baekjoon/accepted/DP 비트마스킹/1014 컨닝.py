from sys import stdin


def solution(N, M, board):
    # into bit mask(reversed)
    board = [int(''.join(reversed(row.replace('.', '0').replace('x', '1'))), 2) for row in board]

    PATT_LEN = 2**M
    dp = [[0]*PATT_LEN for _ in range(N+1)]         # idx 0 is for initiation
    for x in range(1, N+1):                         # for all row
        row = board[x-1]
        for p in range(PATT_LEN):                   # check all possible patterns
            if '11' in bin(p) or row & p:           # can't seat adjacent and can't seat on broken
                continue
            upper_adjacency = p << 1 | p >> 1       # upper adjacency mask
            for i in range(PATT_LEN):               # check all pattern of upper row
                if upper_adjacency & i:             # check upper pattern
                    continue
                dp[x][p] = max(dp[x][p], dp[x-1][i] + bin(p).count('1'))
    return max(dp[-1])


for _ in range(int(stdin.readline())):
    N, M = [int(c) for c in stdin.readline().strip().split(' ')]
    board = []
    for _ in range(N):
        board.append(stdin.readline().strip())
    print(solution(N, M, board))

"""
1
3 3
...
xx.
...
"""
"""
1
1 1
.
"""
"""
1
2 2
..
..
"""
"""
1
2 3
..x
.x.
"""
"""
1
3 3
x.x
x.x
.x.
"""
"""
1
2 3
...
...

1
2 3
x.x
xxx

1
2 3
x.x
x.x

1
10 10
....x.....
..........
..........
..x.......
..........
x...x.x...
.........x
...x......
........x.
.x...x....
"""