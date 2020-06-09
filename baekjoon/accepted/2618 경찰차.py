from sys import stdin
from itertools import product


def solution(N, W, cases):

    def dist(before, after):
        return sum(map(lambda x,y: abs(x-y), before, after))

    # draw dp
    dp = [[0]*(W+1) for _ in range(W+1)]
    # initiate
    for i in range(1, W+1):
        if i == 1:
            dp[0][i] = dist((N, N), cases[i-1])
        else:
            dp[0][i] = dp[0][i-1] + dist(cases[i-2], cases[i-1])
    for j in range(1, W+1):
        if j == 1:
            dp[j][0] = dist((1, 1), cases[j-1])
        else:
            dp[j][0] = dp[j-1][0] + dist(cases[j-2], cases[j-1])

    for i, j in product(range(1, W+1), repeat=2):
        if i == j:
            continue
        elif i > j:
            if i-1 == j:
                dp[i][j] = dp[i-2][j] + dist(cases[i-3] if i-2 > 0 else (1, 1), cases[i-1])
            else:
                dp[i][j] = dp[i-1][j] + dist(cases[i-2], cases[i-1])
        else:
            if i == j-1:
                dp[i][j] = dp[i][j-2] + dist(cases[j-3] if j-2 > 0 else (N, N), cases[j-1])
            else:
                dp[i][j] = dp[i][j-1] + dist(cases[j-2], cases[j-1])
    for row in dp:
        print(row)
    


N, W = int(stdin.readline()), int(stdin.readline())
cases = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(W)]

answer = solution(N, W, cases)
print(len(answer))
for a in answer:
    print(a)