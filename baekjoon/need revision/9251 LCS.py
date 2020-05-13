from sys import stdin


def solution(strings):
    N, M = map(lambda x: len(x), strings)

    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for x in range(1, M + 1):
        for y in range(1, N + 1):
            if strings[0][y - 1] == strings[1][x - 1]:
                dp[x][y] = dp[x - 1][y - 1] + 1
            else:
                dp[x][y] = max([dp[x - 1][y], dp[x][y - 1]])

    return dp[-1][-1]


strings = []
for row in stdin.readlines():
    strings.append(row.strip())

print(solution(strings))
