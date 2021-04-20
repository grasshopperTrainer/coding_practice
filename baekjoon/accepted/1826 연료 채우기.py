from sys import stdin
import heapq


def solution(N, stations, L, P):
    stations.sort(reverse=True)
    heap = []
    count = 0
    while P < L:
        while stations and stations[-1][0] <= P:
            dist, fuel = stations.pop()
            heapq.heappush(heap, -fuel)

        if not heap:
            break
        P -= heapq.heappop(heap)
        count += 1

    if L <= P:
        return count
    return -1


N = int(stdin.readline())
stations = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]
L, P = map(int, stdin.readline().strip().split(' '))

print(solution(N, stations, L, P))

"""
1
1 1
15 13
"""
"""
1
1 2
5 4
10 z
"""
"""
3
4 1
5 1
8 1
10 7
"""
"""
2
5 7
12 1
10 5
"""
"""
2
2 3
4 7
14 4
"""