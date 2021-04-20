from sys import stdin
import heapq


def solution(N, problems):
    problems.sort()
    heap = []
    for i, (dead, score) in enumerate(problems):
        if dead <= len(heap):
            heapq.heappop(heap)
        heapq.heappush(heap, (score, dead))

    return sum(map(lambda x: x[0], heap))


N = int(stdin.readline())
problems = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

print(solution(N, problems))

"""
4
1 5
1 5
10 1
2 1
"""
"""
4
10 5
10 5
10 10
10 20
"""
"""
1
10 5
"""
"""
2
1 2
2 10
"""
"""
3
1 2
2 10
3 5
"""
"""
6
1 10
2 20
2 5
3 100
4 100
5 100
"""