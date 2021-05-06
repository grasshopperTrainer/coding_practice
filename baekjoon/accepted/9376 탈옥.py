from sys import stdin
import heapq


def solution(H, W, board):
    DELTA = ((-1, 0), (0, -1), (1, 0), (0, 1))
    SPACE, WALL, PRISONER, DOOR = '.*$#'

    board.insert(0, ['.'] * W)
    board.append(['.'] * W)
    for i, row in enumerate(board):
        board[i] = ['.'] + row + ['.']

    H, W = H + 2, W + 2
    prisoners = []
    for x in range(H):
        for y in range(W):
            if board[x][y] == PRISONER:
                prisoners.append((x, y))
                board[x][y] = 0

    def draw_cost_board(x, y):
        costs = [[float('inf')] * W for _ in range(H)]
        moves = [(0, x, y)]  # cost pos
        while moves:
            cost, x, y = heapq.heappop(moves)
            if costs[x][y] <= cost:
                continue
            costs[x][y] = cost

            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != WALL:
                    if board[nx][ny] == DOOR:
                        if cost + 1 < costs[nx][ny]:
                            heapq.heappush(moves, (cost + 1, nx, ny))
                    else:
                        if cost < costs[nx][ny]:
                            heapq.heappush(moves, (cost, nx, ny))
        return costs

    costs = [draw_cost_board(*pos) for pos in ((0, 0), *prisoners)]
    min_cost = float('inf')
    for x in range(H):
        for y in range(W):
            sum_cost = sum(cost[x][y] for cost in costs)
            if board[x][y] == DOOR:
                sum_cost -= 2
            min_cost = min(min_cost, sum_cost)

    return min_cost


for _ in range(int(stdin.readline())):
    H, W = map(int, stdin.readline().strip().split(' '))
    board = [list(stdin.readline().strip()) for _ in range(H)]
    print(solution(H, W, board))
