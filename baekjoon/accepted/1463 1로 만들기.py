from sys import stdin

def solution(N):
    cache = [10000000 for _ in range(N+1)]
    cache[-1] = 0

    for n in range(N, 1, -1):
        if n%3 == 0:
            k = n//3
            cache[k] = min([cache[k], cache[n]+1])
        if n%2 == 0:
            k = n//2
            cache[k] = min([cache[k], cache[n]+1])
        k = n-1
        cache[k] = min([cache[k], cache[n]+1])

    return cache[1]

N = int(input())
print(solution(N))