

def solution(N):
    if N < 10:
        return 0

    stair_dp = [[0]*10 for _ in range(N+1)]
    stair_dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for length in range(2, N+1):
        for end in range(10):
            if end != 0:
                stair_dp[length][end] += stair_dp[length-1][end-1]
            if end != 9:
                stair_dp[length][end] += stair_dp[length-1][end+1]
    stair_dp2 = [[0]*10 for _ in range(N+1)]
    stair_dp2[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for length in range(2, N+1):
        for end in range(10):
            if end != 0:
                stair_dp2[length][end] += stair_dp2[length-1][end-1]
            if end != 9:
                stair_dp2[length][end] += stair_dp2[length-1][end+1]
    # stair_dp2 = [0 for i in range(N+1)]
    # stair_dp2[10] = 1
    # for n in range(11, N+1):
    #     # from low to high
    #     for left_l in range(n-10):
    #         temp = 1
    #         if left_l != 0:
    #             temp *= stair_dp[left_l][1]
    #         for middle_l in range(n-left_l, N+1, 2):
    #             temp *= stair_dp[middle_l][9]
    #             temp *= stair_dp[n-middle_l-n][8]
    for row in stair_dp:
        print(row)
    print()
    for row in stair_dp2:
        print(row)
    # print(stair_dp2)
        # from high to low


print(solution(int(input())))