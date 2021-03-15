from sys import stdin
from math import inf


def solution(N, M, W, roads, warmholes):
    graph = {}
    for s, e, t in roads:
        s, e = s - 1, e - 1
        graph.setdefault(s, []).append((e, t))
        graph.setdefault(e, []).append((s, t))
    for s, e, t in warmholes:
        s, e = s - 1, e - 1
        t = -t
        graph.setdefault(s, []).append((e, t))

    visited = [False]*N
    for origin in [2]:
        if visited[origin]:
            continue
        visited[origin] = True

        costs = [inf]*N
        costs[origin] = 0
        for _ in range(N-1):
            for at in graph:
                for goto, cost in graph.get(at, []):
                    if costs[at] + cost < costs[goto]:
                        visited[goto] = True
                        costs[goto] = costs[at] + cost
            print(_, costs)
        # check
        for at in graph:
            for goto, cost in graph[at]:
                if costs[at] + cost < costs[goto]:
                    return 'YES'
        print(origin, costs)
    return 'NO'


lexer = lambda: list(map(int, stdin.readline().strip().split(' ')))
for _ in range(int(stdin.readline())):
    N, M, W = lexer()
    roads = [lexer() for _ in range(M)]
    warmholes = [lexer() for _ in range(W)]
    print(solution(N, M, W, roads, warmholes))

"""
1
5 4 0
1 2 2
2 3 1
3 4 4
4 5 2
"""
