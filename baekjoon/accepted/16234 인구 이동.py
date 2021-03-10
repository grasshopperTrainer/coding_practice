from sys import stdin
from collections import deque


def solution(N, L, R, board):
    DELTA = (0, 1), (0, -1), (-1, 0), (1, 0)

    run_count = 0
    while True:
        new_runs = False
        checked = [[False]*N for _ in range(N)]
        for sx in range(N):
            for sy in range(N):
                if checked[sx][sy]:
                    continue
                checked[sx][sy] = True
                # do dfs
                summed_v = 0
                visited = {(sx, sy)}
                que = deque([(sx, sy)])
                while que:
                    x, y = que.popleft()
                    summed_v += board[x][y]
                    for dx, dy in DELTA:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if (nx, ny) not in visited and not checked[nx][ny] and L <= abs(board[x][y] - board[nx][ny]) <= R:
                                visited.add((nx, ny))
                                checked[nx][ny] = True
                                que.append((nx, ny))

                if 1 < len(visited):
                    new_runs = True
                    ave_val = summed_v//len(visited)
                    for i, j in visited:
                        board[i][j] = ave_val
                    # for row in board:
                    #     print(row)
                    # print()
        if new_runs:
            run_count += 1
        else:
            break
    return run_count


lexer = lambda : [int(c) for c in stdin.readline().strip().split(' ')]
N, L, R = lexer()
board = [lexer() for _ in range(N)]

print(solution(N, L, R, board))

"""
3 1 100
1 1 1
1 2 1
2 2 1
"""