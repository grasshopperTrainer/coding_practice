# how to find loop?
from sys import stdin
from collections import deque


def solution(N, M, orders):
    graph = {i: [] for i in range(1, N+1)}
    rank = {i: 0 for i in range(1, N+1)}

    for order in orders:
        for singer, next_singer in zip(order, order[1:]):
            graph[singer].append(next_singer)
            rank[next_singer] += 1

    graph['decoy'] = []
    # initiate front
    front_que = deque()
    for k, v in rank.items():
        if not v:
            front_que.append(k)
            graph['decoy'].append(k)    # tik roots
    # cycle check
    checked = set()
    def is_cyclic(at, visited=set()):
        if at in checked:
            return False
        for c in graph[at]:
            if c not in visited:
                visited.add(c)
                if is_cyclic(c, visited):
                    return True
                visited.remove(c)
            else:
                return True
        checked.add(at)
        return False
    if is_cyclic('decoy'):
        return [0]

    correct_order = []
    while front_que:
        singer = front_que.popleft()
        correct_order.append(singer)
        for next_s in graph[singer]:
            rank[next_s] -= 1
            if not rank[next_s]:
                front_que.append(next_s)
    return correct_order


N, M = [int(c) for c in stdin.readline().strip().split(' ')]
orders = []
for _ in range(M):
    orders.append([int(c) for c in stdin.readline().strip().split(' ')[1:]])

for a in solution(N, M, orders):
    print(a)

"""
6 3
3 1 4 3
4 6 2 5 4
2 3 2
"""
# from random import randint, shuffle, randrange, sample
# # N = randint(1, 6)
# for t in range(100):
#     print()
#     print('try', t)
#     N = 100
#     s = [i for i in range(1, N+1)]
#     shuffle(s)
#     M = 50
#     splits = [0] + sorted(sample([i for i in range(1,N)], M-1)) + [N]
#     orders = []
#     for f, b in zip(splits, splits[1:]):
#         s = [i for i in range(1, N+1)]
#         shuffle(s)
#         orders.append(s[f:b])
#     s = solution(N, M, orders)
#     if s == [0]:
#         print('_______')
#         for o in orders:
#             print(o)
#         print(s)
#         continue
#
#     d = {e:i for i,e in enumerate(s)}
#     for order in orders:
#         prev = -1
#         for i in order:
#             if d[i] > prev:
#                 prev = d[i]
#             else:
#                 raise
#     print('goot', orders, s)