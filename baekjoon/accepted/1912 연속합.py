from sys import stdin


def solution(N, nums):
    dp = [nums[0]]
    for i, n in enumerate(nums[1:], 1):
        dp.append(max([n, dp[i-1]+n]))

    return max(dp)


N, nums = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N == int(row)
    else:
        nums = [int(c) for c in row.strip().split(' ')]

print(solution(N, nums))