from sys import stdin


def solution(T, k, coins):
    dp = [[0]*(T+1) for _ in range(k+1)]
    dp[0][0] = 1
    for i, (coin, n) in enumerate(coins, 1):
        coin_max_val = coin*n
        for cost in range(T+1):
            if cost > coin_max_val:
                # !KILLER CASE! to ignore the coin being already used to make less costs
                for j in range(n+1):
                    dp[i][cost] += dp[i-1][cost - coin*j]
            else:
                if cost >= coin:
                    # as dp is initialized with 0 value, looking end value by indexing negative
                    # doesn't effect calculation but logically condition check is needed
                    dp[i][cost] += dp[i][cost - coin]
                dp[i][cost] += dp[i-1][cost]

    return dp[-1][T]


T, k, coins = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        T = int(row)
    elif i == 1:
        k = int(row)
    else:
        coins.append([int(c) for c in row.strip().split(' ')])

print(solution(T, k, coins))

"""
20
3
5 3
10 2
1 20
"""

"""
50
3
5 3
10 2
1 5
"""

"""
40
3
5 3
10 2
1 5
"""

"""
39
3
5 3
10 2
1 5
"""

"""
10
3
1 2
2 2
3 3
"""
