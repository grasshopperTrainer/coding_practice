from sys import stdin
import heapq


def solution(N, M, orders):
    graph, rev_graph = {}, {}
    for f, s in orders:
        graph[s] = f
        if s < f:
            rev_graph.setdefault(f, []).append(s)

    answer = []
    picked = [False] * (N + 1)
    heap = [(i, i) for i in range(1, N+1)]
    while heap:
        o, n = heapq.heappop(heap)
        if n in graph and not picked[graph[n]]:
            pass
        else:
            if n in rev_graph:
                
            answer.append(n)
            picked[n] = True

    return answer



N, M = map(int, stdin.readline().strip().split(' '))
orders = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(M)]

print(' '.join(map(str, solution(N, M, orders))))

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