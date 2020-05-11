from sys import stdin
from collections import deque


def solution(N):
    nums = deque([1, 1, 1, 1, 2, 2])
    if N <= 5:
        return nums[N]

    nums.popleft()
    for _ in range(6, N+1):
        nums.append(nums.popleft()+nums[-1])
    return nums[-1]


ns = []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        continue
    ns.append(int(row))

for n in ns:
    print(solution(n))