from sys import stdin


def solution(N, nums):
    left_dp, right_dp = [1]*N, [1]*N
    for i in range(N):
        for j in range(i-1, -1, -1):
            if nums[j] < nums[i] and left_dp[j] >= left_dp[i]:
                left_dp[i] = left_dp[j]+1

    for i in range(N-1, -1, -1):
        for j in range(i+1, N):
            if nums[j] < nums[i] and right_dp[j] >= right_dp[i]:
                right_dp[i] = right_dp[j]+1

    bitonic = map(lambda x,y: x+y-1, left_dp, right_dp)
    return max(bitonic)


N, nums = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        nums = [int(c) for c in row.strip().split(' ')]

print(solution(N, nums))