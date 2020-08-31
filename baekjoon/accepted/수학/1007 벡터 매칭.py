from sys import stdin
from itertools import combinations
from math import sqrt


def solution(N, vertex):
    sum_v = [0, 0]
    for x, y in vertex:
        sum_v[0] += x
        sum_v[1] += y

    best = float('inf')
    for idxs in combinations(range(N), N//2):
        v = sum_v.copy()
        for idx in idxs:
            v[0] -= vertex[idx][0]*2
            v[1] -= vertex[idx][1]*2
        l = sqrt(v[0]**2 + v[1]**2)
        best = min((best, l))
    return best


for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    vertex = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N)]
    print(solution(N, vertex))
# N = 4
# vertex = list('abcd')
# print(len(list(combinations(range(8), 4))))
# print(len(list(permutations(range(7)))))
# print(len(list(permutations(range(10)))))
# head = vertex.pop()
# best_l = float('inf')
# for inline in permutations(vertex):
#     teams = inline[:N//2], list(inline[N//2:])+[head]
#     print(teams[0])
#     print(teams[1])
#     print()