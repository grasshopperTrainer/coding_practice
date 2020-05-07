from sys import stdin, setrecursionlimit

def solution(RN, CN, chart):
    setrecursionlimit(10000)
    NORECORD, DELTAS = -1, ((0, 1), (1, 0), (0, -1), (-1, 0))

    board = [[NORECORD for _ in range(CN)] for _ in range(RN)]
    board[RN-1][CN-1] = 1

    def search(x, y):
        if board[x][y] != NORECORD:
            return board[x][y]

        possibles = 0
        for dx, dy in DELTAS:
            nx, ny = x+dx, y+dy
            if 0 <= nx < RN and 0 <= ny < CN and chart[nx][ny] < chart[x][y]:
                possibles += search(nx, ny)
        board[x][y] = possibles
        return possibles

    return search(0, 0)


RN, CN, chart = 0, 0, []
for i,row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        RN, CN = row
    else:
        chart.append(row)

print(solution(RN, CN, chart))