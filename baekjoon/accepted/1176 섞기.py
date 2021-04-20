from sys import stdin


def solution(N, K, heights):
    heights.sort()
    print(heights)

    mask = 2**N-1
    dp = [[0]*(N) for _ in range(2**N)]
    for i in range(2**N):
        for j in range(N):
            if not (i & 1 << (j + 1)):
                continue
            height = heights[j]
            print(bin(i)[2:])
            for k, b in enumerate(bin(i)[2:], 1):
                if b == '1':

                    for l in range(j):
                        if height - heights[l] <= K:
                            break
                        dp[i][j] += dp[i ^ (1 << k)][l]
    for row in dp:
        print(row)


N, K = map(int, stdin.readline().strip().split(' '))
heights = [int(stdin.readline()) for _ in range(N)]

print(solution(N, K, heights))


"""
15 0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
"""
