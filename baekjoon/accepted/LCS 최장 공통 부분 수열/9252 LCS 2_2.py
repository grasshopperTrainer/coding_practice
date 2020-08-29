from sys import stdin


def solution(aseq, bseq):
    aseq, bseq = 'f'+aseq, 'f'+bseq # add false char for convenience
    N, M = len(aseq), len(bseq)

    # draw dp
    dp = [[0]*(M) for _ in range(N)]
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = max((dp[i-1][j], dp[i][j-1]))
            if aseq[i] == bseq[j]:
                dp[i][j] = max((dp[i][j], dp[i-1][j-1]+1))

    # track lcs
    lcs = ''
    i, j = N-1, M-1
    while True:
        if dp[i][j] == 0:
            break
        if aseq[i] == bseq[j]:
            lcs = aseq[i] + lcs
            i -= 1
            j -= 1
        else:
            if dp[i][j-1] >= dp[i-1][j]:
                j -= 1
            else:
                i -= 1

    return len(lcs), lcs


for a in solution(*[row.strip() for row in stdin.readlines()]):
    print(a)

"""
ACAYKP
CAPCA
"""