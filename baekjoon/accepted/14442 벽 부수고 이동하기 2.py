from sys import stdin
from collections import deque


def solution(N, M, K, board):
    EMPTY = '0'

    visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]

    que = deque()
    que.append((0, 0, 0, 0))
    visited[0][0][0] = True
    while que:
        x, y, through_count, move_count = que.popleft()
        if (x, y) == (N - 1, M - 1):
            return move_count + 1
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == EMPTY and not visited[nx][ny][through_count]:
                    for i in range(through_count, K+1):
                        visited[nx][ny][i] = True
                    que.append((nx, ny, through_count, move_count + 1))
                elif board[nx][ny] != EMPTY and through_count + 1 <= K and not visited[nx][ny][through_count + 1]:
                    for i in range(through_count+1, K+1):
                        visited[nx][ny][i] = True
                    que.append((nx, ny, through_count + 1, move_count + 1))
    return -1


N, M, K = map(int, stdin.readline().strip().split(' '))
board = [stdin.readline().strip() for _ in range(N)]

print(solution(N, M, K, board))
