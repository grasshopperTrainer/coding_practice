from sys import stdin
import heapq


def solution(K, N, primes):
    heap = primes.copy()
    for _ in range(N):
        minv = heapq.heappop(heap)

        for p in primes:
            heapq.heappush(heap, minv * p)

            if minv % p == 0:
                break
    return minv




K, N = map(int, stdin.readline().strip().split(' '))
primes = list(map(int, stdin.readline().strip().split(' ')))
print(solution(K, N, primes))