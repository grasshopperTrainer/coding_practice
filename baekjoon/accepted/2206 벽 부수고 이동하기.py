from sys import stdin
from collections import deque
from itertools import product


def solution(N, M, chart):
    EMPTY, WALL, THROUGH = -1, 0, 1
    NORECORD = -1
    DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for x, y in product(range(N), range(M)):
        if chart[x][y] == 1:
            chart[x][y] = WALL, NORECORD
        else:
            chart[x][y] = EMPTY, NORECORD
    chart[0][0] = EMPTY, 1

    def in_range(x, y):
        return True if 0 <= x < N and 0 <= y < M else False

    que = deque([(0,0)])
    while que:
        x, y = que.popleft()
        current_s, current_v = chart[x][y]
        for dx, dy in DELTAS:
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                next_s, next_v = chart[nx][ny]
                if next_v != NORECORD:
                    if current_s == EMPTY and next_s == THROUGH:
                        chart[nx][ny] = EMPTY, current_v + 1
                        que.append((nx, ny))
                else:
                    if current_s == EMPTY and next_s in (EMPTY, WALL):
                        chart[nx][ny] = next_s, current_v + 1
                        que.append((nx, ny))
                    if current_s in (THROUGH, WALL) and next_s == EMPTY:
                        chart[nx][ny] = THROUGH, current_v + 1
                        que.append((nx, ny))

        if chart[N-1][M-1][1] != -1:
            break

    for row in chart:
        print(row)
    print()

    return chart[N-1][M-1][1]


N, M, chart = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N, M = [int(c) for c in row.strip().split(' ')]
    else:
        chart.append([int(c) for c in row.strip()])

print(solution(N, M, chart))

"""
5 5
00000
11101
00000
11111
00010
"""
"""
6 5
00000
11101
00000
11111
01111
00000
"""
"""
6 6
001000
101010
000010
111100
010111
000000
"""
"""
6 6
000000
111110
000000
011111
000000
000000
"""
"""
7 5
00000
11101
00001
01111
01111
11111
00000
"""

"""
3 3
001
111
100
"""
"""
3 3
001
001
010
"""
"""
3 4
0111
1011
1100
"""