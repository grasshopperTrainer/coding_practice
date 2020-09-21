from sys import stdin
from collections import deque


def solution(N, weights, edges):
    # draw graph
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    # draw tree
    ROOT = 1
    tree = [[] for _ in range(N+1)] # 1-indexing
    que, visited = deque([ROOT]), {ROOT}
    while que:
        at = que.popleft()
        for child in graph[at]:
            if child not in visited:
                visited.add(child)
                tree[at].append(child)
                que.append(child)
    # calculate
    dp = [[0, 0] for _ in range(N+1)]           # selecting self, else
    dp_set = [[[], []] for _ in range(N+1)]     # register set
    def dfs(at):
        dp[at][0] += weights[at-1]
        dp_set[at][0].append(at)
        if not tree[at]:
            return

        for child in tree[at]:
            dfs(child)
            dp[at][0] += dp[child][1]
            dp_set[at][0] += dp_set[child][1]
            dp[at][1] += max(dp[child])
            if dp[child][0] < dp[child][1]:
                dp_set[at][1] += dp_set[child][1]
            else:
                dp_set[at][1] += dp_set[child][0]
        return
    dfs(ROOT)
    # form answer
    if dp[ROOT][0] < dp[ROOT][1]:
        return dp[ROOT][1], sorted(dp_set[ROOT][1])
    else:
        return dp[ROOT][0], sorted(dp_set[ROOT][0])


N = int(stdin.readline())
weights = [int(c) for c in stdin.readline().strip().split(' ')]
edges = []
for _ in range(N-1):
    edges.append([int(c) for c in stdin.readline().strip().split(' ')])

weigh_sum, nodes = solution(N, weights, edges)
print(weigh_sum)
print(' '.join(str(i) for i in nodes))