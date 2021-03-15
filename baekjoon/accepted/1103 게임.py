from sys import stdin, setrecursionlimit
from math import inf, isinf

HOLE = 0

setrecursionlimit(2000)
def solution(N, M, board):
    D = ((-1, 0), (0, -1), (1, 0), (0, 1))
    dp = [[None] * M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True
    def search(x, y, count):
        if dp[x][y] is not None:
            return count + dp[x][y]
        if board[x][y] == HOLE:
            return count
        else:
            amp = board[x][y]
            max_count = count + 1 # ! +1 getting out is also one move
            for dx, dy in D:
                nx, ny = dx * amp + x, dy * amp + y
                if 0 <= nx < N and 0 <= ny < M:
                    if visited[nx][ny]:
                        max_count = inf
                        break
                    visited[nx][ny] = True
                    max_count = max(max_count, search(nx, ny, count + 1))
                    visited[nx][ny] = False

            dp[x][y] = max_count - count
            return max_count

    r = search(0, 0, 0)
    return -1 if isinf(r) else r


N, M = list(map(int, stdin.readline().strip().split(' ')))
board = []
for _ in range(N):
    vs = []
    for c in stdin.readline().strip():
        if c.isnumeric():
            vs.append(int(c))
        else:
            vs.append(HOLE)
    board.append(vs)

print(solution(N, M, board))
