from sys import stdin


def solution(R, C, sharks):
    DELTA = ((-1, 0), (0, -1), (1, 0), (0, 1))
    MOVE_DICT = [0, 0, 2, 3, 1]
    board = [[None]*C for _ in range(R)]

    for x, y, s, d, z in sharks:
        board[x-1][y-1] = (MOVE_DICT[d], s, z)

    def catch_shark(col):
        for x in range(R):
            if board[x][col]:
                weigh = board[x][col][2]
                board[x][col] = None
                return weigh
        return 0

    def move_shark():
        moved = {}
        for x in range(R):
            for y in range(C):
                if board[x][y]:
                    # get and reset
                    heading, speed, w = board[x][y]
                    board[x][y] = None
                    # calculate move
                    ori = heading%2
                    bound_size = R*2-2 if ori == 0 else C*2-2
                    nx, ny = x, y
                    for _ in range(speed%bound_size):
                        dx, dy = DELTA[heading]
                        nx, ny = nx+dx, ny+dy
                        if ori == 1:
                            if ny < 0 or ny == C:
                                ny = max(1, min(C-2, ny))
                                heading = (heading+2)%4
                        else:
                            if nx < 0 or nx == R:
                                nx = max(1, min(R-2, nx))
                                heading = (heading+2)%4
                    moved[(nx, ny)] = max(moved.get((nx, ny), (0, 0, 0)), (heading, speed, w), key=lambda x: x[2])
        # place sharks
        for (n, m), shark in moved.items():
            board[n][m] = shark

    weight_sum = 0
    for col in range(C):
        weight_sum += catch_shark(col)
        move_shark()
    return weight_sum


lexer = lambda: [int(c) for c in stdin.readline().strip().split(' ')]
R, C, M = lexer()
sharks = [lexer() for _ in range(M)]
print(solution(R, C, sharks))
