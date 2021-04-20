from sys import stdin
import heapq


def solution(N, M, rooms):
    for skills in rooms:
        skills.sort()

    min_gap = float('inf')
    maxv = max(r[0] for r in rooms)
    heap = [(r[0], i, 1) for i, r in enumerate(rooms)]
    heapq.heapify(heap)
    while True:
        min_gap = min(min_gap, maxv - heap[0][0])
        skill, roomi, studi = heapq.heappop(heap)
        if studi == M:
            break
        skill = rooms[roomi][studi]
        maxv = max(maxv, skill)
        heapq.heappush(heap, (skill, roomi, studi + 1))
    return min_gap


N, M = map(int, stdin.readline().strip().split(' '))
rooms = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

print(solution(N, M, rooms))

"""
2 1
6
3
"""
