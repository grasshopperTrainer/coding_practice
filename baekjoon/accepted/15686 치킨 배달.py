from sys import stdin
from itertools import combinations, product
from math import inf


def solution(N, M, board):
    # find position of stores and houses
    HOUSE, STORE = 1, 2
    houses, stores = [], []
    for x, y in product(range(N), repeat=2):
        if board[x][y] == HOUSE:
            houses.append((x, y))
        elif board[x][y] == STORE:
            stores.append((x, y))

    # build distance board
    LS, LH = len(stores), len(houses)
    dist_board = [[0]*LS for _ in range(LH)]
    for h_idx, s_idx in product(range(LH), range(LS)):
        dist_board[h_idx][s_idx] = sum(map(lambda x,y: abs(x-y), stores[s_idx], houses[h_idx]))

    # calculate best combination
    min_total_dist = inf
    for selection in combinations(range(LS), M):
        total_dist = 0
        for house in dist_board:
            total_dist += min([house[s_idx] for s_idx in selection])
            if total_dist > min_total_dist:
                break
        else:
            min_total_dist = min([min_total_dist, total_dist])

    return min_total_dist


N, M = [int(c) for c in stdin.readline().strip().split(' ')]
board = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N)]

print(solution(N, M, board))