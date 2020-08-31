# can tracking be removed? can arbitrary path be build whilst binary searching LIS?
from sys import stdin


def solution(N, nums):
    # binary search LIS
    def maximal_pos(n, lis):
        # need to find maximal position
        # where previous pos is smaller than 'n'
        s, e = 0, len(lis)
        while s < e:
            m = (s+e)//2
            if nums[lis[m][-1]] < n:
                s = m + 1
            else:      # if value is the same...  the pos(m) should be in search pool? making it maximal search?
                e = m
        return s

    lis = []
    for i, n in enumerate(nums):
        if not lis:
            lis.append([i])    # record multiple idx for tracking
            continue
        if n > nums[lis[-1][-1]]:
            lis.append([i])
        else:
            idx = maximal_pos(n, lis)
            lis[idx].append(i)

    # track case
    series = []
    for i in range(len(lis)-1, -1, -1):
        if not series:
            series.append(lis[i][-1])
            continue

        for j in range(len(lis[i])-1, -1, -1):
            if lis[i][j] < series[-1]:
                series.append(lis[i][j])
                break   # cause finding arbitrary case

    return [nums[i] for i in reversed(series)]


N = int(stdin.readline())
nums = [int(c) for c in stdin.readline().strip().split(' ')]

LIS = solution(N, nums)
print(len(LIS))
print(' '.join([str(i) for i in LIS]))

"""
5
1 3 5 8 4
"""
"""
6
1 3 5 8 4 7
"""
"""
6
1 3 5 7 4 6
"""