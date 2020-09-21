from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(100100)


def solution(N, ROOT, edges, queries):
    nd_tree = {}
    for a, b in edges:
        nd_tree.setdefault(a, []).append(b)
        nd_tree.setdefault(b, []).append(a)

    tree = [[] for _ in range(N+1)]
    que, visited = deque([ROOT]), {ROOT}
    while que:
        at = que.popleft()
        for child in nd_tree[at]:
            if child not in visited:
                visited.add(child)
                tree[at].append(child)
                que.append(child)

    dp = [None for _ in range(N+1)]
    def dfs(at):
        if dp[at] is not None:
            return dp[at]

        if not tree[at]:
            return 1

        num_leaf = 1
        for child in tree[at]:
            num_leaf += dfs(child)
        dp[at] = num_leaf
        return num_leaf

    answers = []
    for node in queries:
        answers.append(dfs(node))
    return answers


N, R, Q = [int(c) for c in stdin.readline().strip().split(' ')]
edges, queries = [], []
for _ in range(N-1):
    edges.append([int(c) for c in stdin.readline().strip().split(' ')])
for _ in range(Q):
    queries.append(int(stdin.readline()))

for a in solution(N, R, edges, queries):
    print(a)

"""
2 1 2
1 2
1
2

"""