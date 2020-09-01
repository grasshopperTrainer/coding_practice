# slower that dfs stack and time out
from sys import stdin


def solution(R, C, board):
    DELTA = ((0, 1), (0, -1), (1, 0), (-1, 0))
    alpha_dict = {d: False for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    alpha_dict[board[0][0]] = True
    def dfs(x, y, count):
        score = count
        for dx, dy in DELTA:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C:
                if not alpha_dict[board[nx][ny]]:
                    alpha_dict[board[nx][ny]] = True
                    score = max(score, dfs(nx, ny, count+1))
                    alpha_dict[board[nx][ny]] = False
        return score
    return dfs(0, 0, 1)


R, C = [int(c) for c in stdin.readline().strip().split(' ')]
board = [stdin.readline().strip() for _ in range(R)]
print(solution(R, C, board))

"""
2 4
CAKB
ADLQ
"""
