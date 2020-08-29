from sys import stdin
from itertools import product


def solution(seq1, seq2):
    dp = [[0]*(len(seq2)+1) for _ in range(len(seq1)+1)]
    for a, b in product(range(1, len(seq1)+1), range(1, len(seq2)+1)):
        if seq1[a-1] == seq2[b-1]:
            dp[a][b] = dp[a-1][b-1]+1
        else:
            dp[a][b] = max([dp[a][b-1], dp[a-1][b]])
    return dp[-1][-1]


print(solution(*[row.strip() for row in stdin.readlines()]))

"""
AAA
BBAB
"""
"""
aaa
bbbaaaa
"""
"""
bbbaaaa
aaa
"""