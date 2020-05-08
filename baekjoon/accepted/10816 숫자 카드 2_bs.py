from sys import stdin
from collections import Counter


def solution(N, cards, M, nums):
    cards = sorted(Counter(cards).items())
    L = len(cards)
    result = []
    for n in nums:
        s, e = 0, L-1
        while s < e:
            m = (s+e)//2
            if cards[m][0] < n:
                s = m + 1
            else:
                e = m

        result.append(cards[s][1] if cards[s][0] == n else 0)

    return result


N, cards, M, nums = 0, [], 0, []
for i,row in enumerate(stdin.readlines()):
    if i == 0:
        pool = int(row)
    elif i == 1:
        cards = [int(c) for c in row.strip().split(' ')]
    elif i == 2:
        pool = int(row)
    elif i == 3:
        nums = [int(c) for c in row.strip().split(' ')]

print(' '.join([str(i) for i in solution(N, cards, M, nums)]))