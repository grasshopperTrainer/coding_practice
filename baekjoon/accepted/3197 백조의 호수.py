from sys import stdin
from collections import deque


def ds_get_root(ds, idx):
    if ds[idx] == idx:
        return idx
    root = ds_get_root(ds, ds[idx])
    ds[idx] = root
    return root


def ds_union(ds, a, b):
    roots = ds_get_root(ds, a), ds_get_root(ds, b)
    if roots[0] == roots[1]:
        return
    depths = ds_depth(ds, a, 0), ds_depth(ds, b, 0)
    if depths[0] < depths[1]:
        ds[a] = b
    else:
        ds[b] = a


def ds_depth(ds, idx, count):
    if ds[idx] == idx:
        return count
    return ds_depth(ds, ds[idx], count + 1)


def solution(R, C, board):
    SWAN, ICE, WATER = 'L', 'X', '.'
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)

    # init
    edges = []
    swans = []
    region_cnt = 0
    for ox in range(R):
        for oy in range(C):
            if board[ox][oy] not in (WATER, SWAN):
                continue

            sign = region_cnt
            que = deque([(ox, oy)])
            while que:
                x, y = que.popleft()
                if board[x][y] == SWAN:
                    swans.append(sign)
                board[x][y] = sign

                for dx, dy in DELTA:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C:
                        if board[nx][ny] in (WATER, SWAN):
                            que.append((nx, ny))
                        elif board[nx][ny] == ICE:
                            edges.append((nx, ny, sign))
            region_cnt += 1

    ds = [i for i in range(region_cnt)]

    # simulate
    days = 0
    while True:
        # for row in board:
        #     print(row)
        # print(ds, swans)
        # print()
        if ds_get_root(ds, swans[0]) == ds_get_root(ds, swans[1]):
            break

        # melt ice
        new_edges = []
        for x, y, sign in edges:
            if board[x][y] != ICE:
                ds_union(ds, board[x][y], sign)
                continue
            board[x][y] = sign

            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != sign:
                    if board[nx][ny] == ICE:
                        new_edges.append((nx, ny, sign))
                    else:
                        ds_union(ds, board[nx][ny], sign)
        edges = new_edges

        days += 1
    return days


R, C = tuple(map(int, stdin.readline().strip().split(' ')))
board = [list(stdin.readline().strip()) for _ in range(R)]

print(solution(R, C, board))

"""
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXXLXXX....
"""
"""
5 5
XXLXX
XX.XX
..X..
XX.XX
XXLXX
"""
"""
5 5
LXXXX
XXXXX
XXXXX
XXXXX
XXXXL
"""

"""
5 5
XXXXX
XLXXX
XXXXX
XXXXX
XXXXL
"""

"""
5 5
LXX..
.XXX.
.XXX.
.XXX.
.XXXL
"""

"""
5 5
LX.X.
X.X.X
.X.X.
X.X.X
.X.XL
"""