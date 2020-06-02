from sys import stdin


def solution(N, K):
    if K == 1:
        return N

    MOD = 1_000_000_003

    dp = [[1]+[0]*K for _ in range(N+1)]
    dp[3][1] = 3
    dp[4][1], dp[4][2] = 4, 2

    for num_colors in range(5, N+1):
        for num_selected in range(1, K+1):
            dp[num_colors][num_selected] += dp[num_colors - 2][num_selected - 1] + dp[num_colors - 1][num_selected]
            dp[num_colors][num_selected] %= MOD

    return dp[N][K]


N, K = [int(c) for c in stdin.readlines()]

print(solution(N, K))

# for n in range(4, 1001):
#     for k in range(1, n+1):
#         s = solution(n, k)
#         if s == 0:
#             break
#         print(n, k, s)