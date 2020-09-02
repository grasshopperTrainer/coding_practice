
def solution(A, B):
    dp = {}
    def count(N):
        if N in dp:
            return dp[N]
        if N <= 1:
            return N
        t = 1
        while t <= N:
            t *= 2
        t //= 2
        n = count(t-1) + count(N - t) + N - (t - 1)
        dp[N] = n
        return n

    return count(B) - count(A-1)


print(solution(*[int(c) for c in input().strip().split(' ')]))