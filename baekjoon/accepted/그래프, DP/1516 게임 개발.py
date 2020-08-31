from sys import stdin


def solution(N, infos):
    # use 1-indexing
    times = [0 for _ in range(N+1)]
    prev_nodes = [[] for i in range(N+1)]
    for node, info in enumerate(infos, 1):
        times[node] = info[0]
        for bn in info[1:]:
            if bn == -1:
                break
            prev_nodes[node].append(bn)
    # search using dp
    dp = [0 for _ in range(N+1)]
    def search(at):
        if dp[at]:
            pass
        elif not prev_nodes[at]:
            dp[at] = times[at]
        else:
            max_t = 0
            for nn in prev_nodes[at]:
                max_t = max((max_t, search(nn)))
            dp[at] = max_t+times[at]
        return dp[at]
    # execute
    for i in range(1, N+1):
        search(i)
    return dp[1:]


N = int(stdin.readline())
infos = []
for row in range(N):
    infos.append([int(c) for c in stdin.readline().strip().split(' ')])

for a in solution(N, infos):
    print(a)