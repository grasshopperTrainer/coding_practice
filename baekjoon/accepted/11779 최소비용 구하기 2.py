from sys import stdin
import heapq


def solution(N, M, buses, cities):
    A, B = cities
    graph = [[float('inf')]*(N+1) for _ in range(N+1)]
    for a, b, c in buses:
        graph[a][b] = min(graph[a][b], c)

    min_cost = None
    record = [float('inf')] * (N + 1)
    moves = [(0, A)]
    while moves:
        cost, at = heapq.heappop(moves)
        if record[at] <= cost:
            continue
        record[at] = cost

        if at == B:
            min_cost = cost
            break

        for goto, new_cost in enumerate(graph[at]):
            if goto != at and cost + new_cost < record[goto]:
                heapq.heappush(moves, (cost + new_cost, goto))

    path = []
    at = B
    while not path or at != A:
        path.append(at)
        for comefrom, cost in enumerate(graph[i][at] for i in range(N+1)):
            if record[comefrom] + cost == record[at]:
                at = comefrom
                break
    path.append(A)
    path.reverse()

    print(min_cost)
    print(len(path))
    print(' '.join(map(str, path)))


N = int(stdin.readline())
M = int(stdin.readline())
buses = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(M)]
cities = tuple(map(int, stdin.readline().strip().split(' ')))
solution(N, M, buses, cities)

"""
3
3
1 3 3
3 2 3
2 1 3
1 1
"""