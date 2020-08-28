from sys import stdin
from collections import deque
from math import sqrt


def vectorize(a, b):
    return b[0]-a[0], b[1]-a[1]

def cross_len(a, b):
    return a[0]*b[1] - b[0]*a[1]

def solution(N, coord):
    area = 0
    anchor = coord[0]
    for a, b in zip(coord[1:-1], coord[2:]):
        area += cross_len(vectorize(anchor, a), vectorize(anchor, b))
    return round(abs(area / 2), 2)


N = int(stdin.readline())
coord =[[int(c) for c in row.strip().split(' ')] for row in stdin.readlines()]
print(solution(N, coord))
from itertools import permutations