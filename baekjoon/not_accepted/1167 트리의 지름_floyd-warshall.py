# exceeding memory limit
from sys import stdin


def solution(N, routes):
    MAX = 10_000
    board = [[MAX]*N for _ in range(N)]
    for r in routes:
        row = board[r[0]-1]
        for i in range((len(r)-1)//2):  # dirst how can it be cleaner?
            dest, cost = r[i*2+1]-1, r[(i+1)*2]
            row[dest] = cost

    for m in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    board[i][j] = 0
                else:
                    t = board[i][m] + board[m][j]
                    if board[i][j] > t:
                        board[i][j] = t

    return max([max(row) for row in board])


N, routes = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        routes.append([int(c) for c in row.strip().split(' ')[:-1]])

print(solution(N, routes))