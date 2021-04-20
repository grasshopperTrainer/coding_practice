from sys import stdin
import heapq


def solution(N, M, board):
    TRASH, NEAR, EMPTY = 'g', 'n', '.'

    D = ((-1, 0), (0, -1), (1, 0), (0, 1))
    # find start, finish
    start, finish = None, None
    for x in range(N):
        for y in range(M):
            if board[x][y] == 'S':
                start = (x, y)
            elif board[x][y] == 'F':
                finish = (x, y)
            elif board[x][y] == TRASH:
                for dx, dy in D:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == EMPTY:
                        board[nx][ny] = NEAR

    checked = [[False]*M for _ in range(N)]
    checked[start[0]][start[1]] = True
    heap = [(0, 0, *start)]
    while heap:
        a, b, x, y = heapq.heappop(heap)
        if (x, y) == finish:
            return a, b

        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not checked[nx][ny]:
                checked[nx][ny] = True  # x, y is already a best move so visiting from others not necessary
                if board[nx][ny] == TRASH:
                    heapq.heappush(heap, (a+1, b, nx, ny))
                elif board[nx][ny] == NEAR:
                    heapq.heappush(heap, (a, b+1, nx, ny))
                else:
                    heapq.heappush(heap, (a, b, nx, ny))


N, M = map(int, stdin.readline().strip().split(' '))
board = [list(stdin.readline().strip()) for _ in range(N)]

print(' '.join(map(str, solution(N, M, board))))

"""
4 1
F
g
g
S
"""
"""
4 4
F...
....
....
...S
"""