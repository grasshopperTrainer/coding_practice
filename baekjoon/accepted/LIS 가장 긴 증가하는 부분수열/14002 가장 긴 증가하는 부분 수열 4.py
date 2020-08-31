from sys import stdin


def solution(N, nums):
    # build dp
    one_of_end = [-1, 0] # idx, len
    dp = [1]*N
    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
        if dp[i] > one_of_end[1]:
            one_of_end = i, dp[i]

    # track series
    series = [one_of_end[0]]
    while dp[series[-1]] != 1:
        last = series[-1]
        for i in range(last, -1, -1):
            if dp[i] == dp[last]-1:
                series.append(i)
                break   # cause need single arbitrary case

    return [nums[idx] for idx in reversed(series)]


N = int(stdin.readline())
nums = [int(c) for c in stdin.readline().strip().split(' ')]

LIS = solution(N, nums)
print(len(LIS))
print(' '.join([str(i) for i in LIS]))
