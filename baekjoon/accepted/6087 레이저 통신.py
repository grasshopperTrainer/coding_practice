from sys import stdin
import heapq


def solution(W, H, board):
    EMPTY, WALL, TARGET = '.', '*', 'C'
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)

    targets = []
    for x in range(H):
        for y in range(W):
            if board[x][y] == TARGET:
                targets.append((x, y))

    moves = []
    for i, (dx, dy) in enumerate(DELTA):
        nx, ny = targets[0][0] + dx, targets[0][1] + dy
        if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != WALL:
            moves.append((0, i, nx, ny))

    record = [[float('inf')] * W for _ in range(H)]
    while True:
        count, heading, x, y = heapq.heappop(moves)
        if (x, y) == targets[1]:
            return count
        
        if record[x][y] < count:
            continue
        record[x][y] = count

        for i, (dx, dy) in enumerate(DELTA):
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != WALL:
                if heading == i:
                    heapq.heappush(moves, (count, i, nx, ny))
                else:
                    heapq.heappush(moves, (count + 1, i, nx, ny))


W, H = tuple(map(int, stdin.readline().strip().split(' ')))
board = [tuple(stdin.readline().strip()) for _ in range(H)]

print(solution(W, H, board))

"""
5 5
C**..
.*...
...*.
***..
C....
"""
"""
5 5
.....
.***.
.C*C.
..*..
..*..
"""
"""
5 6
....C
.***.
...*.
**...
*C*.*
.....
"""
"""
5 4
.*...
.*C*.
.C*..
.....
"""