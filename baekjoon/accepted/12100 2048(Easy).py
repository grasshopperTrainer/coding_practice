# improved by replacing 2d board into 1d

import sys
from itertools import product
from collections import deque

def solution(N, board_ori):

    EMPTY = 0
    # tried slicing but couldn't find a way to include index 0 when negative stepping
    INDICES = [[list(range(N*i, N*(i+1))) for i in range(N)],
              [list(range(N*(i+1)-1, N*i-1, -1)) for i in range(N)],
              [list(range(i, N*N, N)) for i in range(N)],
              [list(range(N*N-i-1, -1, -N)) for i in range(N)]]

    board = tuple(board_ori)
    visited = {board}
    status = [board]

    for _ in range(5):
        new_status = []
        for board, indices in product(status, INDICES):
            new_board = [EMPTY]*N*N
            for idxs in indices:
                vals = deque([board[i] for i in idxs if board[i] != EMPTY])

                if not vals:
                    continue

                merged = [vals.popleft()]
                is_just_joined = False
                while vals:
                    val = vals.popleft()
                    if merged[-1] == val and not is_just_joined:
                        merged[-1] *= 2
                        is_just_joined = True
                        continue
                    merged.append(val)
                    is_just_joined = False

                merged += [EMPTY] * (N - len(merged))
                for i, val in zip(idxs, merged):
                    new_board[i] = val

            tuple_board = tuple(new_board)
            if tuple_board not in visited:
                visited.add(tuple_board)
                new_status.append(new_board)

        if not new_status:
            break
        status = new_status
        # for s in status:
        #     for i in range(N):
        #         print(s[N*i:N*(i+1)])
        #     print()
        # print('________')


    return max(max(s) for s in status)

# N = 4
# board = [[2,4,4,8],[2,0,0,0],[4,0,0,0],[8,2,4,8]]
# N = 5
# board = [[0,0,2,0,0],[0,0,0,0,0],[2,0,2,0,2],[0,0,0,0,0],[0,0,2,0,0]]
# N = 2
# board = [[0, 0], [0, 0]]
# N = 3
# board = [[2,0,2],[0,2,0],[2,0,2]]
# for row in board:
#     print(row)
# print()

N, board = 0, []
for i, row in enumerate(sys.stdin.readlines()):
    if i == 0:
        N = int(row)
        continue
    board += list(map(int, row.strip().split(' ')))

print(solution(N, board))