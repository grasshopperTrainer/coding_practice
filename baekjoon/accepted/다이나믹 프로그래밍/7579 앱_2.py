from sys import stdin


def solution(N, M, mems, costs):
    # look for max memory gained when X expense is used
    MAX_COST = sum(costs)
    old_dp = [0] * (MAX_COST + 1)
    for mem, cost in zip(mems, costs):
        new_dp = [0] * (MAX_COST + 1)
        for expense in range(0, MAX_COST + 1):
            # can't try to remove last app when target expense is less than
            if expense < cost:
                new_dp[expense] = old_dp[expense]
            else:  # see if removing last app is beneficial
                new_dp[expense] = max((old_dp[expense], old_dp[expense - cost] + mem))
        old_dp = new_dp
    for cost, mem_gained in enumerate(old_dp):
        if mem_gained >= M:
            return cost


args = []
for _ in range(3):
    args.append([int(c) for c in stdin.readline().strip().split(' ')])
print(solution(*args[0], args[1], args[2]))
