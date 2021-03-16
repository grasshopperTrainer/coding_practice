from sys import stdin
import heapq


def solution(N, board):
    LENDIC = {c: i for i, c in enumerate(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), 1)}

    # calc total cable length
    length = 0
    for row in board:
        for c in row:
            if c == '0':
                continue
            length += LENDIC[c]

    # use only min cable
    for i in range(N):
        for j in range(N):
            if board[i][j] == '0':
                if board[j][i] != '0':
                    board[i][j] = board[j][i]
            elif board[j][i] == '0':
                if board[i][j] != '0':
                    board[j][i] = board[i][j]
            elif LENDIC[board[i][j]] < LENDIC[board[j][i]]:
                board[j][i] = board[i][j]
            else:
                board[i][j] = board[j][i]

    heap = [(0, 0)]
    visited = [False] * N
    while heap:
        c, at = heapq.heappop(heap)
        if visited[at]:
            continue
        visited[at] = True
        length -= c

        for goto, c in enumerate(board[at]):
            if c == '0':
                continue
            heapq.heappush(heap, (LENDIC[c], goto))

    if sum(visited) != N:
        return -1
    return length


N = int(stdin.readline())
board = [list(stdin.readline().strip()) for _ in range(N)]

print(solution(N, board))

"""
3
a00
0ef
0hi
"""
"""
3
faa
afa
aaf
"""