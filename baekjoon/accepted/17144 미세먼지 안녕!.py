from sys import stdin


def get_upper_path(ox, oy, R, C):
    path = []
    for y in range(1, C):
        path.append((ox, y))
    for x in range(ox - 1, -1, -1):
        path.append((x, C - 1))
    for y in range(C - 2, -1, -1):
        path.append((0, y))
    for x in range(1, ox):
        path.append((x, 0))
    return path


def get_lower_path(ox, oy, R, C):
    path = []
    for y in range(1, C):
        path.append((ox, y))
    for x in range(ox + 1, R):
        path.append((x, C - 1))
    for y in range(C - 2, -1, -1):
        path.append((R - 1, y))
    for x in range(R - 2, ox, -1):
        path.append((x, 0))
    return path


def solution(R, C, T, board):
    cleaner = []
    for x in range(R):
        for y in range(C):
            if board[x][y] == -1:
                cleaner.append((x, y))

    upper_path = get_upper_path(*cleaner[0], R, C)
    lower_path = get_lower_path(*cleaner[1], R, C)

    for _ in range(T):
        # diffuse
        new_board = [[0] * C for _ in range(R)]
        for x in range(R):
            for y in range(C):
                if (x, y) in cleaner or board[x][y] == 0:
                    continue

                diff_count = 0
                diff_val = board[x][y] // 5
                for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in cleaner:
                        new_board[nx][ny] += diff_val
                        diff_count += 1
                new_board[x][y] += board[x][y] - diff_count * diff_val
        board = new_board

        # circulate
        for i in range(len(upper_path)-1, 0, -1):
            nx, ny = upper_path[i]
            x, y = upper_path[i-1]
            board[nx][ny] = board[x][y]
        board[upper_path[0][0]][upper_path[0][1]] = 0  # clean first place

        for i in range(len(lower_path)-1, 0, -1):
            nx, ny = lower_path[i]
            x, y = lower_path[i-1]
            board[nx][ny] = board[x][y]
        board[lower_path[0][0]][lower_path[0][1]] = 0  # clean first place

    return sum(sum(row) for row in board)


R, C, T = map(int, stdin.readline().strip().split(' '))
board = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(R)]
print(solution(R, C, T, board))
