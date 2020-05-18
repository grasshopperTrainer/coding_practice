from sys import stdin
from math import inf, isinf
import heapq


def solution(N, budget, tickets):
    tree = {}
    for s, e, c, t in tickets:
        d = tree.setdefault(s, {})
        d[e] = [c, t]
        # # what if there are more than one tickets connecting two airports?
        # d.setdefault(e, []).append([c, t])

    # add 1 for index starting with 1 and money spent being exactly at budget
    dp = [[inf] * (budget + 1) for _ in range(N + 1)]    # dp[arrive_at][money_spent] = min time_spent
    dp[1][0] = 0    # record starting

    # min_time_spent, money_spent, pos
    # target is min_time so put it in front to be sorted with it
    heap = [(0, 0, 1)]
    while heap:
        time_to_here, money_to_here, node = heapq.heappop(heap)
        # if min time already revised no need to follow this search
        if time_to_here > dp[node][money_to_here]:
            continue

        for next_node, (cost, time) in tree.get(node, {}).items():
            # for cost, time in tickets:
            money_spent_next = money_to_here + cost
            time_to_next = time_to_here + time
            # only record cases possible to arrive to the end within the budget
            if money_spent_next > budget:
                continue
            if dp[next_node][money_spent_next] > time_to_next:
                dp[next_node][money_spent_next] = time_to_next
                heapq.heappush(heap, (time_to_next, money_spent_next, next_node))

    best = min(dp[-1])  # dp[last = arriving at LA]
    return best if not isinf(best) else 'Poor KCM'


it = iter(stdin.readlines())
T = int(next(it))
for i in range(T):
    tickets = []
    N, M, K = [int(c) for c in next(it).strip().split(' ')]
    for _ in range(K):
        tickets.append([int(c) for c in next(it).strip().split(' ')])
    print(solution(N, M, tickets))

"""
2
3 100 3
1 2 1 1
2 3 1 1
1 3 3 30
4 12 5
1 2 5 3
2 3 2 4
3 2 1 1
3 4 1 5
1 3 11 6

"""