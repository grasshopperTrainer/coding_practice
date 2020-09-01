def solution(N):
    # dp with bitmask pattern
    dp = [[[0]*(2**10) for _ in range(10)] for _ in range(N+1)] # len, end, pattern
    for i in range(1, 10):  # don't forget 0 is not considered as stair num
        dp[1][i][2**i] = 1

    for i in range(2, N+1):         # length
        for j in range(10):         # ending num
            for k in range(2**10):  # occupied pattern
                if j != 0:
                    dp[i][j][k | 1 << j] += dp[i-1][j-1][k] % 1_000_000_000
                if j != 9:
                    dp[i][j][k | 1 << j] += dp[i-1][j+1][k] % 1_000_000_000

    return sum([dp[-1][i][2**10-1] for i in range(10)]) % 1_000_000_000


print(solution(int(input())))