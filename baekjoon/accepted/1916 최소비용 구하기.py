from sys import stdin
import heapq


def solution(N, M, buses, target):
    board = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for a, b, c in buses:
        board[a][b] = min(board[a][b], c)

    start, end = target
    moves = [(0, start)]
    record = [float('inf')]*(N+1)
    while moves:
        c, at = heapq.heappop(moves)
        if at == end:
            return c

        if record[at] <= c:
            continue
        record[at] = c

        for goto, cost in enumerate(board[at]):
            if goto != at and cost != float('inf') and c + cost < record[goto]:
                heapq.heappush(moves, (c + cost, goto))


N = int(stdin.readline())
M = int(stdin.readline())
buses = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(M)]
target = tuple(map(int, stdin.readline().strip().split(' ')))
print(solution(N, M, buses, target))
