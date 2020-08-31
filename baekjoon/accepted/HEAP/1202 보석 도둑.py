from sys import stdin
import heapq


def solution(N, K, gems, bags):
    gems.sort(key=lambda x: x[0], reverse=True)
    bags.sort()

    score = 0
    heap = []
    for bag in bags:
        while gems and gems[-1][0] <= bag:
            weight, price = gems.pop()
            heapq.heappush(heap, (-price, weight))
        if heap:
            score += -heapq.heappop(heap)[0]
    return score


N, K = [int(c) for c in stdin.readline().strip().split(' ')]
gems = []
for _ in range(N):
    gems.append([int(c) for c in stdin.readline().strip().split(' ')])
bags = []
for _ in range(K):
    bags.append(int(stdin.readline()))
print(solution(N, K, gems, bags))


# import random
# N = random.randint(1, 300_000)
# K = random.randint(1, 300_000)
# gems, bags = [], []
# for _ in range(N):
#     gems.append((random.randint(1, 100), random.randint(1, 100)))
# for _ in range(K):
#     bags.append(random.randint(1, 100))
# print(N, K)
# print(solution(N, K, gems, bags))

"""
4 4
2 99
5 65
7 23
3 15
10
8
4
3
"""
"""
4 4
1 100
2 200
13 300
10 500
10
10
10
14
"""
"""
1 1
5 1
1
"""