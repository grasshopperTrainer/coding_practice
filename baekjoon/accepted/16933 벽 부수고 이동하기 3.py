# time out
from sys import stdin
from collections import deque


def solution(N, M, K, board):
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)
    EMPTY, WALL = '0', '1'
    DAY = True

    target = N - 1, M - 1
    record = [[[[float('inf')] * (K + 1) for _ in range(2)] for _ in range(M)] for _ in range(N)]
    moves = deque([(1, 0, DAY, 0, 0)])  # move count, destroy count, day, x, y
    counts = 0
    while moves:
        counts += 1
        move_cnt, through_cnt, day, x, y = moves.popleft()
        if (x, y) == target:
            return move_cnt

        if record[x][y][day][through_cnt] <= move_cnt:
            continue
        record[x][y][day][through_cnt] = move_cnt

        waiting = False
        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == EMPTY:
                    if move_cnt + 1 < record[nx][ny][not day][through_cnt]:
                        moves.append((move_cnt + 1, through_cnt, not day, nx, ny))
                else:
                    if day:
                        if through_cnt + 1 <= K and move_cnt + 1 < record[nx][ny][not day][through_cnt + 1]:
                            moves.append((move_cnt + 1, through_cnt + 1, not day, nx, ny))
                    else:  # night but near has wall, try wait
                        if not waiting and move_cnt + 1 < record[x][y][not day][through_cnt]:
                            moves.append((move_cnt + 1, through_cnt, not day, x, y))
                            waiting = True
    return -1


N, M, K = tuple(map(int, stdin.readline().strip().split(' ')))
board = [stdin.readline().strip() for _ in range(N)]
print(solution(N, M, K, board))

# N, M, K = 1000, 1000, 1
# board = ['0'*1000 for _ in range(1000)]

"""
1 4 2
0110
"""
"""
10 10 1
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
"""
