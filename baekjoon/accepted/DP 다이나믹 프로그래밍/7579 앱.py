from sys import stdin

def solution(N, target, sizes, costs):
    MAXCOST = sum(costs)+1

    dp = [[0 for _ in range(MAXCOST+1)] for _ in range(N+1)]
    min_cost = MAXCOST
    for i in range(1, N+1):
        size, cost = sizes[i-1], costs[i-1]
        for j in range(1, MAXCOST+1):
            if j < cost:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max([size+dp[i-1][j-cost], dp[i-1][j]])

            if dp[i][j] >= target:

                min_cost = min([min_cost, j])
                break

    return min_cost

N, target, sizes, costs = 0, 0, [], []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, target = row
    elif i == 1:
        sizes = row
    elif i == 2:
        costs = row

print(solution(N, target, sizes, costs))