from sys import stdin


def solution(N, nums):
    dp = []
    for this in range(N):
        dp.append(1)    # having self only is also a subsequence
        for before in range(this-1, -1, -1):
            if nums[this] > nums[before] and dp[this] < dp[before]+1:
                dp[this] = dp[before]+1
                
    return max(dp)


N, nums = 0, []
for i,row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        nums = [int(c) for c in row.strip().split(' ')]

print(solution(N, nums))