from sys import stdin
import copy

EMPTY, BLOCK = 0, 1
N, M = 6, 4


def get_block_coord(typ, origin):
    if typ == 1:
        return [origin]
    elif typ == 2:
        return [origin, [origin[0], origin[1] + 1]]
    else:
        return [origin, [origin[0] + 1, origin[1]]]


def rotate_block_coord(coord):
    coord[0][0], coord[0][1], coord[-1][0], coord[-1][1] = coord[0][1], coord[0][0], coord[-1][1], coord[-1][0]
    return coord


def is_vertical(coords):
    return coords[0][0] != coords[-1][0]


def search_top(board, block_coord):
    minx = N - 1
    for _, y in block_coord:
        for x, row in enumerate(board):
            if row[y] == BLOCK:
                minx = min(minx, x - 1)
    return minx


def place_block(board, coords, score):
    x = search_top(board, coords)

    placed_coords = []
    for _, y in reversed(coords):
        board[x][y] = BLOCK
        placed_coords.append((x, y))
        if is_vertical(coords):
            x -= 1

    # check for filled row
    board, score = check_filled_row(board, placed_coords[0][0], 1 + is_vertical(coords), score)
    # check for overflow
    board = check_overflow(board)
    return board, score


def check_filled_row(board, row, count, score):
    for _ in range(count):
        if all(v == BLOCK for v in board[row]):  # filled
            score += 1
            board = pop_row(board, row)
        else:
            row -= 1
    return board, score


def check_overflow(board):
    for _ in range(2):
        if any(board[1][y] == BLOCK for y in range(M)):
            board = pop_row(board, N - 1)
    return board


def pop_row(board, x):
    return [[EMPTY] * M] + board[:x] + board[x + 1:]


def create_new_board():
    return [[EMPTY] * M for _ in range(N)]


def solution(moves):
    score = 0
    gboard, bboard = [create_new_board() for _ in range(2)]
    for typ, x, y in moves:
        gcoord = get_block_coord(typ, [x, y])
        bcoord = rotate_block_coord(copy.deepcopy(gcoord))

        gboard, score = place_block(gboard, gcoord, score)
        bboard, score = place_block(bboard, bcoord, score)

        # # debugger
        # for r, rr in zip(gboard, bboard):
        #     print(r, list(reversed(rr)))
        # print()
    block_count = 0
    for grow, brow in zip(gboard, bboard):
        block_count += sum(grow) + sum(brow)
    return score, block_count


moves = tuple(list(map(int, stdin.readline().strip().split(' '))) for _ in range(int(stdin.readline())))
for a in solution(moves):
    print(a)

"""
9
1 3 3
3 1 3
3 2 3
3 1 3
3 0 3
2 3 0
2 2 1
1 0 0
2 0 2
"""
