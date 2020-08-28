from sys import stdin


def solution(N, items):
    if 0 <= items[0] <= items[-1]:
        return items[0], items[1]
    if items[-2] <= items[-1] <= 0:
        return items[-2], items[-1]

    # find border
    for i, v in enumerate(items):
        if v >= 0:
            left, right = i-1, i
            break

    # record
    best = float('inf')
    best_combo = None, None
    while True:
        v = items[right] + items[left]
        if abs(v) < best:
            best = abs(v)
            best_combo = items[left], items[right]
        if v == 0:
            break
        if 0 <= v:
            left -= 1
        else:
            right += 1
        if left < 0 or right >= N:
            break
    return best_combo


N = int(stdin.readline())
items = [int(c) for c in stdin.readline().strip().split(' ')]
print(' '.join(str(i) for i in solution(N, items)))

# import random
# items = [random.randint(-20, 0) for _ in range(10)]
# items.sort()
# print(items)
# print(solution(len(items), items))
# """
# 5
# -5 -2 -1 4 98
# 8
# -10 -5 -2 -1 6 7 8 8
# """
