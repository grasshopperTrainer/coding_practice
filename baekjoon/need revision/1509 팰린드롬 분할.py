from sys import stdin, setrecursionlimit


setrecursionlimit(100_000)
def solution(chars):
    UNMARKED, L = float('inf'), len(chars)
    dp = [[UNMARKED] * L for _ in range(L)]
    counter = [0]
    def search(s, e):
        if dp[s][e] != UNMARKED:
            return dp[s][e]
        counter[0] += 1
        if s == e:
            dp[s][e] = 1
        elif s+1 == e:
            if chars[s] == chars[e]:
                dp[s][e] = 1
            else:
                dp[s][e] = 2
        else:
            if e - s > 1:
                for m in range(s, e):
                    dp[s][e] = min((dp[s][e], search(s, m) + search(m + 1, e)))
                if search(s + 1, e - 1) == 1:
                    if chars[s] == chars[e]:
                        dp[s][e] = 1
                    else:
                        dp[s][e] = min((dp[s][e], 3))

        return dp[s][e]

    search(0, L - 1)
    print(len(chars)**2)
    print(counter)
    return dp[0][-1]


print(solution(stdin.readline().strip()))