from sys import stdin
import heapq


def solution(N, lectures):
    lectures.sort(key=lambda x: x[1], reverse=True)

    max_count = 0
    onair = []
    while lectures:
        _, s, e = lectures.pop()
        while onair and onair[0][0] <= s:
            heapq.heappop(onair)
        heapq.heappush(onair, (e, s))
        max_count = max(max_count, len(onair))

    return max_count


N = int(stdin.readline())
lectures = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

print(solution(N, lectures))