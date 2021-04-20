# memexeed

from sys import stdin, setrecursionlimit


setrecursionlimit(1_000_000)
def solution(N, edges):
    tree = [[] for _ in range(N+1)]
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    visited = [False]*(N+1)
    def search(at):
        visited[at] = True
        a, b = [1, 0]
        for child in tree[at]:
            if visited[child]:
                continue
            r = search(child)
            a += min(r)
            b += r[0]
        return a, b

    return min(search(1))


N = int(stdin.readline())
nodes = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N-1)]

print(solution(N, nodes))

"""
8
2 1
3 1
4 1
5 2
6 2
7 4
8 4
"""
"""
3
2 1
3 2
"""
"""
2
1 2
"""
"""
5
1 5
2 5
3 5
4 5
"""
"""
4
1 2
3 4
2 4
"""