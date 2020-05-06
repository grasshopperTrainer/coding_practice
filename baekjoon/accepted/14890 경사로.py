from sys import stdin
from collections import deque

def solution(N, L, board):

    def roads(board):   # generator returning horizontal, vertical roads
        cols = [[] for _ in range(len(board))]
        for rn, row in enumerate(board):
            for cn, v in enumerate(row):
                cols[cn].append(v)
            yield row

        for col in cols:
            yield col

    path_count = 0
    for road in roads(board):
        road, passed = deque(road), deque()
        passed.append(road.popleft())

        while road:
            next_seg, last_seg = road[0], abs(passed[-1])
            # going flat
            if next_seg == last_seg:    # no bridge needed
                passed.append(road.popleft())
                continue

            # going high
            if len(passed) >= L and all((passed[-(i+1)] == next_seg - 1 for i in range(L))):
                passed.append(road.popleft())
                continue

            # going low
            if len(road) >= L and all((road[i] == last_seg - 1 for i in range(L))):
                for _ in range(L):
                    passed.append(-road.popleft())   # negate to mark bridge built
                continue

            # else, can't build bridge
            break
        else:   # if all road is moved to passed, mark good path
            path_count += 1

    return path_count



N, L = None, None
board = []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N, L = (int(c) for c in row.strip().split(' '))
    else:
        board.append([int(c) for c in row.strip().split(' ')])

print(solution(N, L, board))

