from sys import stdin
import heapq


def solution(N, M, orders):
    count = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for a, b in orders:
        graph[a].append(b)
        count[b] += 1

    heap = []
    # find simply solvable
    for i in range(1, N+1):
        if count[i] == 0:
            heap.append(i)
    heapq.heapify(heap)

    answer = []
    while heap:
        x = heapq.heappop(heap)
        answer.append(x)
        for y in graph[x]:
            count[y] -= 1
            if count[y] == 0:
                heapq.heappush(heap, y)
    return ' '.join(map(str, answer))


N, M = map(int, stdin.readline().strip().split(' '))
orders = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(M)]

print(solution(N, M, orders))

"""
5 2
4 2
2 5
"""

"""
5 3
4 2
4 3
2 5
"""
"""
3 1
2 3
"""
"""
3 2
3 2
2 1
"""
"""
6 4
3 2
3 4
3 5
5 6
"""
"""
5 3
4 3
4 2
2 5
"""
"""
8 5
3 2
5 3
6 4
4 7
4 8
"""
"""
6 3
3 2
5 3
6 4
"""
