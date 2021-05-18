from sys import stdin
from collections import deque


def solution(N, M, coords):
    N, M = N + 1, M + 1  # !critical
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)

    def search(a, b, others):
        # find min path
        total_count = 0
        board = [[float('inf')] * M for _ in range(N)]
        board[a[0]][a[1]] = 0
        moves = deque([(0, *a)])
        while moves:
            c, x, y = moves.popleft()
            if (x, y) == b:
                break

            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == float('inf') and (nx, ny) not in others:
                    board[nx][ny] = c + 1
                    moves.append((c + 1, nx, ny))
        if board[b[0]][b[1]] == float('inf'):  # check reachability
            return float('inf')
        total_count += board[b[0]][b[1]]

        # reconstruct path
        MARK = -1
        at = b
        while board[at[0]][at[1]] != 0:
            x, y = at
            count = board[x][y]
            board[x][y] = MARK
            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == count - 1:
                    at = nx, ny
                    break
        board[a[0]][a[1]] = MARK

        # find min path others
        a, b = others
        moves = deque([(0, *a)])
        while moves:
            c, x, y = moves.popleft()
            if (x, y) == b:
                total_count += c
                break

            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != MARK:
                    board[nx][ny] = MARK
                    moves.append((c + 1, nx, ny))
        if board[b[0]][b[1]] == MARK:  # check reachability
            return total_count
        return float('inf')

    # find best
    answer = min(search(*coords[:2], coords[2:]), search(*coords[2:], coords[:2]))
    if answer == float('inf'):
        return 'IMPOSSIBLE'
    return answer


parser = lambda: stdin.readline().strip().split(' ')
N, M = map(int, parser())
coords = [tuple(map(int, parser())) for _ in range(4)]

print(solution(N, M, coords))

"""
100 100
80 12
55 94
99 50
45 61
"""
"""
2 2
0 0
1 1
0 1
1 0
"""
"""
2 2
0 0
1 0
0 1
1 1
"""
