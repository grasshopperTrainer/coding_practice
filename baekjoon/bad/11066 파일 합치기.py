from sys import stdin

def solution(sizes):
    MAX, L = 10_000*500, len(sizes)
    NORECORD = -1
    dp = [[NORECORD]*L for _ in range(L)]
    sum_vs = [[NORECORD]*L for _ in range(L)]
    def sum_v(s, e):
        if e == -1:
            return 0
        if sum_vs[s][e] != NORECORD:
            return sum_vs[s][e]
        if s == e:
            sum_vs[s][e] = sizes[s]
            return sum_vs[s][e]

        sum_vs[s][e] = sum_v(s, e-1) + sizes[e]
        return sum_vs[s][e]

    def calc(s, e):
        if dp[s][e] != NORECORD:
            return dp[s][e]
        if s == e:
            dp[s][e] = 0
            return 0

        min_val = MAX
        part_sum = sum_v(s, e)
        for m in range(s, e):
            min_val = min([min_val, calc(s, m) + calc(m+1, e)])
        dp[s][e] = min_val + part_sum
        return dp[s][e]

    return calc(0, len(sizes)-1)


T, K, ss = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        T = int(row)
    elif i%2 == 0:
        ss.append([int(c) for c in row.strip().split(' ')])

for sizes in ss:
    print(solution(sizes))