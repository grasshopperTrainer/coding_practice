# time out
from sys import stdin
from collections import deque


def solution(N, edges, queries):
    graph = {}
    for a, b, cost in edges:
        graph.setdefault(a, []).append((b, cost))
        graph.setdefault(b, []).append((a, cost))

    depths = [0] * (N + 1)

    root = 1
    tree = [[(i, None), []] for i in range(N + 1)]  # [(parent, cost), [children]]
    tree[1][0] = (1, 0)

    visited = [False] * (N + 1)
    visited[1] = True
    que = deque([(0, root)])
    while que:
        h, par = que.popleft()
        for child, cost in graph[par]:
            if not visited[child]:
                visited[child] = True
                depths[child] = h + 1
                tree[par][1].append(child)
                tree[child][0] = par, cost
                que.append((h + 1, child))

    # draw lca
    max_ancestors = len(bin(N - 2)[2:]) + 1
    costs = [[0] * max_ancestors for _ in range(N + 1)]  # parent, cost
    ancestors = [[root] * max_ancestors for _ in range(N + 1)]  # parent, cost

    for i in range(1, N + 1):
        ancestors[i][0] = tree[i][0][0]
        costs[i][0] = tree[i][0][1]
    for i in range(1, N + 1):
        for j in range(1, max_ancestors):
            ancestors[i][j] = ancestors[ancestors[i][j - 1]][j - 1]
            costs[i][j] = costs[i][j - 1] + costs[ancestors[i][j - 1]][j - 1]

    def search_lca_cost(anc, costs, depths, a, b):
        cost = 0
        while depths[a] != depths[b]:
            if depths[a] < depths[b]:
                offset = 0
                while depths[anc[b][offset + 1]] > depths[a]:
                    offset += 1
                cost += costs[b][offset]
                b = anc[b][offset]
            else:
                offset = 0
                while depths[anc[a][offset + 1]] > depths[b]:
                    offset += 1
                cost += costs[a][offset]
                a = anc[a][offset]
        if a != b:
            while anc[a][0] != anc[b][0]:
                offset = 0
                while anc[a][offset + 1] != anc[b][offset + 1]:
                    offset += 1
                cost += costs[a][offset] + costs[b][offset]
                a, b = anc[a][offset], anc[b][offset]
            cost += costs[a][0] + costs[b][0]
        return cost

    def search_nth_node(anc, depths, oa, ob, n):
        a, b = oa, ob
        while depths[a] != depths[b]:
            if depths[a] < depths[b]:
                offset = 0
                while depths[anc[b][offset + 1]] > depths[a]:
                    offset += 1
                b = anc[b][offset]
            else:
                offset = 0
                while depths[anc[a][offset + 1]] > depths[b]:
                    offset += 1
                a = anc[a][offset]
        if a != b:
            while anc[a][0] != anc[b][0]:
                offset = 0
                while anc[a][offset + 1] != anc[b][offset + 1]:
                    offset += 1
                a, b = anc[a][offset], anc[b][offset]
            a, b = anc[a][0], anc[b][0]
        # a is lca

        # on which side?
        sdepth = depths[oa] - depths[a] + 1
        edepth = depths[ob] - depths[a] + 1
        if n == sdepth:
            return a
        elif n < sdepth:  # on starting side
            x = oa
        else:  # on ending side
            n = edepth - (n - sdepth)
            x = ob

        while n != 1:
            offset = 0
            while True:
                if 0 < n - 2 ** offset:
                    offset += 1
                else:
                    offset -= 1
                    break
            n -= 2 ** offset
            x = anc[x][offset]
        return x

    for tokens in queries:
        if tokens[0] == 1:
            _, a, b = tokens
            print(search_lca_cost(ancestors, costs, depths, a, b))
        else:
            _, a, b, n = tokens
            print(search_nth_node(ancestors, depths, a, b, n))


N = int(stdin.readline())
edges = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(N - 1)]
queries = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(int(stdin.readline()))]

solution(N, edges, queries)

"""
10
1 2 1
2 3 1
3 4 1
4 5 1
5 6 1
6 7 1
7 8 1
8 9 1
9 10 1
2
1 1 10
2 1 10 3
"""

"""
6
1 2 1
2 4 1
2 5 2
1 3 1
3 6 2
1
2 6 6 1
"""
"""
6
1 2 1
2 4 1
2 5 2
1 3 1
3 6 2
1
1 4 6
"""
"""
2
1 2 10
5
1 1 2
2 1 2 1
2 2 1 1
2 1 2 2
2 2 1 2
"""
"""
6
1 2 2
1 3 3
2 4 4
5 4 5
4 6 6
7
1 1 4
1 3 5
1 2 4
1 5 3
1 6 3
2 3 5 2
2 1 4 2
2 3 5 3
"""
"""
6
1 2 1
2 4 1
2 5 2
1 3 1
3 6 2
2
1 1 1
2 1 1 1
"""
"""
5
1 2 1
3 4 1
5 2 1
5 4 1
0
"""
