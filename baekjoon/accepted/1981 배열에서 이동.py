from sys import stdin
import heapq


def solution(N, board):
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)
    goal = (N - 1, N - 1)
    val = board[0][0]
    moves = [(0, val, val, 0, 0)]  # diff, min, max, x, y

    min_val, max_val = float('inf'), 0
    for row in board:
        for val in row:
            min_val = min(min_val, val)
            max_val = max(max_val, val)
    dist = max_val - min_val + 1

    record = [[[float('inf')] * dist for _ in range(N)] for _ in range(N)]
    while moves:
        diff, small, big, x, y = heapq.heappop(moves)
        if (x, y) == goal:
            return diff
        if record[x][y][big-min_val] <= diff:
            continue
        record[x][y][big-min_val] = diff

        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if big < board[nx][ny]:
                    new_big = board[nx][ny]
                    new_diff = new_big - small
                    if new_diff < record[nx][ny][new_big-min_val]:
                        heapq.heappush(moves, (new_diff, small, new_big, nx, ny))
                elif board[nx][ny] < small:
                    new_small = board[nx][ny]
                    new_diff = big - new_small
                    if new_diff < record[nx][ny][big-min_val]:
                        heapq.heappush(moves, (new_diff, new_small, big, nx, ny))
                else:
                    if diff < record[nx][ny][big-min_val]:
                        heapq.heappush(moves, (diff, small, big, nx, ny))


N = int(stdin.readline())
board = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]
print(solution(N, board))


"""
5
1 1 3 6 8
1 2 2 5 5
4 4 2 3 3
8 0 2 3 4
4 3 0 2 1
"""