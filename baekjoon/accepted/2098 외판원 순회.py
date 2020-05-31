# there is not need to think of starting position
# it can be any arbitrary origin
from sys import stdin
from math import inf
from collections import deque


def solution(N, board):
    dp = [[inf]*N for _ in range(2**N)]
    # !KILLER CASE!
    # think of search starting at arbitrary position 0
    # if think of dp as visited positions where origin(0) not included, it starts with
    # dp[bitmask 0 meaning no other place visited][current position(0)] = cost(0)
    dp[0][0] = 0

    for state in range(2**N):   # as defined above start with 0
        for last_pos in range(N):
            for next_pos, cost in enumerate(board[last_pos]):
                if not cost:
                    continue
                next_state = state | (1 << next_pos)
                if state != next_state and dp[next_state][next_pos] > dp[state][last_pos] + cost:
                    dp[next_state][next_pos] = dp[state][last_pos] + cost

    # as dp started with [0][0]
    # dp['1'*N][0] already indicates min value coming back to 0 - arbitrary origin
    return dp[-1][0]


N = int(stdin.readline())
board = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N)]

print(solution(N, board))

"""
4
0 1 2 3
2 0 3 0
3 0 0 0
1 2 3 0
"""
"""
4
0 1 100 100
0 0 3 0
0 200 0 400
1 1 1 0
"""