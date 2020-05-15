from sys import stdin

def solution(CN, N, RN, paths):
    RIGHTEND, LEFTEND, NOPATH, MAX, LEFT, RIGHT = -1, 1, 0, 300, -1, 1

    board = [[0] * CN for _ in range(RN)]
    for rn, cn in paths:
        board[rn-1][cn-1] = LEFTEND
        board[rn-1][cn] = RIGHTEND

    # for row in board:
    #     print(row)
    # print()
    def place_bridge(rn, cn, place):
        # print(f'bridging {"right" if place == 1 else "left"}')
        board[rn][cn] = place
        board[rn][cn + place] = -place

    def remove_bridge(rn, cn, place):
        # print(f'removing bridge {"right" if place == 1 else "left"}')
        board[rn][cn] = NOPATH
        board[rn][cn + place] = NOPATH

    def move_right_down(x, y):
        next_pos = x + 1, y + 1
        # print(f'move rightdown from {x,y} to {next_pos}')
        return next_pos

    def move_left_down(x, y):
        next_pos = x + 1, y - 1
        # print(f'move leftdown from {x,y} to {next_pos}')
        return next_pos

    def move_down(x, y):
        next_pos = x + 1, y
        # print(f'move down from {x,y} to {next_pos}')
        return next_pos



    def search(pos, start, num_added):
        # for row in board:
        #     print(row)
        # print()
        rn, cn = pos
        if rn == 0 and start == CN:  # search successfully finished
            # for row in board:
            #     print(row)
            # print()
            return num_added

        if rn == RN:
            if cn == start: # reached good end
                # print(f'switching to next column from {start} to {start+1}')
                return search([0, start + 1], start + 1, num_added)
            else:                        # not a good end
                return MAX

        if num_added > 3 or num_added > N:  # can't add more bridge
            return MAX

        min_added = []
        # there are 5 movements, move right, left, down, bridge right, left
        # print(rn,cn)
        if board[rn][cn] in (LEFTEND, RIGHTEND):   # if bridge met
            if cn < CN-1 and board[rn][cn+1] == RIGHTEND:   # move right
                min_added.append(search(move_right_down(rn,cn), start, num_added))
            elif cn > 0 and board[rn][cn-1] == LEFTEND:    # move left
                min_added.append(search(move_left_down(rn,cn), start, num_added))

        else:   # if no bridge, move down or build one
            if num_added < N:
                if cn == CN-2 or (cn < CN-2 and board[rn][cn+1] == NOPATH):
                    place_bridge(rn, cn, RIGHT)
                    min_added.append(search(move_right_down(rn, cn), start, num_added+1))
                    remove_bridge(rn, cn, RIGHT)
                if cn == 1 or (cn > 1 and board[rn][cn-1] == NOPATH):
                    place_bridge(rn, cn, LEFT)
                    min_added.append(search(move_left_down(rn, cn), start, num_added+1))
                    remove_bridge(rn, cn, LEFT)

            min_added.append(search(move_down(rn, cn), start, num_added))

        return min(min_added)

    result = search([0, 0], 0, 0)
    if result == MAX:
        return -1
    return result


N, M, H, paths = 0, 0, 0, []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, M, H = row
    else:
        paths.append(row)

print(solution(N, M, H, paths))
