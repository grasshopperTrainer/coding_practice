
def solution(N):

    fibo = {0: 1, 1: 1}
    def fibonacci(n):
        if n in fibo:
            return fibo[n]

        a, b = fibonacci(n-2), fibonacci(n-1)
        fibo[n] = (a + b + 1)%1_000_000_007
        return fibo[n]

    return fibonacci(N)


print(solution(int(input())))