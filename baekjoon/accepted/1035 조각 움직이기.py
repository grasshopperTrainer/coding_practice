from sys import stdin
from collections import deque


def solution(board):
    DELTA = (0, 1), (0, -1), (1, 0), (-1, 0)
    N = 5

    poses = []
    num_pieces = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == '*':
                num_pieces += 1
                poses.append((x, y))

    if len(poses) == 1:
        return 0

    def search(n, board, poses, count_sum):
        if n == len(poses):
            # if all moved, check if all are connected
            sx, sy = 0, 0
            for x in range(N):
                for y in range(N):
                    if board[x][y] == '*':
                        sx, sy = x, y
                        break
            # bfs
            count = 1
            visited = [[False]*N for _ in range(N)]
            visited[sx][sy] = True
            que = deque([(sx, sy)])
            while que:
                x, y = que.popleft()
                for dx, dy in DELTA:
                    nx, ny = x+dx, y+dy
                    # check only near pieces
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '*' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        count += 1
                        que.append((nx, ny))
            # if is all connected return summed count else null
            if count == len(poses):
                return count_sum
            return float('inf')
        else:
            # check all possible moves of current piece
            sx, sy = poses[n]
            visited = [[False]*N for _ in range(N)]
            # for not moving current piece
            min_count = search(n+1, board, poses, count_sum)
            visited[sx][sy] = True
            que = deque([(sx, sy, 0)])
            while que:
                x, y, c = que.popleft()
                for dx, dy in DELTA:
                    nx, ny = x+dx, y+dy
                    # if moving to is empty and not visited
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        que.append((nx, ny, c+1))
                        # mark unmark for next search
                        board[sx][sy] = '.'
                        board[nx][ny] = '*'
                        min_count = min(min_count, search(n+1, board, poses, count_sum + c+1))
                        board[sx][sy] = '*'
                        board[nx][ny] = '.'

            return min_count

    return search(0, board, poses, 0)


board = [list(stdin.readline().strip()) for _ in range(5)]
print(solution(board))

"""
.....
.....
..**.
.***.
.....
"""
"""
.....
.....
.*...
.....
*...*
"""
"""
.....
.....
.....
.....
....*
"""
"""
*....
.....
.....
.....
....*
"""