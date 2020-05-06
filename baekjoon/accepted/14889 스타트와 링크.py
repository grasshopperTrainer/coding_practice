from sys import stdin
from itertools import combinations


def solution(N, board):
    min_gap = 2000
    plyrs = set(range(N))
    wildcard = 0  # to avoid populating same team
    for team_a in combinations(range(1,N), N//2-1):
        team_a = (*team_a, wildcard)  # add wildcard to the team
        teams = (team_a, tuple(plyrs - set(team_a)))
        gap = 0
        for i, team in zip((1,-1), teams):
            for plyr in team:
                # no need to bother playing with one himself as it always results 0
                for plying_with in team:
                    gap += board[plyr][plying_with]*i

        min_gap = min([min_gap, abs(gap)])

    return min_gap


N, board = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
        continue
    board.append(list(map(int, row.strip().split(' '))))

print(solution(N, board))