from sys import stdin
from math import factorial, gcd


def solution(N, nums, K):
    dp = [[0]*101 for i in range(2**N+1)]
    dp[0][0] = 1    # num ways dividable by K by selecting nothing and having 0 remainder, 0/K = 0?
    for selection in range(2**N):
        for remainder in range(101):
            for selected_num in range(N):
                new_selection = selection | 1 << selected_num
                if new_selection != selection:
                    dp[new_selection][]

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