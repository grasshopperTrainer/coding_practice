from sys import stdin
import heapq


def solution(W, H, board):
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)
    CLEAN, DIRTY, FURN, ROBOT = '.*xo'

    robot = None
    dirts = 0
    for x in range(H):
        for y in range(W):
            if board[x][y] == ROBOT:
                robot = (x, y)
                board[x][y] = CLEAN  # not to disturb searching
            elif board[x][y] == DIRTY:  # give id to a robot
                board[x][y] = dirts
                dirts += 1

    # number of dirt patterns
    dirt_full = 2 ** dirts
    # move count for each cleaned dirt pattern
    record = [[[float('inf')] * dirt_full for _ in range(W)] for _ in range(H)]
    moves = [(0, 0, *robot)]  # move count, dirt clean count, pos
    while moves:
        move_cnt, dirt_mask, x, y = heapq.heappop(moves)
        # return if all cleaned
        if dirt_mask + 1 == dirt_full:
            return move_cnt
        # if reachable with less move count, this sub path has no chance to become bin path
        if record[x][y][dirt_mask] <= move_cnt:
            continue
        record[x][y][dirt_mask] = move_cnt

        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != FURN:
                if board[nx][ny] != CLEAN:  # not a furniture but not a clean either -> dirt
                    new_dirt_mask = dirt_mask | (1 << board[nx][ny])  # mark as cleaned
                    heapq.heappush(moves, (move_cnt + 1, new_dirt_mask, nx, ny))
                else:
                    heapq.heappush(moves, (move_cnt + 1, dirt_mask, nx, ny))
    return -1


while True:
    W, H = tuple(map(int, stdin.readline().strip().split(' ')))
    if (W, H) == (0, 0):
        break
    board = [list(stdin.readline().strip()) for _ in range(H)]

    print(solution(W, H, board))

"""
7 5
.......
.o...*.
.......
.*...*.
.......
0 0
"""
