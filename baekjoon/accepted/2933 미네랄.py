from sys import stdin
from collections import deque


def find_clusters(board, offset):
    R, C = len(board), len(board[0])
    EMPTY, ROCK = '.', 'x'
    clusters = []
    visited = [[False] * C for _ in range(R)]

    for ox in range(R):
        for oy in range(C):
            if visited[ox][oy] or board[ox][oy] == EMPTY:
                continue

            uid = len(clusters)
            coords = []
            que = deque([(ox, oy)])
            while que:
                x, y = que.popleft()
                coords.append((x, y))
                board[x][y] = uid

                for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != EMPTY and not visited[nx][ny]:
                        visited[nx][ny] = True
                        que.append((nx, ny))

            minx, miny = list(map(min, zip(*coords)))
            maxx, maxy = list(map(max, zip(*coords)))
            r, c = maxx - minx + 1, maxy - miny + 1
            cluster = [[EMPTY] * c for _ in range(r)]
            for x, y in coords:
                cluster[x - minx][y - miny] = ROCK
            clusters.append([(minx + offset[0], miny + offset[1]), (r, c), cluster])
    return clusters


def search_move_dist(board, cluster):
    EMPTY = '.'
    R = len(board)

    min_dist = float('inf')
    (ox, oy), (r, c), carta = cluster

    for y in range(c):
        for x in range(r - 1, -1, -1):
            if carta[x][y] != EMPTY:
                sx = ox + x + 1  # starting pos

                for ex in range(sx, R):
                    if board[ex][oy + y] != EMPTY:
                        break
                else:
                    ex = R
                min_dist = min(min_dist, ex - sx)

                break
    return min_dist


def move_cluster(board, cluster, dist):
    EMPTY, ROCK = '.', 'x'
    (ox, oy), (r, c), carta = cluster

    # erase
    for x in range(ox, ox + r):
        for y in range(oy, oy + c):
            if carta[x - ox][y - oy] != EMPTY:
                board[x][y] = EMPTY
    # mark
    for x in range(r):
        for y in range(c):
            if carta[x][y] != EMPTY:
                board[x + ox + dist][y + oy] = ROCK
    # offset cluster
    cluster[0] = cluster[0][0] + dist, cluster[0][1]


def solution(R, C, board, throws):
    EMPTY, ROCK = '.', 'x'

    for i, gx in enumerate(throws):
        gx = R - gx
        if i % 2 == 0:  # left -> right
            yrange = range(C)
        else:
            yrange = range(C - 1, -1, -1)

        # find clusters and mark
        clusters = find_clusters(board, (0, 0))
        # find closest intersecting cluster
        for oy in yrange:
            if board[gx][oy] != EMPTY:
                uid = board[gx][oy]
                board[gx][oy] = EMPTY
                (x, y), _, carta = clusters[uid]
                carta[gx - x][oy - y] = EMPTY
                sub_clusters = find_clusters(carta, (x, y))

                # descend block
                for cluster in sub_clusters:
                    dist = search_move_dist(board, cluster)
                    move_cluster(board, cluster, dist)
                break

        # for row in board:
        #     print(list(map(str, row)))
        # print()
    # format answer
    for i, row in enumerate(board):
        for j, v in enumerate(row):
            if v != EMPTY:
                row[j] = ROCK
        board[i] = ''.join(row)
    return board


R, C = list(map(int, stdin.readline().strip().split(' ')))
board = [list(stdin.readline().strip()) for _ in range(R)]
N = int(stdin.readline())
throws = tuple(map(int, stdin.readline().strip().split(' ')))

for row in solution(R, C, board, throws):
    print(row)

"""
8 8
........
........
...x.xx.
...xxx..
..xxx...
..x.xxx.
..x...x.
.xxx..x.
5
6 6 4 3 1
"""
"""
........
........
.....x..
...xxx..
...xx...
..x.xx..
..x...x.
.xxx..x.
"""
"""
........
........
........
........
.....x..
..xxxx..
..xxx.x.
..xxxxx.
"""
"""
3 3
xxx
.x.
xxx
1
1 2
"""
"""
3 3
xxx
xxx
xxx
13
1 1 1 1 3 3 3 1 1 1 1 1 1
"""
"""
4 3
xxx
.x.
xxx
..x
4
1 1 4 1
"""
"""
4 5
xxxxx
xxx..
x.xx.
...x.
4
2 4 2 1
"""
"""
xxxx.
xxx..
...x
...xx
"""
