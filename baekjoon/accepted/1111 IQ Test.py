# not accepteddd
from sys import stdin


def solution(N, nums):
    if N == 1:
        return 'A'

    def search(idx, a, b):
        if idx == N - 1:
            return True

        r = nums[idx] * a + b
        if r == nums[idx + 1]:
            return search(idx + 1, a, b)
        else:
            return r

    answer = None

    for inc in (1, -1):
        a, b = 0, 0
        for _ in range(10_000_000):
            b = nums[1] - nums[0] * a
            r = search(0, a, b)

            if isinstance(r, bool):
                if not answer:
                    answer = a, b
                else:
                    return 'A'
            elif 100 < abs(r):
                break
            a += inc

    if answer:
        return nums[-1] * answer[0] + answer[1]
    return 'B'


N = int(stdin.readline())
nums = list(map(int, stdin.readline().strip().split(' ')))

print(solution(N, nums))

"""
3
1 4 61
"""
"""
3
0 3 0
"""
"""
4
0 3 0 1
"""
"""
2
0 0
"""
"""
2
1 -1
"""
"""
5
0 -6 4 -8 8
"""
"""
5
0 -6 -100 100 99
"""
"""
8
0 0 -1 1 -2 2 -3 3
"""
