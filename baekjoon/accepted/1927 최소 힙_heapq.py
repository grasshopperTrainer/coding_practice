from sys import stdin
import heapq


def solution(nums):
    answer = []
    heap = []
    for n in nums:
        if n == 0:
            if not heap:
                answer.append(0)
            else:
                answer.append(heapq.heappop(heap))
        else:
            heapq.heappush(heap, n)

    return answer


N, nums = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        nums.append(int(row))

for a in solution(nums):
    print(a)