from sys import stdin

def solution(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    cache = 0, 1
    for n in range(2, N+1):
        cache = cache[1], sum(cache)
    return cache[1]


print(solution(int(stdin.read())))