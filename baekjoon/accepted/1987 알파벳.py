from sys import stdin


def solution(R, C, board):
    DELTA = ((0, 1), (0, -1), (1, 0), (-1, 0))
    alpha_set = set()
    for i in range(R):
        for j in range(C):
            alpha_set.add(board[i][j])
    alpha_dict = {d: i for i, d in enumerate(alpha_set)}
    dp = {}
    def bfs(x, y, visited=set(), alphas=0):
        if (alphas, x, y) in dp:
            return dp[(alphas, x, y)]
        if alphas & 1 << alpha_dict[board[x][y]]:
            return bin(alphas).count('1')
        alphas |= 1 << alpha_dict[board[x][y]]
        score = 0
        for dx, dy in DELTA:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    score = max(score, bfs(nx, ny, visited, alphas))
                    visited.remove((nx, ny))
        alphas &= 2**len(bin(alphas)[2:]) ^ 1 << alpha_dict[board[x][y]]
        dp[(alphas, x, y)] = score
        return score
    return bfs(0,0,{(0,0)})


R, C = [int(c) for c in stdin.readline().strip().split(' ')]
board = [stdin.readline().strip() for _ in range(R)]
print(solution(R, C, board))

"""
2 4
cakb
adlb
"""
