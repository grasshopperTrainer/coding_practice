from sys import stdin


def solution(board):
    N = 10
    DELTA = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
    OFF, ON = '#', 'O'

    def turn_switch(x, y, board):
        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = ON if board[nx][ny] == OFF else OFF

    for mask in range(2 ** N):
        search_board = [list(row) for row in board]
        turn_count = 0
        for y in range(N):
            if mask & 1 << y:
                turn_count += 1
                turn_switch(0, y, search_board)
        # look through rest of rows
        for x in range(1, N):
            for y in range(N):
                if search_board[x - 1][y] == ON:
                    turn_count += 1
                    turn_switch(x, y, search_board)

        if all(map(lambda x: x == OFF, search_board[-1])):
            return turn_count
    return -1


print(solution([stdin.readline().strip() for _ in range(10)]))
