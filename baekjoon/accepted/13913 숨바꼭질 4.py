from sys import stdin
import heapq


def solution(N, K):
    best_time = None
    L = max(K, N) * 2
    record = [float('inf')] * L
    record[N] = 0
    moves = [(0, N)]  # time at
    while moves:
        time, at = heapq.heappop(moves)
        if at != N and record[at] <= time:
            continue
        record[at] = time

        if at == K:
            best_time = time
            break

        if 0 <= at - 1 and time + 1 < record[at - 1]:
            heapq.heappush(moves, (time + 1, at - 1))
        if at + 1 < L and time + 1 < record[at + 1]:
            heapq.heappush(moves, (time + 1, at + 1))
        if at * 2 < L and time + 1 < record[at * 2]:
            heapq.heappush(moves, (time + 1, at * 2))

    path = []
    at = K
    while at != N:
        path.append(at)
        if at != 0 and at % 2 == 0 and record[at // 2] == record[at] - 1:
            at = at // 2
            continue
        if 0 <= at - 1 and record[at - 1] == record[at] - 1:
            at = at - 1
            continue
        if at + 1 < L and record[at + 1] == record[at] - 1:
            at = at + 1
            continue
        raise
    path.append(N)

    path.reverse()
    print(best_time)
    print(' '.join(map(str, path)))


solution(*map(int, stdin.readline().strip().split(' ')))
"""
100000 0
"""
