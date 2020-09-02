

def solution(N):
    dp = [float('inf') for _ in range(N+1)]
    dp[1] = 0
    for i in range(1, N+1):
        if i*3 <= N:
            dp[i*3] = min(dp[i*3], dp[i]+1)
        if i*2 <= N:
            dp[i*2] = min(dp[i*2], dp[i]+1)
        if i+1 <= N:
            dp[i+1] = min(dp[i+1], dp[i]+1)

    path = [N]
    i = N
    while i != 1:
        for j, sign in zip((i//3, i//2, i-1), (i%3, i%2, False)):
            if j <= N and (dp[j] == dp[i]-1) and not sign:
                i = j
                break
        path.append(i)
    return path


min_path = solution(int(input()))
print(len(min_path)-1)
print(' '.join([str(i) for i in min_path]))
