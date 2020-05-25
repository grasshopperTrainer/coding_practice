# time over
from sys import stdin


def solution(R, C, K, tiles):
    pos = [-1] + [(r-1)*C+c-1 for r, c in tiles] + [R*C]

    full_n_tiles, full_n_ways = C//2, 1 if C%2 == 0 else (C//2+1)%1_000_000_007
    num_tiles, num_ways = 0, 1
    for start, end in zip(pos[:-1], pos[1:]):
        if end - start - 1 == 0:
            continue
        front_group, end_group = start//C+1, end//C
        front_gap, end_gap = front_group*C - start-1, end - end_group*C
        num_tiles += full_n_tiles*(end_group - front_group)
        for _ in range(end_group - front_group + 1):
            num_ways = (num_ways*full_n_ways)%1_000_000_007

        num_tiles += front_gap//2
        if front_gap%2 == 1:
            num_ways = (num_ways*front_gap//2+1)%1_000_000_007
        num_tiles += end_gap//2
        if end_gap%2 == 1:
            num_ways = (num_ways*end_gap//2+1)%1_000_000_007
    if num_tiles == 0:
        num_ways = 0
    return num_tiles, num_ways


# R, C, K, tiles = 0, 0, 0, []
# for i, row in enumerate(stdin.readlines()):
#     row = [int(c) for c in row.strip().split(' ')]
#     if i == 0:
#         R, C, K = row
#     else:
#         tiles.append(row)

import random
import time

while True:
    R, C = random.randint(1, 1_000_000_000), random.randint(1, 1_000_000_000)
    K = random.randint(0, 1000)
    tiles = {}
    made = set()
    for i in range(K):
        while True:
            x, y = random.randint(1, R), random.randint(1, C)
            if (x,y) not in made:
                made.add((x,y))
                tiles.setdefault(x, []).append(y)
                break

    for k, v in tiles.items():
        v.sort()
    sorted_tiles = sorted(tiles.items(), key=lambda x:x[0])

    tiles = []
    for i in sorted_tiles:
        for j in i[1]:
            tiles.append((i[0],j))

    print('input size',R,C,K)
    s = time.time()
    print(' '.join([str(i) for i in solution(R, C, K, tiles)]))
    e = time.time()

    if e-s >= 2:
        print('too long', R, C, K, e-s)
        raise
    else:
        print(e-s)

"""
2 2 4
1 1
1 2
2 1
2 2
"""

"""
4 5 6
1 2
1 3
3 1
4 3
"""
"""
4 5 6
1 2
1 3
4 3
4 4
4 5
"""
"""
4 4 0

"""