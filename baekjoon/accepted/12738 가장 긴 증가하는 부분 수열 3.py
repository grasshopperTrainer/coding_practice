from sys import stdin
import bisect


def solution(nums):
    lis = []
    for num in nums:
        if not lis:
            lis.append(num)
            continue
        if lis[-1] < num:
            lis.append(num)
        else:
            i = bisect.bisect_left(lis, num)
            lis[i] = num
    return len(lis)


stdin.readline()
nums = list(map(int, stdin.readline().strip().split(' ')))
print(solution(nums))

"""
5
3 3 5 5 6
 """
