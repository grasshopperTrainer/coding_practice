from sys import stdin


def solution(N, S, E, T, board):
    S, E = S-1, E-1
    dp = [[0]*N for _ in range(T+1)]
    dp[0][S] = 1
    for lead_t in range(T+1):
        for at in range(N):
            for come_from, drive_t in [(f, ts[at]) for f, ts in enumerate(board)]:
                if drive_t and lead_t - drive_t >= 0:
                    dp[lead_t][at] += dp[lead_t-drive_t][come_from]
            dp[lead_t][at] %= 1_000_003
    return dp[-1][E]


N, S, E, T = [int(c) for c in stdin.readline().strip().split(' ')]
board = [[int(c) for c in row.strip()] for row in stdin.readlines()]

print(solution(N, S, E, T, board))