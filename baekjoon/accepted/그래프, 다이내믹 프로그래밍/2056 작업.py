from sys import stdin


def solution(N, infos):
    # draw reverse graph
    # pre drawing can be ignored but this way is faster
    graph = {i:[] for i in range(N)}
    times = []
    for i, info in enumerate(infos):
        times.append(info[0])
        if info[1]:
            for next_n in info[2:]:
                graph[i].append(next_n-1)
    dp = {}

    def search(at):
        if not graph[at]:
            return times[at]
        if at in dp:
            return dp[at]
        max_t = 0
        for back_n in graph[at]:
            max_t = max((max_t, search(back_n)))
        dp[at] = max_t + times[at]
        return dp[at]

    max_t = 0
    for i in range(N):
        max_t = max((max_t, search(i)))
    return max_t


N, infos = int(stdin.readline()), []
for row in stdin.readlines():
    infos.append([int(c) for c in row.strip().split(' ')])
print(solution(N, infos))