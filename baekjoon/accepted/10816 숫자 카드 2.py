from sys import stdin
from collections import Counter

def solution(N, cards, M, nums):
    cards = Counter(cards)
    result = []
    for n in nums:
        if n not in cards:
            result.append(0)
        else:
            result.append(cards[n])
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