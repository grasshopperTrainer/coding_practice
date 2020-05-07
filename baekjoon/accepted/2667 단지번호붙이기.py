from sys import stdin
from collections import deque
from itertools import product

def solution(N, chart):
    DELTA = ((0, 1), (1, 0), (0, -1), (-1, 0))
    EMPTY, HOUSE, MARKED = 0, 1, 'M'
    def bfs(x, y):
        chart[x][y] = MARKED    #
        count = 1               # island is also a cluster
        que, visited = deque([(x,y)]), {(x,y)}
        while que:
            x, y = que.popleft()
            for dx, dy in DELTA:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and chart[nx][ny] == HOUSE:
                    chart[nx][ny] = MARKED
                    count += 1
                    que.append((nx,ny))

        return count

    record = []
    for rn, cn in product(range(N), repeat=2):
        if chart[rn][cn] == HOUSE:
            record.append(bfs(rn, cn))

    return (len(record), *sorted(record))

N, chart = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        chart.append([int(c) for c in row.strip()])

for a in solution(N, chart):
    print(a)