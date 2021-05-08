from sys import stdin
import heapq


def solution(N, M, board):
    EMPTY, WALL, KEYS, DOORS, AT, EXIT = '.', '#', set('abcdef'), set('ABCDEF'), '0', '1'
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)

    goals = set()
    at = None
    for x in range(N):
        for y in range(M):
            if board[x][y] == AT:
                at = x, y
            elif board[x][y] == EXIT:
                goals.add((x, y))

    moves = [(0, 0, *at)]  # move cnt, key possession, x, y
    record = [[[float('inf')] * 2 ** 6 for _ in range(M)] for _ in range(N)]  # key mask 'abcdef'
    while moves:
        cnt, keys, x, y = heapq.heappop(moves)
        if (x, y) in goals:
            return cnt

        if record[x][y][keys] <= cnt:
            continue
        record[x][y][keys] = cnt

        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != WALL:
                if board[nx][ny] in KEYS:  # new key get
                    new_keys = keys | (1 << (ord(board[nx][ny]) - ord('a')))
                    if cnt + 1 < record[nx][ny][new_keys]:
                        heapq.heappush(moves, (cnt + 1, new_keys, nx, ny))
                elif board[nx][ny] in DOORS:  # door open
                    if keys & (1 << (ord(board[nx][ny]) - ord('A'))):
                        if cnt + 1 < record[nx][ny][keys]:
                            heapq.heappush(moves, (cnt + 1, keys, nx, ny))
                else:  # empty or with AT sign
                    if cnt + 1 < record[nx][ny][keys]:
                        heapq.heappush(moves, (cnt + 1, keys, nx, ny))

    return -1


N, M = tuple(map(int, stdin.readline().strip().split(' ')))
board = [stdin.readline().strip() for _ in range(N)]
print(solution(N, M, board))
