from sys import stdin, setrecursionlimit

# setrecursionlimit(300_000)
def solution(N, weights, supervisors):
    ROOT = 1

    graph = [[] for _ in range(N+1)]
    for i, s in enumerate(supervisors, 2):
        graph[s].append(i)

    dp = [[0, 0] for _ in range(N+1)]
    def fill_dp(at):
        if not graph[at]:
            dp[at] = [weights[at-1], 0]
            return dp[at]

        summed = [weights[at-1], 0]
        for child in graph[at]:
            vs = fill_dp(child)
            max_v = max(vs)
            summed[1] += max_v if 0 < max_v else 0
            summed[0] += vs[1] if 0 < vs[1] else 0
        dp[at] = summed
        return summed

    def build_route(at, selected):
        nodes = []
        if selected:
            nodes.append(at)
            for child in graph[at]:
                if 0 < dp[child][1]:
                    nodes += build_route(child, False)
        else:
            nodes = []
            for child in graph[at]:
                if 0 < max(dp[child]):
                    if dp[child][0] < dp[child][1]:
                        nodes += build_route(child, False)
                    else:
                        nodes += build_route(child, True)
        return nodes

    fill_dp(ROOT)
    select_root = build_route(ROOT, True)
    not_select_root = build_route(ROOT, False)
    select_root.sort()
    not_select_root.sort()

    print(' '.join(map(str, dp[ROOT])))
    print(' '.join(map(str, select_root+[-1])))
    print(' '.join(map(str, not_select_root+[-1])))


N = int(stdin.readline())
weights = [int(c) for c in stdin.readline().strip().split(' ')]
supervisors = [int(c) for c in stdin.readline().strip().split(' ')]

solution(N, weights, supervisors)