from sys import stdin
from itertools import product
import heapq

def solution(board):
    empty = []
    row_empty, col_empty = [],[]
    for i in range(9):
        row_empty.append(sum(map(lambda x: x == 0, board[i])))
        col_empty.append(sum(map(lambda x: x == 0, [row[i] for row in board])))

    for x, y in product(range(9), repeat=2):
        if board[x][y] == 0:
            heapq.heappush(empty, (min([row_empty[x], col_empty[y]]), x, y))

    while empty:
        n, x, y = empty.pop(0)
        if n == 1:


    def fill(board, empty):
        pass

    return fill(board, empty)


board = []
for row in stdin.readlines():
    board.append([int(c) for c in row.strip().split(' ')])

print(solution(board))



