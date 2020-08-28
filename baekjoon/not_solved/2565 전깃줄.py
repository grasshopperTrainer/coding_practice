from sys import stdin


def solution(N, wires):
    M = 0
    a_b = {}
    b_a = {}
    for a, b in wires:
        a_b[a] = b
        b_a[b] = a
        M = max((M, a, b))

    dp = [[float('inf')]*(M+1) for _ in range(M+1)]
    dp[0][0] = 0
    print(a_b, b_a)
    for i in range(M+1):
        for j in range(M+1):
            if i == 0:
                if j in b_a:
                    dp[i][j] = min((dp[i][j], dp[i][j-1]+1))
                else:
                    dp[i][j] = min((dp[i][j], dp[i][j-1]))
            elif j == 0:
                if i in a_b:
                    dp[i][j] = min((dp[i][j], dp[i-1][j]+1))
                else:
                    dp[i][j] = min((dp[i][j], dp[i-1][j]))
            else:
                if j in b_a:
                    if b_a[j] == i:
                        dp[i][j] = min((dp[i][j], dp[i][j-1]))
                    else:
                        dp[i][j] = min((dp[i][j], dp[i][j-1]+1))
                else:
                    dp[i][j] = min((dp[i][j], dp[i][j-1]))
                if i in a_b:
                    if a_b[i] == j:
                        dp[i][j] = min((dp[i][j], dp[i-1][j]-1))
                    else:
                        dp[i][j] = min((dp[i][j], dp[i-1][j]+1))
                else:
                    dp[i][j] = min((dp[i][j], dp[i-1][j]))

    for row in dp:
        print(row)
    exit()


    pass


N, wires = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        wires.append([int(c) for c in row.strip().split(' ')])

print(solution(N, wires))