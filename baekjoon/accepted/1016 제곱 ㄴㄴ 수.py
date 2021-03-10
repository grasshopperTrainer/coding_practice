from sys import stdin
from math import sqrt, ceil


def solution(A, B):
    N = ceil(sqrt(B))
    primes = [True]*N
    for num in range(2, N):
        if primes[num]:
            for i in range(num*2, N, num):
                primes[i] = False
    primes = [i for i in range(2, N) if primes[i]]
    
    counter = 1 if A == 1 else 0
    for i in range(A, B+1):
        n = i
        for p in primes:
            if n < p:
                break
            if n%p == 0:
                n //= p
        if n == i or n == 1:
            counter += 1
    return counter


A, B = map(lambda x: int(x), stdin.readline().strip().split(' '))
print(solution(A, B))

"""
999_999_000_000 1_000_000_000_000
"""