from sys import stdin, setrecursionlimit

setrecursionlimit(1_000_100)


def solution(N, edges):
    # no tree
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # calc
    ROOT = 1
    visited = [False]*(N+1)
    # dp = [[0, 0] for _ in range(N+1)]   # i'm early adaptor, i'm not
    def dfs(at, im_early, im_not):
        visited[at] = True
        im_early += 1

        for child in graph[at]:
            if not visited[child]:
                r = dfs(child, 0, 0)
                im_early += min(r)
                im_not += r[0]
        return im_early, im_not

    return min(dfs(ROOT, 0, 0))


N = int(stdin.readline())
edges = []
for _ in range(N-1):
    edges.append([int(c) for c in stdin.readline().strip().split(' ')])
print(solution(N, edges))