from sys import stdin
import heapq


def solution(N, dcosts, pcosts):
    # adding imaginary starting node
    pcosts.append(dcosts.copy())

    heap = [(0, N)]
    picked = [False]*(N+1)
    sum_cost = 0
    while heap:
        c, at = heapq.heappop(heap)
        if picked[at]:
            continue
        picked[at] = True
        sum_cost += c

        for goto, cost in enumerate(pcosts[at]):
            if picked[goto]:
                continue

            if dcosts[goto] < cost:
                heapq.heappush(heap, (dcosts[goto], goto))
            else:
                heapq.heappush(heap, (cost, goto))
    return sum_cost


N = int(stdin.readline())
dcosts = [int(stdin.readline()) for _ in range(N)]
pcosts = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

print(solution(N, dcosts, pcosts))