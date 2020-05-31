# didn't understand that starting position can be any place
from sys import stdin
from math import inf
from collections import deque


def solution(N, board):
    MAX = N**2-1
    record = inf
    for origin in range(N):
        que = deque([(origin, 2**origin, 0)])
        while que:
            pos_now, visited, money_spent = que.popleft()
            if visited == MAX and board[pos_now][origin] != 0:
                record = min([record, money_spent + board[pos_now][origin]])

            for go_next, cost in enumerate(board[pos_now]):
                next_visited = visited | 1 << go_next
                if visited != next_visited and cost != 0:
                    que.append((go_next, next_visited, money_spent+cost))

    return record


N = int(stdin.readline())
board = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N)]

print(solution(N, board))
