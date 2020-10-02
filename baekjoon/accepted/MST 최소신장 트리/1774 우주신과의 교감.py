from sys import stdin
from math import sqrt
import heapq


def solution(N, coords, built):
    dists = [[float('inf')]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            d = sqrt((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2)
            dists[i][j] = dists[j][i] = d

    for a, b in map(lambda x: (x[0]-1, x[1]-1), built):
        dists[a][b] = dists[b][a] = 0.

    ROOT = 0
    sum_dist = 0
    visited = {ROOT}
    heap = [(cost, goto) for goto, cost in enumerate(dists[ROOT])] # cost, at
    heapq.heapify(heap)
    while heap:
        cost, at = heapq.heappop(heap)
        if at in visited:
            continue
        visited.add(at)
        sum_dist += cost
        for goto, gocost in enumerate(dists[at]):
            heapq.heappush(heap, (gocost, goto))

    # first thought was that no sum_dist can't be integer as all dists[i][j] is float
    # yet for example if all connection is already built all dists[i][j] is int 0
    # resulting following code incompatible

    # stred = str(sum_dist)
    # stred = stred[:stred.find('.')+3]
    # if len(stred)-2 == stred.find('.'):
    #     stred += '0'
    return format(sum_dist,".2f")


lexer = lambda : [int(c) for c in stdin.readline().strip().split(' ')]
N, M = lexer()
coords = [lexer() for _ in range(N)]
built = [lexer() for _ in range(M)]
print(solution(N, coords, built))

"""
3 0
1 1
1 2
2 1
"""
"""
4 1
1 1
4 1
2 3
4 3
1 1
"""