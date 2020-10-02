from sys import stdin


def solution(N, M, board):
    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1))
    DELTA = {c: d for d, c in zip(DELTA, 'UDLR')}

    count = 0
    checked = [[False]*M for _ in range(N)]
    for n in range(N):
        for m in range(M):
            visited = set()
            x, y = n, m
            while True:
                if (x, y) in visited:
                    count += 1
                    break
                if checked[x][y]:
                    break
                visited.add((x, y))
                checked[x][y] = True
                dx, dy = DELTA[board[x][y]]
                x, y = x+dx, y+dy
    return count


N, M = [int(c) for c in stdin.readline().strip().split(' ')]
board = [stdin.readline().strip() for _ in range(N)]

print(solution(N, M, board))

"""
3 3
RRD
DRL
RRU
"""
"""
3 3
RRD
URD
ULL
"""
"""
3 3
RLL
UUU
UUU
"""
"""
3 3
RLL
RUL
RLU
"""
"""
2 3
DLD
UUU
"""
"""
1 4
RLRL
"""
"""
2 4
RLRL
URLU
"""