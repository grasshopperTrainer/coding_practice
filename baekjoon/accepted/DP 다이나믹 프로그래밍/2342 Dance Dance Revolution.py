


def solution(steps):
    dp = [[[float('inf')]*5 for _ in range(5)] for _ in range(len(steps))]
    dp[0][0][0] = 0
    for i in range(1, len(steps)):
        step = steps[i-1]
        for j in range(5):
            for k in range(5):
                if j == step:
                    dp[i][step][k] = min(dp[i][step][k], dp[i-1][j][k]+1)
                elif j == 0:
                    dp[i][step][k] = min(dp[i][step][k], dp[i-1][j][k]+2)
                elif (step - j)%2 == 1:
                    dp[i][step][k] = min(dp[i][step][k], dp[i-1][j][k]+3)
                else:
                    dp[i][step][k] = min(dp[i][step][k], dp[i-1][j][k]+4)

                if k == step:
                    dp[i][j][step] = min(dp[i][j][step], dp[i-1][j][k]+1)
                elif k == 0:
                    dp[i][j][step] = min(dp[i][j][step], dp[i-1][j][k]+2)
                elif (step - k)%2 == 1:
                    dp[i][j][step] = min(dp[i][j][step], dp[i-1][j][k]+3)
                else:
                    dp[i][j][step] = min(dp[i][j][step], dp[i-1][j][k]+4)

    last_step = steps[-2]
    return min(min(dp[-1][last_step]), min([dp[-1][i][last_step] for i in range(5)]))


print(solution([int(c) for c in input().strip().split(' ')]))

