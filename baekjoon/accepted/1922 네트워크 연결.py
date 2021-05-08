from sys import stdin
import heapq


def solution(N, M, lines):
    graph = [[float('inf')] * N for _ in range(N)]
    for a, b, c in lines:
        a, b = a - 1, b - 1
        graph[a][b] = graph[b][a] = min(c, graph[a][b])

    picked = [False for _ in range(N)]
    picked[0] = True

    total_cost = 0
    lines = [(c, i) for i, c in enumerate(graph[0]) if i != 0 and c != float('inf')]
    heapq.heapify(lines)
    while lines:
        c, at = heapq.heappop(lines)
        if picked[at]:
            continue
        picked[at] = True
        total_cost += c
        for goto, cost in enumerate(graph[at]):
            if goto != at and cost != float('inf'):
                heapq.heappush(lines, (cost, goto))
    return total_cost


N = int(stdin.readline())
M = int(stdin.readline())
lines = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(M)]
print(solution(N, M, lines))
