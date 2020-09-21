from sys import stdin, setrecursionlimit

setrecursionlimit(10_100)


def solution(N, populations, edges):
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    ROOT = 1
    visited = [False]*(N+1)
    def dfs(at):
        visited[at] = True
        selected_pop = populations[at-1]
        rejected_pop = 0

        for child in graph[at]:
            if not visited[child]:
                r = dfs(child)
                selected_pop += r[1]
                rejected_pop += max(r)
        print(at, selected_pop, rejected_pop)
        return selected_pop, rejected_pop
    return max(dfs(ROOT))


N = int(stdin.readline())
populations = [int(c) for c in stdin.readline().strip().split(' ')]
edges = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N-1)]

print(solution(N, populations, edges))


"""
3
1 20 10
1 2
2 3
"""