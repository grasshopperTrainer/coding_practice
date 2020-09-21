def solution(n):
    N = n * 2

    def dfs(comb, state):
        if len(comb) == N:
            if state == 0:
                return 1
            else:
                return 0
        if N - len(comb) < state:
            return 0
        total = dfs(comb + '(', state + 1)
        if state != 0:
            total += dfs(comb + ')', state - 1)
        return total

    return dfs('', 0)


print(solution(3))
