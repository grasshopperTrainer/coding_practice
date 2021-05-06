from sys import stdin


def solution(N, coins, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        coin = coins[i - 1]
        dp[i][0] = 1
        for cost in range(1, M + 1):
            dp[i][cost] = dp[i - 1][cost]
            if 0 <= cost - coin:
                dp[i][cost] += dp[i][cost - coin]
    return dp[-1][-1]


for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    coins = list(map(int, stdin.readline().strip().split(' ')))
    M = int(stdin.readline())
    print(solution(N, coins, M))
