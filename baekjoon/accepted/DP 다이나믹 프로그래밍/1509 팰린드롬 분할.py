from sys import stdin, setrecursionlimit


setrecursionlimit(100_000)
def solution(chars):
    L = len(chars)
    # dp all palindrome
    is_palin_dp = [[0]*L for _ in range(L)] # : is [end][start] palindrome
    for end in range(L):
        for start in range(end+1):
            # int ing just for better debugging
            if start == end:
                is_palin_dp[end][start] = 1
            elif start + 1 == end:    # adjacent pair case
                is_palin_dp[end][start] = int(chars[start] == chars[end])
            else:
                is_palin_dp[end][start] = int(is_palin_dp[end-1][start+1] and chars[start] == chars[end])
    # dp min palindrome subdivision
    dp = [None]*L  # : min num subdivision to [end]
    def search(end):
        # base condition : no letter to check
        if end == -1:
            return 0
        if dp[end] is not None:
            return dp[end]
        min_v = float('inf')
        for start in range(end+1):  # [end][end] is also len(1) palindrome so need to be checked
            if is_palin_dp[end][start]:
                min_v = min(min_v, search(start-1)+1)   # +1 for current start-end being a palindrome
        dp[end] = min_v
        return min_v
    return search(L-1)


print(solution(stdin.readline().strip()))