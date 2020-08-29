from sys import stdin
from itertools import product


def solution(N, series):
    nums_a, nums_b = [], []
    for x, y in product(range(N), repeat=2):
        nums_a.append(series[x][0] + series[y][1])
        nums_b.append(series[x][2] + series[y][3])
    nums_a.sort()
    nums_b.sort()

    L = N**2
    counter = 0
    pointer_a, pointer_b = 0, L-1

    while True:
        sum_v = nums_a[pointer_a] + nums_b[pointer_b]

        if sum_v == 0:
            # need to consider aligned equal values
            shift_a, shift_b = 0, 0
            while True:
                shift_a += 1
                if pointer_a+shift_a >= L:
                    break
                if nums_a[pointer_a+shift_a] != nums_a[pointer_a]:
                    break
            while True:
                shift_b += 1
                if pointer_b-shift_b < 0:
                    break
                if nums_b[pointer_b-shift_b] != nums_b[pointer_b]:
                    break
            # shifting
            pointer_a += shift_a
            pointer_b += shift_b
            # scoring
            counter += shift_a*shift_b
        elif 0 < sum_v:
            pointer_b -= 1
        else:
            pointer_a += 1
        # exit condition
        if pointer_a >= L or pointer_b < 0:
            break
    return counter


N = int(stdin.readline())
series = []
for _ in range(N):
    series.append([int(c) for c in stdin.readline().strip().split(' ')])

print(solution(N, series))
"""
2
0 -100 2 2
0 -4 2 4
"""
# import random
# sets = [random.sample(range(-1000, 1000), 4) for i in range(3000)]
# print(solution(3000, sets))