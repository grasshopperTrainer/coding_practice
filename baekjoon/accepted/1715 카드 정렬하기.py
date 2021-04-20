from sys import stdin
import heapq


def solution(stacks):
    heapq.heapify(stacks)
    count = 0
    while len(stacks) != 1:
        a, b = heapq.heappop(stacks), heapq.heappop(stacks)
        count += a + b
        heapq.heappush(stacks, a + b)
    return count


stacks = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
print(solution(stacks))
