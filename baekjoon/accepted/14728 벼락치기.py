from sys import stdin


def solution(N, T, studies):
    dp = [[0 for _ in range(T+1)] for _ in range(N)]

    for i in range(N):
        for elapse in range(0, T + 1):
            t, s = studies[i]
            dp[i][elapse] = dp[i-1][elapse]
            if 0 <= elapse - t:
                if dp[i][elapse] < dp[i - 1][elapse - t] + s:
                    dp[i][elapse] = dp[i - 1][elapse - t] + s
    return max(dp[-1])


lexer = lambda: list(map(int, stdin.readline().strip().split(' ')))
N, T = lexer()
studies = [lexer() for _ in range(N)]

print(solution(N, T, studies))

"""
3 20
10 10
10 10
20 100
"""
"""
3 20
10 100
10 50
10 60
"""
