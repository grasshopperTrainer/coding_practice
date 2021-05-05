# bad solution

from sys import stdin, setrecursionlimit

setrecursionlimit(1000_000)


def solution(N, board):
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)
    DOOR, EMPTY, MIRROR, WALL = '#.!*'
    NOMIRROR, SLASH, BACKSLASH = 0, 1, 2

    def next_dir(mirror_pos, direction):
        if mirror_pos == SLASH:
            if direction in (1, 3):
                return (direction + 1) % 4
            else:
                return (direction - 1) % 4
        if mirror_pos == BACKSLASH:
            if direction in (0, 2):
                return direction + 1
            else:
                return direction - 1

    def search(mirrors, build, direction, visited, x, y):
        if visited[x][y][direction]:
            return float('inf')
        visited[x][y][direction] = True

        if (x, y) == doors[1]:
            return mirrors

        min_count = float('inf')
        dx, dy = DELTA[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != WALL:
            # go as was going
            min_count = min(min_count, search(mirrors, build, direction, visited, nx, ny))
            # if mirror, stir
            if board[nx][ny] not in (EMPTY, WALL, DOOR):  # mirror id
                mid = board[nx][ny]
                if build[mid] == SLASH:
                    min_count = min(min_count, search(mirrors, build, next_dir(SLASH, direction), visited, nx, ny))
                elif build[mid] == BACKSLASH:
                    min_count = min(min_count, search(mirrors, build, next_dir(BACKSLASH, direction), visited, nx, ny))
                else:  # place new mirror
                    build[mid] = SLASH
                    min_count = min(min_count, search(mirrors + 1, build, next_dir(SLASH, direction), visited, nx, ny))
                    build[mid] = NOMIRROR

                    build[mid] = BACKSLASH
                    min_count = min(min_count, search(mirrors + 1, build, next_dir(BACKSLASH, direction), visited, nx, ny))
                    build[mid] = NOMIRROR
        visited[x][y][direction] = False
        return min_count

    mirrors = 0
    doors = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == DOOR:
                doors.append((x, y))
            elif board[x][y] == MIRROR:
                board[x][y] = mirrors
                mirrors += 1

    # find initial direction
    x, y = doors[0]
    direction = None
    for i, (dx, dy) in enumerate(DELTA):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != WALL:
            direction = i
            break

    visited = [[[False] * 4 for _ in range(N)] for _ in range(N)]  # for each direction
    return search(0, [NOMIRROR] * mirrors, direction, visited, x, y)


N = int(stdin.readline())
board = [list(stdin.readline().strip()) for _ in range(N)]
print(solution(N, board))

"""
5
***#*
*!.!*
*...*
*!.!*
*#***
"""