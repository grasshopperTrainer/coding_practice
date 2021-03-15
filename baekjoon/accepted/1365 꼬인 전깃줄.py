from sys import stdin
import bisect


def solution(N, nums):
    array = []
    for num in nums:
        i = bisect.bisect_right(array, num)
        if len(array) == i:
            array.append(num)
        else:
            array[i] = num
    return len(nums) - len(array)


N = int(stdin.readline())
nums = list(map(int, stdin.readline().strip().split(' ')))

print(solution(N, nums))

"""
7
3 4 6 1 2 3 5
"""