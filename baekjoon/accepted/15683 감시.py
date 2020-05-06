from sys import stdin
import itertools



def solution(N, M, board):
    WALL, CCTV, OBSERVING, EMPTY = 'W', 'C', '1', 0

    # build 2D array representing cctv states
    # described as bitwise patterns indicating observation on each side
    OBSERV_PATTERN, ROTATIONS = ['1000', '1010', '1100', '1110', '1111'], [4, 2, 4, 4, 1]
    CCTVS = [[] for _ in range(5)]
    for i, (observe, num_rotations) in enumerate(zip(OBSERV_PATTERN, ROTATIONS)):
        for rotation in range(num_rotations):
            CCTVS[i].append(observe[rotation:] + observe[:rotation])

    # function for marking board
    def mark(rn, cn, cctv, sign):
        newly_marked = 0
        # observation indication and delta of next index
        for o, d in zip(cctv, ((0, 1), (-1, 0), (0, -1), (1, 0))):
            if o == OBSERVING:
                trn, tcn = rn, cn
                while 0 <= trn < N and 0 <= tcn < M and board[trn][tcn] != WALL:
                    if board[trn][tcn] != CCTV:
                        # check newly mark, unmark
                        if (board[trn][tcn], sign) in ((0, 1), (1, -1)):
                            newly_marked += 1
                        board[trn][tcn] += sign

                    trn, tcn = trn + d[0], tcn + d[1]

        return newly_marked

    empty = 0
    cctvs = []
    # format board and check cctvs, empty space
    for rn, cn in itertools.product(range(N), range(M)):
        v = board[rn][cn]
        if v == EMPTY:
            empty += 1
        elif v == 6:
            board[rn][cn] = WALL
        else:
            cctvs.append((rn, cn, board[rn][cn]-1))
            board[rn][cn] = CCTV
    cctvs.sort(key=lambda x: x[2], reverse=True)    # heuristic

    def search(cctv_idx, dead_zones):
        if dead_zones == 0:
            return 0
        if cctv_idx == len(cctvs):
            return dead_zones

        rn, cn, cctv_kind = cctvs[cctv_idx]
        min_space = dead_zones
        for cctv in CCTVS[cctv_kind]:
            dead_zones -= mark(rn, cn, cctv, 1)
            min_space = min([min_space, search(cctv_idx + 1, dead_zones)])
            dead_zones += mark(rn, cn, cctv, -1)
        return min_space

    return search(0, empty)


N, M, board = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    row = [int(v) for v in row.strip().split(' ')]
    if i == 0:
        N, M = row
    else:
        board.append(row)

print(solution(N, M, board))