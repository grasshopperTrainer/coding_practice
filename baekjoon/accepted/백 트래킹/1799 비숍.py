from sys import stdin


def solution(N, board):
    PLACE = '1'
    dia1, dia2 = [[True for _ in range(N*2-1)] for _ in range(2)]
    # search
    def dfs(x, y, count):
        if x == N:
            return count
        if y >= N:
            return dfs(x+1, (y+1)%2, count)             # shifting to step on designated color
        max_c = 0
        if board[x][y] == PLACE and dia1[x+y] and dia2[x-y]:
            dia1[x+y] = False
            dia2[x-y] = False
            max_c = max(max_c, dfs(x, y+2, count+1))    # place here
            dia1[x+y] = True
            dia2[x-y] = True
            max_c = max(max_c, dfs(x, y+2, count))      # do not place here
        else:
            max_c = max(max_c, dfs(x, y+2, count))      # can't place, move on
        return max_c
    return dfs(0,0,0) + dfs(0,1,0)


N = int(stdin.readline())
board = [stdin.readline().strip().split(' ') for _ in range(N)]
print(solution(N, board))