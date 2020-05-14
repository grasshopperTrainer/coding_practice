from sys import stdin
from itertools import product
from collections import deque


def solution(M, N, cabbages):
    EMPTY, CABBAGE = 0, 'C'
    DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    field = [[EMPTY]*M for _ in range(N)]
    for y, x in cabbages:
        field[x][y] = CABBAGE

    def bfs(x, y, field, mark):
        field[x][y] = mark
        que = deque([(x,y)])
        while que:
            x, y = que.popleft()
            for dx, dy in DELTAS:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == CABBAGE:
                    field[nx][ny] = mark
                    que.append((nx, ny))

    count = 0
    for x, y in product(range(N), range(M)):
        if field[x][y] != CABBAGE:
            continue

        count += 1
        bfs(x, y, field, count)

    return count


T, M, N, K, cabbages = 0, 0, 0, 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        T = int(row)
        continue
    if K == 0:
        M, N, K = [int(c) for c in row.strip().split(' ')]
        cabbages = []
    else:
        cabbages.append([int(c) for c in row.strip().split(' ')])
        K -= 1
        if K == 0:
            print(solution(M, N, cabbages))