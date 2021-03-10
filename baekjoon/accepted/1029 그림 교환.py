from sys import stdin


def solution(N, board):
    dp = [[[-1]*10 for _ in range(2**N)] for _ in range(N)]
    def dfs(owner, price, visited):
        if dp[owner][visited][price] != -1:
            return dp[owner][visited][price]

        max_count = bin(visited)[2:].count('1')
        for sell_to, buy_price in enumerate(board[owner]):
            if not visited & (1 << sell_to) and price <= buy_price:
                max_count = max(max_count, dfs(sell_to, buy_price, visited | 1 << sell_to))

        dp[owner][visited][price] = max_count
        return max_count

    visited = 1
    return dfs(0, 0, visited)


N = int(stdin.readline())
board = []
for _ in range(N):
    board.append([int(c) for c in stdin.readline().strip()])

print(solution(N, board))

"""
3
000
000
000
"""
"""
4
0123
3021
3304
5680
"""
"""
3
999
999
999
"""
"""
2
01
10
"""