from sys import stdin
import copy

SHARK = -1
EMPTY = (0, 0)
EATEN = None
DELTA = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
N = 4


def solution(board):
    fishes = [None for _ in range(17)]
    for x in range(N):
        for y in range(N):
            fishes[board[x][y][0]] = (x, y)
    return search(board, fishes, (0, 0), 0)


def search(board, fishes, shark, score):
    x, y = shark

    # need new record
    new_board, new_fishes = copy.deepcopy(board), copy.deepcopy(fishes)
    # shark catch fish -> erase fish
    fish, move_dir = new_board[x][y]
    new_fishes[fish] = EATEN

    # add score and set high
    score += fish
    high_score = score

    # simulate fish
    move_fishes(new_board, new_fishes, shark)

    # gonna move shark so set shark position empty
    new_board[x][y] = EMPTY

    # move shark
    offset = 0
    dx, dy = DELTA[move_dir - 1]
    while True:
        offset += 1
        nx, ny = x + dx * offset, y + dy * offset
        if 0 <= nx < N and 0 <= ny < N:
            if new_board[nx][ny] != EMPTY:  # can't move into empty pos, take next offset
                high_score = max(high_score, search(new_board, new_fishes, (nx, ny), score))
        else:  # off bound, nowhere to move on
            break
    return high_score


def move_fishes(board, fishes, shark):
    for afish in range(1, 17):  # simulate all fishes
        if fishes[afish] == EATEN:
            continue
        x, y = fishes[afish]

        _, od = board[x][y]
        td = od - 1  # temp delta, original delta
        while True:
            dx, dy = DELTA[td]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) != shark:
                # if empty
                if board[nx][ny] == EMPTY:
                    bfish = 0  # just use trash index
                else:
                    bfish = board[nx][ny][0]  # else, swapping fish is
                # swap
                board[x][y], board[nx][ny] = board[nx][ny], (afish, td + 1)  # td + 1 for index correction
                fishes[afish], fishes[bfish] = (nx, ny), (x, y)
                break  # once swapped, sim for the fish done
            else:
                td = (td + 1) % 8  # % for rotation
                # all directions checked, nowhere to go
                if td == od - 1:
                    break


board = []
for _ in range(4):
    nums = list(map(int, stdin.readline().strip().split(' ')))
    row = [(i, j) for i, j in zip(nums[0:8:2], nums[1:8:2])]
    board.append(row)

print(solution(board))
