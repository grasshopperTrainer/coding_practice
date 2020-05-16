from sys import stdin
from math import inf, isinf
import heapq

def solution(N, M, tickets):
    tree = {}
    for s, e, c, t in tickets:
        d = tree.setdefault(s, {})
        d[e] = [t, c]
        # d.setdefault(e, {})[t] = c

    lead = {i: inf for i in range(1, N+1)}
    lead[1] = 0
    heap = [(0, 1)]
    while heap:
        _, node = heapq.heappop(heap)
        for next_node, (time, _) in tree.get(node, {}).items():
            if lead[next_node] > lead[node] + time:
                lead[next_node] = lead[node] + time
                heapq.heappush(heap, (lead[next_node], next_node))
    print(lead)

    dp = [[inf]*M for _ in range(N+1)]
    for i in range(M):
        for j in range(1, N+1):

            print(tree[j])

            exit()


it = iter(stdin.readlines())
T = int(next(it))
for _ in range(T):
    tickets = []
    N, M, K = [int(c) for c in next(it).strip().split(' ')]
    for _ in range(K):
        tickets.append([int(c) for c in next(it).strip().split(' ')])

    print(solution(N, M, tickets))

"""
1
3 5 3
1 2 1 1
2 3 1 1
1 3 3 30
"""