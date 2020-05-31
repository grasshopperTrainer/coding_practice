from sys import stdin
from math import factorial, gcd


def solution(N, nums, K):
    L = len(str(K))

    record = {}
    def count(selection, merged):
        if merged in record:
            return record[merged]

        if merged != '' and len(merged) >= L:
            if int(merged) % K == 0:
                # count bits by Brian Kernighan's Algorithm
                c = 0
                while selection:
                    selection &= selection - 1
                    c += 1
                num_ways = factorial(N - c)
                record[int(merged)] = num_ways
                return num_ways

        total = 0
        for shift in range(N):
            temp_selection = selection | (1 << shift)
            if selection != temp_selection:
                total += count(temp_selection, nums[shift] + merged)
        return total

    num_dividable, max_count = count(0, ''), factorial(N)
    if num_dividable == 0:
        return '0/1'
    else:
        divisor = gcd(num_dividable, max_count)
        return f'{num_dividable//divisor}/{max_count//divisor}'


N = int(stdin.readline())
nums = [stdin.readline().strip() for i in range(N)]
K = int(stdin.readline())

print(solution(N, nums, K))

"""
5
5221
40
1
58
9
2
"""
"""
3
12
2
1
1
"""