from sys import stdin
from collections import deque
from itertools import product
from copy import deepcopy


def solution(N, M, board):
    DIVIDER = 10
    DELTA = ((-1, 0), (1, 0), (0, -1), (0, 1))
    SPACE, WALL = 0, 1

    answer = deepcopy(board)
    checked = [[False] * M for _ in range(N)]
    for x, y in product(range(N), range(M)):
        if board[x][y] == WALL:
            continue
        if checked[x][y]:
            continue

        que = deque([(x, y)])
        visited = {(x, y)}
        walls = set()
        while que:
            x, y = que.popleft()
            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if board[nx][ny] == WALL:
                        walls.add((nx, ny))
                    elif (nx, ny) not in visited:
                        visited.add((nx, ny))
                        que.append((nx, ny))
                        checked[nx][ny] = True
        count = len(visited)
        for n, m in walls:
            answer[n][m] += count

    for x, y in product(range(N), range(M)):
        answer[x][y] %= DIVIDER
    return answer


N, M = [int(c) for c in stdin.readline().strip().split(' ')]
board = [[int(c) for c in stdin.readline().strip()] for _ in range(N)]
for row in solution(N, M, board):
    print(''.join([str(i) for i in row]))
