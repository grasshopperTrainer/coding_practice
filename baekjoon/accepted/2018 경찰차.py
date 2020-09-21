from sys import stdin


def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def solution(N, W, crimes):
    dp = [[[float('inf')]*(W+1) for _ in range(W+1)] for _ in range(W+1)]
    dp[0][0][0] = 0
    for crime in range(1, W+1):
        for f_at in range(W+1):
            for s_at in range(W+1):
                d = dist(crimes[s_at-1], (N,N) if s_at==1 else crimes[s_at-1-1])
                dp[crime][f_at][s_at] = min(dp[crime][f_at][s_at], dp[crime-1][f_at][s_at-1]+d)
                d = dist(crimes[f_at-1], (1,1) if f_at==1 else crimes[f_at-1-1])
                dp[crime][f_at][s_at] = min(dp[crime][f_at][s_at], dp[crime-1][f_at-1][s_at]+d)

    for row in dp:
        print(row)
    print(dp[-1][W])
    print([i[W] for i in dp[-1]])



N = int(stdin.readline())
W = int(stdin.readline())
crimes = []
for _ in range(W):
    crimes.append([int(c) for c in stdin.readline().strip().split(' ')])
for a in solution(N, W, crimes):
    print(a)


"""
6
2
2 2
5 5

"""