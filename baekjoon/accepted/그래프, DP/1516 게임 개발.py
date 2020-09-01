from sys import stdin


def solution(N, infos):
    # draw graph
    graph = [None for _ in range(N+1)]    # 1indexing
    times = [0 for _ in range(N+1)]
    for node, (time, *befores) in enumerate(infos, 1):
        times[node] = time
        graph[node] = befores[:-1]
    # search
    dp = [None for _ in range(N+1)]
    def dfs(at):
        if dp[at] is not None:
            return dp[at]
        max_t = 0
        for before in graph[at]:
            max_t = max(max_t, dfs(before))
        dp[at] = max_t + times[at]
        return dp[at]

    return [dfs(i) for i in range(1, N+1)]


N = int(stdin.readline())
infos = []
for row in range(N):
    infos.append([int(c) for c in stdin.readline().strip().split(' ')])

for a in solution(N, infos):
    print(a)