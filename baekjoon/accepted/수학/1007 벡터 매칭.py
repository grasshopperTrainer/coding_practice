from sys import stdin
from itertools import combinations
from math import sqrt


def solution(N, vertex):
    # vector all summed
    total_v = [sum(i) for i in zip(*vertex)]
    # look for possibilities
    min_l = float('inf')
    for selection in combinations(range(N), N//2):
        # took very long as sub_sum_vec can become very big,
        # better directly subtract from copied total_v
        sub_sum_vec = [sum(i) for i in zip(*[vertex[i] for i in selection])]
        temp_v = [a-2*b for a, b in zip(total_v, sub_sum_vec)]
        min_l = min(min_l, sqrt(sum([i**2 for i in temp_v])))

    return min_l


for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    vertex = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N)]
    print(solution(N, vertex))