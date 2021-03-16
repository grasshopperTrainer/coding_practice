from sys import stdin


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

    essencials = []
    for i in range(N):
        for j in range(i + 1, N):
            if costs[i][j] > graph[i][j]:
                essencials.append(graph[i][j])
            elif costs[i][j] < graph[i][j]:
                return -1
    
    if not essencials:
        return -1
    return sum(essencials)


N = int(stdin.readline())
graph = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

print(solution(N, graph))

"""
3
0 1 2
1 0 1
2 1 0
"""
"""
3
0 1 1
1 0 1
1 1 0
"""