from sys import stdin
import heapq


def solution(N, graph):
    costs = [[float('inf')] * N for _ in range(N)]

    for i in range(N):
        for k in range(N):
            for j in range(N):
                # disable direct move
                # so min cost != graph value means without direct connection, min distance is unreachable
                if i == j or i == k or j == k:
                    continue

                t = graph[i][k] + graph[k][j]
                if t <= costs[i][j]:
                    costs[i][j] = t

    for row in costs:
        print(row)


N = int(stdin.readline())
graph = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

print(solution(N, graph))
