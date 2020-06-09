from sys import stdin
from itertools import product


def solution(seq1, seq2):
    L1, L2 = len(seq1), len(seq2)

    # draw dp
    dp = [[0]*(L2+1) for _ in range(L1+1)]
    for a, b in product(range(1, L1+1), range(1, L2+1)):
        if seq1[a-1] == seq2[b-1]:
            dp[a][b] = dp[a-1][b-1]+1
        else:
            dp[a][b] = max([dp[a][b-1], dp[a-1][b]])

    # track
    subseq = ''
    idx1, idx2 = L1, L2
    while dp[idx1][idx2] != 0:
        if seq1[idx1-1] == seq2[idx2-1]:    # same meaning it is a part of largest subseq
            subseq = seq1[idx1-1] + subseq
            idx1 -= 1
            idx2 -= 1
        else:
            if dp[idx1][idx2-1] > dp[idx1-1][idx2]:
                idx2 -= 1
            else:
                idx1 -= 1

    return subseq


answer = solution(*[row.strip() for row in stdin.readlines()])
print(len(answer))
# if len(answer):
print(answer)
