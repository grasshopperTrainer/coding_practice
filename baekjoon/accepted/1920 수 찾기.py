from sys import stdin

def solution(nums, pool):
    result = []
    pool = set(pool)
    for n in nums:
        if n in pool:
            result.append(1)
        else:
            result.append(0)
    return result


nums, pool = [], []
for i,row in enumerate(stdin.readlines()):
    if i == 1:
        pool = [int(c) for c in row.strip().split(' ')]
    elif i == 3:
        nums = [int(c) for c in row.strip().split(' ')]

for a in solution(nums, pool):
    print(a)