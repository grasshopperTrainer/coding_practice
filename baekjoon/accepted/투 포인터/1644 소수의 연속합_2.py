

def solution(N):
    # prepare prime
    primes = [True for i in range(N+1)]
    for num in range(2, N+1):
        if num:
            for multiple in range(num*2, N+1, num):
                primes[multiple] = False
    primes = [i for i in range(2, N+1) if primes[i]]
    NP = len(primes)
    # calc
    count = 0
    l, r = 0, 0
    sumv = 0
    while True:
        if sumv == N:
            count += 1
        if sumv <= N and r < NP:
            sumv += primes[r]
            r += 1
        elif l < NP:
            sumv -= primes[l]
            l += 1
        if NP == r and NP == l:
            break
    return count


print(solution(int(input())))