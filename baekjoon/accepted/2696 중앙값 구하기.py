from sys import stdin
from math import ceil
import heapq


def solution(nums):
    medians = []
    left_heap, right_heap = [], []
    for i, n in enumerate(nums, 1):
        # init
        if not right_heap:
            right_heap = [n]
            medians.append(n)
            continue

        if right_heap[0] <= n:
            heapq.heappush(right_heap, n)
        else:
            heapq.heappush(left_heap, -n)

        if len(left_heap) == len(right_heap):
            continue
        while len(left_heap) > len(right_heap):
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
        while len(left_heap) + 1 < len(right_heap):
            heapq.heappush(left_heap, -heapq.heappop(right_heap))

        if i % 2 == 1:
            medians.append(right_heap[0])

    print(len(medians))
    for i in range(ceil(len(medians)/10)):
        print(' '.join(map(str, medians[i*10:(i+1)*10])))


for _ in range(int(stdin.readline())):
    M = int(stdin.readline())
    nums = []
    for _ in range(ceil(M / 10)):
        nums += list(map(int, stdin.readline().strip().split(' ')))

    solution(nums)

"""
1
9
1 2 3 4 5 6 7 8 9
"""
"""
1
9
9 8 7 6 5 4 3 2 1
"""
