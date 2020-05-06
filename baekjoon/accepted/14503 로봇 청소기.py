from sys import stdin

def solution(N, M, facing, robot, board):
    DIRTY, WALL, CLEAN = 0, 1, 2
    OFFSETS = (1, M, -1, -M)    # ordered following clockwise rotation
    FACING_OFFSET = dict(zip((1,2,3,0), OFFSETS))

    move = FACING_OFFSET[facing]
    cleaned = 0
    while True:
        if board[robot] == DIRTY:  # current is dirty
            board[robot] = CLEAN
            cleaned += 1

        # nothing to do
        if all([board[robot+off] in (WALL, CLEAN) for off in OFFSETS]):
            behind = robot + OFFSETS[OFFSETS.index(move)-2]
            if board[behind] == WALL:  # can't move back
                break
            else:   # move back
                robot = behind
        else:   # something to do
            move = OFFSETS[OFFSETS.index(move)-1]   # rotate left
            if board[robot+move] == DIRTY:   # move forward if it's dirty
                robot += move

    return cleaned


N, M, facing, robot, board = 0, 0, 0, 0, []
for i, row in enumerate(stdin.readlines()):
    row = list(map(int, row.strip().split(' ')))
    if i == 0:
        N, M = row
    elif i == 1:
        robot, facing = row[0]*M+row[1], row[2]
    else:
        board += list(row)

print(solution(N, M, facing, robot, board))