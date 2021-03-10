from sys import stdin


def solution(R, C, board):
    DELTA = (-1, -1), (-1, +1)
    dp = [[[0,0] for _ in range(C)] for _ in range(R)]
    
    max_size = 0
    for x in range(R):
        for y in range(C):
            if board[x][y] == '1':
                dp[x][y] = [1,1]
                for i, (dx, dy) in enumerate(DELTA):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx and 0 <= ny < C:
                        if board[nx][ny] == '1':
                            dp[x][y][i] += dp[nx][ny][i]
            for i in range(min(dp[x][y])-1, -1, -1):
                left, right = dp[x-i][y-i], dp[x-i][y+i]
                size = i+1
                if size <= left[1] and size <= right[0]:
                    max_size = max(max_size, i+1)
                    break
    return max_size


R, C = map(lambda x: int(x), stdin.readline().strip().split(' '))
board = []
for _ in range(R):
    board.append(stdin.readline().strip())

print(solution(R, C, board))