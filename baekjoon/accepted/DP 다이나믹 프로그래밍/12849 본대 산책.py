# from sys import setrecursionlimit
#
#
# setrecursionlimit(100_100)
# # recursive dp
# def solution(D):
#     graph = [[1, 2],
#              [0, 2, 3],
#              [0, 1, 3, 4],
#              [1, 2, 4, 5],
#              [2, 3, 5, 6],
#              [3, 4, 7],
#              [4, 7],
#              [5, 6]]
#
#     dp = {}
#     def dfs(at, t):
#         if (at, t) in dp:
#             return dp[(at, t)]
#         if t == D:
#             if at == 0:
#                 return 1
#             else:
#                 return 0
#         count = 0
#         for to in graph[at]:
#             count += dfs(to, t+1) % 1_000_000_007
#         dp[(at, t)] = count % 1_000_000_007
#         return dp[(at, t)]
#     return dfs(0, 0)

# iteration?
def solution(D):
    graph = [[1, 2],
             [0, 2, 3],
             [0, 1, 3, 4],
             [1, 2, 4, 5],
             [2, 3, 5, 6],
             [3, 4, 7],
             [4, 7],
             [5, 6]]

    dp = [[0]*8 for _ in range(D+1)]
    dp[0][0] = 1
    for i in range(1, D+1):
        for j in range(8):
            for linked in graph[j]:
                dp[i][j] += dp[i-1][linked]
            dp[i][j] %= 1_000_000_007
    return dp[D][0]


print(solution(int(input())))