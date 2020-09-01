from sys import stdin, setrecursionlimit


setrecursionlimit(101100)
def solution(N, K, T, G, E):
    # use 1index
    graph = [[] for i in range(N+1)]    # record building before
    for before, current in E:
        graph[current].append(before)

    # search using dfs
    dp = [None for _ in range(N+1)] # None for not recorded

    def dfs(at):
        if dp[at] is not None:
            return dp[at]
        max_time = 0 # max building all previous building
        for prev in graph[at]:
            max_time = max(max_time, dfs(prev))
        # record to reference afterward
        dp[at] = max_time + T[at-1] # -1 for 0indexing
        return dp[at]

    return dfs(G)


for _ in range(int(stdin.readline())):
    N, K = [int(c) for c in stdin.readline().strip().split(' ')]
    T, E = 0, []
    for i in range(K + 1):
        row = [int(c) for c in stdin.readline().strip().split(' ')]
        if i == 0:
            T = row
        else:
            E.append(row)
    G = int(stdin.readline())
    print(solution(N, K, T, G, E))
