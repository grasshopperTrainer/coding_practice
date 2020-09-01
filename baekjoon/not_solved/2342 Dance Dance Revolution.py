


def solution(steps):
    dp = [[[float('inf')]*5 for _ in range(5)] for _ in range(len(steps)+1)]
    dp[0][0][0] = 0
    for i in range(1, len(steps)+1):
        for j in range(5):
            for k in range(5):
                dp[i][j][k] = min(dp[i-1][0][k]+2, dp[i-1][0][k])  # move leg on center or



print(solution([int(c) for c in input().strip().split(' ')]))

