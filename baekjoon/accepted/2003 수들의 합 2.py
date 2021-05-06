from sys import stdin


def solution(N, M, nums):
    count = 0
    summed = 0
    a, b = 0, 0
    while True:
        if summed == M:
            count += 1
        if summed <= M:
            if b == N:
                break
            summed += nums[b]
            b += 1
        else:
            summed -= nums[a]
            a += 1
    return count


N, M = map(int, stdin.readline().strip().split(' '))
nums = list(map(int, stdin.readline().strip().split(' ')))
print(solution(N, M, nums))
"""
1 1
1
"""

"""
2 2
1 1
"""
"""
6 13
2 3 5 7 11 13
"""
"""
3 1
1 2 1
"""
"""
5 2
5 2 1000 1 1
"""