from sys import stdin
from collections import deque


def roll(marbles, delta, board):
    WALL, HOLE = '#', 'O'
    a, b = marbles
    amove, bmove = True, True
    while amove or bmove:
        if amove:
            atemp = a[0] + delta[0], a[1] + delta[1]
            if board[atemp[0]][atemp[1]] == HOLE:
                amove = False
                a = atemp
            elif board[atemp[0]][atemp[1]] == WALL:
                amove = False
            else:
                a = atemp
        if bmove:
            btemp = b[0] + delta[0], b[1] + delta[1]
            if btemp == a:
                if board[a[0]][a[1]] == HOLE:
                    b = btemp
                bmove = False
            elif board[btemp[0]][btemp[1]] == HOLE:
                bmove = False
                b = btemp
            elif board[btemp[0]][btemp[1]] == WALL:
                bmove = False
            else:
                b = btemp
    return a, b


def solution(ROW, COL, board):
    DELTA = ((-1, 0), (0, -1), (1, 0), (0, 1))
    WALL, HOLE = '#', 'O'
    rpos, bpos = None, None
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == 'R':
                rpos = (r, c)
            elif board[r][c] == 'B':
                bpos = (r, c)

    que = deque([(rpos, bpos, 0, -1)])  # marble pos, move count, last move
    while que:
        rpos, bpos, count, last = que.popleft()
        if count == 10:
            break
        for next_move in range(4):
            if (last - next_move) % 2 == 1 or last == -1:  # initial or go perpendicular
                delta = DELTA[next_move]
                # check which precede and simulate movement
                if (delta[0] and rpos[0] * delta[0] >= bpos[0] * delta[0]) or (delta[1] and rpos[1] * delta[1] >= bpos[1] * delta[1]):
                    marbles = [rpos, bpos]
                    r, b = roll(marbles, delta, board)
                else:
                    marbles = [bpos, rpos]
                    b, r = roll(marbles, delta, board)

                asign, bsign = board[r[0]][r[1]], board[b[0]][b[1]]
                if asign == HOLE:
                    if bsign == HOLE:
                        continue
                    else:
                        return count + 1
                elif bsign == HOLE:
                    continue
                if r != rpos or b != bpos:
                    que.append((r, b, count + 1, next_move))
    return -1


R, C = [int(c) for c in stdin.readline().strip().split(' ')]
board = []
for _ in range(R):
    board.append(stdin.readline().strip())
print(solution(R, C, board))

"""
4 7
#######
##....#
#ORB#.#
#######
"""
"""
3 7
#######
#BO..R#
#######
"""
"""
4 7
#######
#R....#
##.OB##
#######
"""
"""
4 7
#######
#.....#
##ROB##
#######
"""
"""
5 7
#######
#R....#
#..O..#
#....B#
#######
"""
"""
6 9
#########
#R......#
#.O.....#
#.......#
#......B#
#########
"""
"""
10 10
##########
#R#...##.#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#..BO#.#
#.#.#.#..#
#...#.##.#
##########
"""
"""
5 5
#####
#O..#
#R..#
#B..#
#####
"""
