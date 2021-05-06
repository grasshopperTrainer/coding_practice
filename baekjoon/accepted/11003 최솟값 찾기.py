from sys import stdin
import heapq


def solution(N, L, nums):
    answer = []

    removed = {}
    vals = []
    for i, num in enumerate(nums):
        heapq.heappush(vals, num)
        if 0 <= i - L:
            to_remove = nums[i - L]
            removed[to_remove] = removed.get(to_remove, 0) + 1

        while vals[0] in removed:
            val = heapq.heappop(vals)
            removed[val] -= 1
            if not removed[val]:
                removed.pop(val)
        answer.append(vals[0])
    return ' '.join(map(str, answer))


N, L = map(int, stdin.readline().strip().split(' '))
nums = list(map(int, stdin.readline().strip().split(' ')))
print(solution(N, L, nums))
