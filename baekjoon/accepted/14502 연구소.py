from sys import stdin
from itertools import combinations
from collections import deque


def solution(N, M, board):
    NM = N * M
    EMPTY, WALL, VIRUS = 0, 1, 2
    WALLABLE, VIRUS_AT = [], []
    for i, v in enumerate(board):
        if v == VIRUS:
            VIRUS_AT.append(i)
        elif v == EMPTY:
            WALLABLE.append(i)
    NUMWALLS = board.count(WALL) + 3
    OFFSETS = (1, -1, M, -M)

    high_survive = 0
    for new_walls in map(set, combinations(WALLABLE, 3)):
        infected = {*VIRUS_AT}
        que = deque(VIRUS_AT)
        while que:
            virus = que.popleft()
            for off in OFFSETS:
                t_virus = virus + off
                if 0 <= t_virus < NM and (abs(off) != 1 or t_virus // M == virus // M):
                    if t_virus not in infected and t_virus not in new_walls and board[t_virus] == EMPTY:
                        infected.add(t_virus)
                        que.append(t_virus)
        high_survive = max([high_survive, NM - NUMWALLS - len(infected)])

    return high_survive


N, M, board = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N, M = map(int, row.strip().split(' '))
        continue
    board += list(map(int, row.strip().split(' ')))

print(solution(N, M, board))
