from sys import stdin
import heapq


def solution(N, buildings):



N = int(stdin.readline())
buildings = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

print(solution(N, buildings))

"""
3
1 5 4
2 3 6
3 7 5
"""
