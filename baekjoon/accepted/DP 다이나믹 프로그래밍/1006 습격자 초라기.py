from sys import stdin


def solution(N, W, inner, outer):
    if N == 1:
        if inner[0] + outer[0] <= W:
            return 1
        return 2
    BOTH_PASSIVE, BOTH_ACTIVE, INNER_ACTIVE, OUTER_ACTIVE = 0, 1, 2, 3
    # description of end?
    dp_vert_passive = [[float('inf')] * 4 for _ in range(N)]
    dp_both_active = [[float('inf')] * 4 for _ in range(N)]
    dp_inner_active = [[float('inf')] * 4 for _ in range(N)]
    dp_outer_active = [[float('inf')] * 4 for _ in range(N)]
    dp_hori_passive = [[float('inf')] * 4 for _ in range(N)]

    dp_vert_passive[0][BOTH_PASSIVE] = 1 if inner[0] + outer[0] <= W else float('inf')
    dp_both_active[0][BOTH_ACTIVE] = 2
    dp_inner_active[0][INNER_ACTIVE] = 1 if outer[N - 1] + outer[0] <= W else float('inf')
    dp_outer_active[0][OUTER_ACTIVE] = 1 if inner[N - 1] + inner[0] <= W else float('inf')
    dp_hori_passive[0][BOTH_PASSIVE] = 2 if inner[N-1]+inner[0] <= W and outer[N-1]+outer[0] <= W else float('inf')

    for i in range(1, N):
        for state in range(4):
            for dp in (dp_vert_passive, dp_both_active, dp_inner_active, dp_outer_active, dp_hori_passive):
                if state == BOTH_PASSIVE:
                    if inner[i] + outer[i] <= W:
                        dp[i][BOTH_PASSIVE] = min(dp[i - 1]) + 1
                    if inner[i - 1] + inner[i] <= W and outer[i - 1] + outer[i] <= W:
                        dp[i][BOTH_PASSIVE] = min(dp[i][BOTH_PASSIVE], dp[i - 1][BOTH_ACTIVE])
                elif state == BOTH_ACTIVE:
                    dp[i][BOTH_ACTIVE] = min(dp[i - 1]) + 2
                elif state == INNER_ACTIVE:
                    if outer[i] + outer[i - 1] <= W:
                        dp[i][INNER_ACTIVE] = min(dp[i - 1][BOTH_ACTIVE], dp[i - 1][OUTER_ACTIVE]) + 1
                elif state == OUTER_ACTIVE:
                    if inner[i] + inner[i - 1] <= W:
                        dp[i][OUTER_ACTIVE] = min(dp[i - 1][BOTH_ACTIVE], dp[i - 1][INNER_ACTIVE]) + 1

    return min(min(dp_both_active[-1]),
               min(dp_vert_passive[-1]),
               min(dp_hori_passive[-2]),
               dp_inner_active[-1][BOTH_ACTIVE],
               dp_inner_active[-1][OUTER_ACTIVE],
               dp_outer_active[-1][BOTH_ACTIVE],
               dp_outer_active[-1][INNER_ACTIVE])


parser = lambda x: [int(c) for c in x.strip().split(' ')]
for _ in range(int(stdin.readline())):
    N, W = parser(stdin.readline())
    inner = parser(stdin.readline())
    outer = parser(stdin.readline())
    print(solution(N, W, inner, outer))

"""
2 
8 100 
70 60 55 43 57 60 44 50 
58 40 47 90 45 52 80 40 
5 120 
70 55 57 60 50 
47 90 45 52 80
"""
"""
4 
6 5 
1 5 1 1 1 1 
1 1 1 1 5 1 
12 5 
1 1 1 1 1 5 1 1 1 1 1 5 
1 1 5 1 1 5 1 1 5 1 1 5 
3 5 
1 4 1 
1 4 1 
4 5 
2 4 1 1 
3 1 4 3  
"""
"""
1
6 5 
1 5 1 1 1 1 
1 1 1 1 5 1 
"""
