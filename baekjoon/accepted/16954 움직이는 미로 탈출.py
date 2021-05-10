from sys import stdin


def solution(board):
    WALL = '#'
    DELTA = (0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)
    N = 8

    moves = [(N - 1, 0)]  # row offset, x, y
    while True:
        visited = [[False] * N for _ in range(N)]
        new_moves = []
        for x, y in moves:
            if (x, y) == (0, N - 1):
                return 1

            if board[x][y] == WALL:
                continue

            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] != WALL:
                    visited[nx][ny] = True
                    new_moves.append((nx, ny))
        board.pop()
        board.insert(0, '.'*N)

        moves = new_moves
        if not moves:
            return 0


board = [stdin.readline().strip() for _ in range(8)]
print(solution(board))
