from sys import stdin


def solution(R, C, board):
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)
    EMPTY, VERT, HORI, CROSS, LEFT_DOWN, LEFT_UP, RIGHT_UP, RIGHT_DOWN = '.|-+1234'

    def define_missing(x, y, direction):
        goable = []
        for new_dir in (direction, (direction - 1) % 4, (direction + 1) % 4):
            dx, dy = DELTA[new_dir]
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != EMPTY:
                if new_dir == 0:
                    if board[nx][ny] in (VERT, LEFT_DOWN, RIGHT_DOWN, CROSS):
                        if new_dir == direction:
                            goable.append(VERT)
                        elif direction == 1:
                            goable.append(LEFT_UP)
                        elif direction == 3:
                            goable.append(RIGHT_UP)
                        # goable.append(new_dir)
                elif new_dir == 2:
                    if board[nx][ny] in (VERT, LEFT_UP, RIGHT_UP, CROSS):
                        if new_dir == direction:
                            goable.append(VERT)
                        elif direction == 1:
                            goable.append(LEFT_DOWN)
                        elif direction == 3:
                            goable.append(RIGHT_DOWN)
                        # goable.append(new_dir)
                elif new_dir == 1:
                    if board[nx][ny] in (HORI, LEFT_DOWN, LEFT_UP, CROSS):
                        if new_dir == direction:
                            goable.append(HORI)
                        elif direction == 0:
                            goable.append(RIGHT_DOWN)
                        elif direction == 2:
                            goable.append(RIGHT_UP)
                        # goable.append(new_dir)
                elif new_dir == 3:
                    if board[nx][ny] in (HORI, RIGHT_UP, RIGHT_DOWN, CROSS):
                        if new_dir == direction:
                            goable.append(HORI)
                        elif direction == 0:
                            goable.append(LEFT_DOWN)
                        elif direction == 2:
                            goable.append(LEFT_UP)
                        # goable.append(new_dir)
        if len(goable) == 3:
            return CROSS
        return goable[0]

    def find_next_dir(direction, block):
        if block == VERT:
            return direction
        elif block == HORI:
            return direction
        elif block == LEFT_DOWN:
            if direction == 0:
                return 3
            elif direction == 1:
                return 2
        elif block == LEFT_UP:
            if direction == 1:
                return 0
            elif direction == 2:
                return 3
        elif block == RIGHT_UP:
            if direction == 3:
                return 0
            elif direction == 2:
                return 1
        elif block == RIGHT_DOWN:
            if direction == 3:
                return 2
            elif direction == 0:
                return 1
        elif block == CROSS:
            return direction

    zagreb, moscow = None, None
    for x in range(R):
        for y in range(C):
            if board[x][y] == 'M':
                moscow = (x, y)
            elif board[x][y] == 'Z':
                zagreb = (x, y)

    # find inid dir
    init_stat = None
    for i, (dx, dy) in enumerate(DELTA):
        nx, ny = moscow[0] + dx, moscow[1] + dy
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != EMPTY:
            init_stat = nx, ny, find_next_dir(i, board[nx][ny])  # *pos, dir

    move = init_stat
    while True:
        x, y, direction = move
        if (x, y) == zagreb:
            break

        dx, dy = DELTA[direction]
        nx, ny = x + dx, y + dy
        if board[nx][ny] == EMPTY:  # missing
            missing = define_missing(nx, ny, direction)
            return ' '.join(map(str, (nx + 1, ny + 1, missing)))
        else:
            move = nx, ny, find_next_dir(direction, board[nx][ny])
            if board[nx][ny] == CROSS:
                if direction % 2 == 0:
                    board[nx][ny] = HORI
                else:
                    board[nx][ny] = VERT


R, C = map(int, stdin.readline().strip().split(' '))
board = [list(stdin.readline().strip()) for _ in range(R)]
print(solution(R, C, board))
