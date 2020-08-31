from sys import stdin

def solution(N, nums):
    LIS = [nums.pop(0)]

    def find_lowest_pos(n):
        s, e = 0, len(LIS)-1
        if s == e:
            return 0
        # !!! remember this pattern for finding min max !!!
        while s <= e:
            m = (s+e)//2
            if LIS[m] < n:
                s = m + 1
            else:
                e = m - 1
        return s

    for n in nums:
        if n > LIS[-1]:
            LIS.append(n)
        else:
            idx = find_lowest_pos(n)
            LIS[idx] = n

    return len(LIS)


N, nums = 0, []
for i,row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        nums = [int(c) for c in row.strip().split(' ')]

print(solution(N, nums))