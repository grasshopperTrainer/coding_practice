from sys import stdin
from collections import Counter
from math import log10


def solution(N):
    counter = [0]*10

    unit = 1
    while True:
        to_nine_count = 0

        while N%10 != 9:
            N += 1
            to_nine_count += 1
        chunk = N//10
        print(N, chunk, unit, to_nine_count)
        for i in range(10):
            counter[i] += (chunk+1)
        for i in range(9, 9-to_nine_count, -1):
            counter[i] -= 1
        print(counter)
        N //= 10
        counter[0] -= 1
        counter[N%10] += 1
        if N == 0:
            break
        unit *= 10

    return counter


N = int(stdin.readline())
print(' '.join([str(i) for i in solution(N)]))

# def dum_solution(N):
#     counter = [0,0,0,0,0,0,0,0,0,0]
#     for i in range(1, N+1):
#         for c in str(i):
#             counter[int(c)] += 1
#     return counter
#
# print(' '.join([str(i) for i in dum_solution(N)]))
