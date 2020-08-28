from sys import stdin
from math import inf


def solution(N, thresh, nums):
    l, r = -1, -1
    min_l = inf
    sum_v = 0
    while l < N and r < N:
        # move pointer
        if l == r or sum_v < thresh:
            r += 1
            if r < N:
                sum_v += nums[r]
        else:
            l += 1
            if l < N:
                sum_v -= nums[l]
        # check value
        if sum_v >= thresh:
            min_l = min((min_l, r-l))
    return min_l if min_l != inf else 0


N, thresh = [int(c) for c in stdin.readline().strip().split(' ')]
nums = [int(c) for c in stdin.readline().strip().split(' ')]
print(solution(N, thresh, nums))
"""
3 3
3 3 3
"""
"""
5 10
2 4 2 1 2
"""