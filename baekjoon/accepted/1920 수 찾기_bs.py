from sys import stdin

def solution(pool, nums):
    L = len(pool)
    pool.sort()

    result = []
    for n in nums:
        s, e = 0, L-1
        while s < e:
            m = (s+e)//2
            if n > pool[m]:
                s = m+1
            else:
                e = m
        result.append(int(pool[s] == n))

    return result

pool, nums = [], []
for i,row in enumerate(stdin.readlines()):
    if i == 1:
        pool = [int(c) for c in row.strip().split(' ')]
    elif i == 3:
        nums = [int(c) for c in row.strip().split(' ')]

for a in solution(pool, nums):
    print(a)