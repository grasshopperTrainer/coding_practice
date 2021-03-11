from sys import stdin


def solution(N, costs, money):
    min_cost = min(costs)
    max_pick = money//min_cost

    dp = [[None] * (money + 1) for _ in range(max_pick + 1)]

    highest = 0
    cost_num = {}
    for n, c in enumerate(costs):
        cost_num[c] = str(n)  # bigger number always comes later so automatically overridden for same cost
        if c <= money:
            dp[1][c] = str(n)
            highest = max(highest, n)

    for pick_count in range(2, max_pick + 1):
        for spent in range(1, money + 1):
            for c, n in cost_num.items():   # try bying this number
                if c <= spent:
                    prev = dp[pick_count - 1][spent - c]
                    if prev is not None:    # if spent - c could have bought something
                        if int(n) < int(prev[0]):
                            dp[pick_count][spent] = prev + n
                        else:
                            dp[pick_count][spent] = n + prev

                        if dp[pick_count][spent] is not None:
                            highest = max(highest, int(dp[pick_count][spent]))
    return highest


N = int(stdin.readline())
costs = list(map(int, stdin.readline().strip().split(' ')))
money = int(stdin.readline())
print(solution(N, costs, money))

"""
1
10
1
"""
