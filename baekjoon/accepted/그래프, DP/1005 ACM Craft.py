from sys import stdin, setrecursionlimit
from math import inf


setrecursionlimit(100000)
def solution(num_node, K, build_time, target, plan):
    # flip graph
    graph = [[] for _ in range(num_node)]
    for f, t in plan:
        graph[t-1].append(f-1)
    # use dp
    dp = {}

    def search(at):
        if not graph[at]:
            return build_time[at]
        if at in dp:
            return dp[at]
        t = -inf
        for comefrom in graph[at]:
            t = max((t, search(comefrom)))

        dp[at] = t+build_time[at]
        return t + build_time[at]

    return search(target - 1)


for _ in range(int(stdin.readline())):
    N, K = [int(c) for c in stdin.readline().strip().split(' ')]
    D, plan = 0, []
    for i in range(K + 1):
        row = [int(c) for c in stdin.readline().strip().split(' ')]
        if i == 0:
            D = row
        else:
            plan.append(row)
    T = int(stdin.readline())
    print(solution(N, K, D, T, plan))
# print(solution(4, 4, [10, 1, 100, 10], 4, [[1, 2], [1, 3], [2, 4], [3, 4]]))
