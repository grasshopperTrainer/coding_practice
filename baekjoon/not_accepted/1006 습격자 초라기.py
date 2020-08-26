from sys import stdin
from math import inf


def solution(N, W, enemies):
    # form enemy matrix
    enemies = [(a, b) for a, b in zip(enemies[:N], enemies[N:2 * N])]
    # MOBILE, SETTLED
    MM, MS, SM, SS = 0, 1, 2, 3

    def search_dp(idx):
        dp = [[inf] * 4 for _ in range(N)]
        dp[0][idx] = 0
        # search
        for col_idx in range(1, N):
            for status in range(4):
                prev_rec = dp[col_idx - 1]
                new_status = inf
                if status == MM:
                    new_status = min(prev_rec) + 2
                elif status == MS:
                    if enemies[col_idx][1]+enemies[col_idx-1][1] <= W:
                        new_status = min((prev_rec[MM], prev_rec[SM])) + 1
                elif status == SM:
                    if enemies[col_idx][0]+enemies[col_idx-1][0] <= W:
                        new_status = min((prev_rec[MM], prev_rec[MS])) + 1
                elif status == SS:
                    # new_status = inf
                    if all([a+b <= W for a, b in zip(enemies[col_idx], enemies[col_idx-1])]):
                        new_status = prev_rec[MM] + 0
                    if sum(enemies[col_idx]) <= W:
                        new_status = min((new_status, min(prev_rec)+1))
                dp[col_idx][status] = new_status
        # print(idx)
        # for row in dp:
        #     print(row)
        return dp[-1]

    minest = []
    result = search_dp(3)
    if all([a+b <= W for a,b in zip(enemies[0], enemies[-1])]):
        minest.append(min(result))
    else:
        minest.append(min(result)+2)
    if enemies[0][1] + enemies[-1][1] <= W:
        minest.append(min([x+1 if i in (0, 2) else inf for i, x in enumerate(search_dp(0))]))
    if enemies[0][0] + enemies[-1][0] <= W:
        minest.append(min([x+1 if i in (0, 1) else inf for i, x in enumerate(search_dp(0))]))
    if sum(enemies[0]) <= W:
        minest.append(min(search_dp(3))+1)
    return min(minest)


for _ in range(int(stdin.readline())):
    N, W = 0, 0
    enemies = []
    for i in range(3):
        row = [int(c) for c in stdin.readline().strip().split(' ')]
        if i == 0:
            N, W = row
        else:
            enemies += row
    print(solution(N, W, enemies))

"""
1
8 100
70 60 55 43 57 60 44 50
30 40 47 90 45 52 80 40
"""
"""
1
3 3
1 2 2
3 3 2
"""
"""
1
3 6
2 1 3
1 2 5
"""
# N, W, enemies = 8, 100, [70, 60, 55, 43, 57, 60, 44, 50, 58, 40, 47, 90, 45, 52, 80, 40]
# print(solution(N, W, enemies))
