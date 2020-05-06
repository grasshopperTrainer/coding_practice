from sys import stdin
from collections import deque

def solution(N, M, dice, board, moves):
    EAST, WEST, NORTH, SOUTH = 1, 2, 3, 4
    inst = {EAST:(1, 0, slice(3,6), (0,1)),
            WEST:(-1, -1, slice(3,6), (0,-1)),
            NORTH:(-1, -1, slice(1,None,3), (-1,0)),
            SOUTH:(1, 0, slice(1,None,3), (1,0))}   # rotation, replace, slice, offset
    dice_map = [0]*9
    dice_btm = 0

    for m in moves:
        rot, rep, slc, off = inst[m]
        t_dice = [sum(i) for i in zip(dice, off)]
        if all([0 <= c < l for c, l in zip(t_dice,(N,M))]):
            dice = t_dice
            vals = deque(dice_map[slc])
            vals.rotate(rot)

            new_bottom = vals[rep]
            vals[rep] = dice_btm
            dice_btm = new_bottom

            dice_map[slc] = vals

            if board[dice[0]][dice[1]] == 0:
                board[dice[0]][dice[1]] = dice_btm
            else:
                dice_btm = board[dice[0]][dice[1]]
                board[dice[0]][dice[1]] = 0

            print(dice_map[4])

N, M, dice, board, moves = 0, 0, [0,0], [], []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N, M, dice[0], dice[1], _ = map(int, row.strip().split(' '))
        continue
    if i <= N:
        board.append(list(map(int, row.strip().split(' '))))
    else:
        moves = tuple(map(int, row.strip().split(' ')))

solution(N, M, dice, board, moves)
