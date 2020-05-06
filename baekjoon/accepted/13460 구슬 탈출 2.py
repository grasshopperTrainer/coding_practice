import sys
from collections import deque
from functools import reduce


WALL, RED, BLUE, HOLE, EXIT = '#', 'R', 'B', 'O', (-1, -1)
N, M = 0, 0
red, blue = None, None
board = []
for i, row in enumerate(sys.stdin.readlines()):
    if i == 0:
        N, M = list(map(int, row.strip().split(' ')))
        continue

    board.append(list(row.strip()))
    if RED in row:
        red = i - 1, row.find(RED)
    if BLUE in row:
        blue = i - 1, row.find(BLUE)

def move(coord, delta):
    return coord[0] + delta[0], coord[1] + delta[1]

def get_ahead(coord, delta):
    return board[coord[0] + delta[0]][coord[1] + delta[1]]

def get_current(coord):
    return board[coord[0]][coord[1]]

visited = {(red, blue)}
movements = [(red, blue)] # R pos , B pos
DELTA = ((0,-1), (0,1), (-1,0), (1,0))    # left, right, up, down
for attempt in range(1, 11):
    new_movements = []
    for red, blue in movements:
        for delta in DELTA:
            t_red, t_blue = red[:], blue[:]
            while True: # move red
                if get_current(t_red) == HOLE:
                    t_red = EXIT
                    break
                elif get_ahead(t_red, delta) == WALL:
                    break
                elif move(t_red, delta) == t_blue:
                    if get_ahead(t_blue, delta) == HOLE:
                        t_blue = EXIT
                        t_red = EXIT
                        break
                    elif get_ahead(t_blue, delta) != WALL:
                        t_blue = move(t_blue, delta)
                        t_red = move(t_red, delta)
                    else:
                        break
                else:
                    t_red = move(t_red, delta)

            while True: # move blue
                if t_blue == EXIT:
                    break
                if get_ahead(t_blue, delta) == HOLE:
                    t_blue = EXIT
                elif get_ahead(t_blue, delta) == WALL or move(t_blue, delta) == t_red:
                    break
                else:
                    t_blue = move(t_blue, delta)

            if t_red == EXIT and t_blue != EXIT:
                print(attempt)
                exit()

            elif (t_red, t_blue) not in visited and t_red != t_blue != EXIT:
                visited.add((t_red, t_blue))
                new_movements.append([t_red, t_blue])

    movements = new_movements
    if not movements:
        break

print(-1)

"""
5 5
#####
#R..#
#.O.#
#..B#
#####
3 4
#####
#...#
#.R.#
#.B.#
#.O.#
#...#
#####
"""