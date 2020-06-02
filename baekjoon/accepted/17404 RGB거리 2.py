from sys import stdin
from math import inf
from itertools import product


def solution(N, board):
    min_cost = inf
    for first_color in range(3):  # look for each case separately
        dp = [[inf]*3 for _ in range(N)]
        dp[0][first_color] = board[0][first_color]
        for house in range(1, N):
            for this_color, prev_color in product(range(3), repeat=2):
                if house == N-1 and this_color == first_color:
                    continue
                if this_color != prev_color:
                    dp[house][this_color] = min([dp[house][this_color], dp[house-1][prev_color] + board[house][this_color]])
        min_cost = min([min_cost, min(dp[-1])])

    return min_cost


N = int(stdin.readline())
board = [[int(c) for c in stdin.readline().strip().split(' ')]for _ in range(N)]

print(solution(N, board))