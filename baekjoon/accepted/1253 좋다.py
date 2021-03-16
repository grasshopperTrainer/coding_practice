from sys import stdin


def solution(N, nums):
    if N <= 2:
        return 0
    nums.sort()

    count = 0
    for i in range(N):
        target = nums[i]
        lp, rp = 0, N-1
        while lp < rp:
            if rp == i:
                rp -= 1
                continue
            if lp == i:
                lp += 1
                continue

            summed = nums[lp] + nums[rp]
            if summed == target:
                count += 1
                break
            elif summed < target:
                lp += 1
            elif summed > target:
                rp -= 1
    return count


N = int(stdin.readline())
nums = list(map(int, stdin.readline().strip().split(' ')))

print(solution(N, nums))

"""
3
0 0 0
"""
"""
4
0 0 1 1
"""
"""
7
0 0 0 0 0 1 1
"""