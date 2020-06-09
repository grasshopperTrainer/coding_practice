from math import inf, isinf


def solution(N):
    # find min path
    dp = [inf]*(N+1)
    dp[N] = 0
    for n in range(N, 1, -1):
        if dp[n-1] >= 1 and dp[n-1] > dp[n]+1:
            dp[n-1] = dp[n]+1
        if n//2 >= 1 and n%2 == 0 and dp[n//2] > dp[n]+1:
            dp[n//2] = dp[n]+1
        if n//3 >= 1 and n%3 == 0 and dp[n//3] > dp[n]+1:
            dp[n//3] = dp[n]+1

    # track min path
    min_path = [1]
    while min_path[-1] != N:
        last = min_path[-1]
        for next_num in (last+1, last*2, last*3):
            if next_num <= N and dp[next_num] == dp[last] - 1:
                min_path.append(next_num)
                break   # cause only need one minimal path
    min_path.reverse()
    
    return min_path


min_path = solution(int(input()))
print(len(min_path))
print(' '.join([str(i) for i in min_path]))
