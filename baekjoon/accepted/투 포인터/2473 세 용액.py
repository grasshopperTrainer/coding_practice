from sys import stdin


def solution(N, items):
    items.sort()

    if 0 <= items[0] <= items[-1]:
        return items[0], items[1], items[2]
    if items[0] <= items[-1] <= 0:
        return items[-3], items[-2], items[-1]

    best = float('inf')
    best_combo = None
    for middle in range(1, N-1):
        left, right = middle-1, middle+1
        while True:
            # print(left, middle, right)
            v = items[left] + items[middle] + items[right]
            if abs(v) < best:
                best = abs(v)
                best_combo = items[left], items[middle], items[right]
            if v == 0:
                break
            if v < 0:
                right += 1
            if v > 0:
                left -= 1
            if left < 0 or right >= N:
                break
        if best == 0:
            break
    return best_combo


N = int(stdin.readline())
items = [int(c) for c in stdin.readline().strip().split(' ')]
print(' '.join(str(i) for i in solution(N, items)))


# import random
# from itertools import combinations
#
# def dum(N, items):
#     best = float('inf')
#     comb = None
#     for i in combinations(items, 3):
#         if abs(sum(i)) < best:
#             best = abs(sum(i))
#             comb = i
#     return comb
#
# while True:
#     print('__________________________________')
#     items = [random.randint(-20, 20) for _ in range(10)]
#     items.sort()
#     print(items)
#     a, b = solution(len(items), items), dum(len(items), items)
#     print(a, b)
#     print(sum(a), sum(b))
#     if abs(sum(a)) != abs(sum(b)):
#         break
# print(dum(len(items), items))
# """
# 5
# -5 -2 -1 4 98
# 8
# -10 -5 -2 -1 6 7 8 8
# """
