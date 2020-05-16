from sys import stdin
import heapq


def solution(nums):
    answers = []
    heap = []
    for n in nums:
        heapq.heappush(heap, -n)
        if n == 0:
            answers.append(-heapq.heappop(heap))
    return answers


N, nums = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        nums.append(int(row))

for a in solution(nums):
    print(a)