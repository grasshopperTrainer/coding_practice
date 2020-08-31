# too slow. two pointer is faster
from math import ceil


def solution(N):
    # prepare primes
    primes = [True]*(N+1)
    for i in range(2, ceil((N+1)//2)):
        if primes[i]:
            for n in range(i*2, N+1, i):
                primes[n] = False
    primes = [i for i in range(2, N+1) if primes[i]]
    # search
    dp = [[0]*len(primes) for _ in range(N+1)]
    for n in range(2, N+1):
        for p in range(len(primes)):
            prime = primes[p]
            if prime > n:
                break
            temp = n - prime
            if temp == 0:
                dp[n][p] = 1
            elif temp >= 0:
                dp[n][p] = dp[temp][p-1]
    return sum(dp[-1])


print(solution(int(input())))