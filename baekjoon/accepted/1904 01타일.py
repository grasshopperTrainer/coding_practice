def solution(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2

    a, b = 1, 2
    for i in range(2, N):
        a, b = b, (a + b)%15746
    return b

N = int(input())
print(solution(N))