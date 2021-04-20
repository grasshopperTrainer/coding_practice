from sys import stdin
import heapq


def solution(N, board):
    heap = [(-v, i, N-1) for i, v in enumerate(board[-1])]
    heapq.heapify(heap)

    for _ in range(N):
        val, y, x = heapq.heappop(heap)
        heapq.heappush(heap, (-board[x-1][y], y, x-1))
    return -val


N = int(stdin.readline())
board = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

print(solution(N, board))