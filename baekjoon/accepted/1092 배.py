# not good

from sys import stdin
from math import ceil


def solution(N, cranes, M, boxes):
    cranes.sort()
    boxes.sort()

    if cranes[-1] < boxes[-1]:
        return -1

    # allocate boxes
    best = ceil((len(boxes)+1)/N)
    works = [0]*N
    cid = 0
    for i, box in enumerate(boxes):
        print(works)
        if box <= cranes[cid] and works[cid] < best:
            works[cid] += 1
        elif cid < N-1:
            cid += 1
            works[cid] += 1
        else:
            works[-1] += M - i
            break
    return max(works)


N = int(stdin.readline())
cranes = list(map(int, stdin.readline().strip().split(' ')))
M = int(stdin.readline())
boxes = list(map(int, stdin.readline().strip().split(' ')))
print(solution(N, cranes, M, boxes))

"""
3
6 8 9
6
8 8 8 9 9 9
"""
"""
3
6 8 10
6
6
"""
"""
3
6 8 10
6
6 6 6 7 7 7
"""
"""
3
1 2 9
1
1 1 1 1 1 1 9
"""
"""
3
1 2 9
1
1 2 9 1 2 9 1 2
"""
"""
5
1 2 3 4 5
14
1 1 1 1 1 2 3 4 4 4 5 5 5 5
"""
"""
4
1 2 3 4
1
1 1 1 1 1 1 1 1 2 3 4 4
"""