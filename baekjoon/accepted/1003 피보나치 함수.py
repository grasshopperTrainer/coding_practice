from sys import stdin

def solution(N):
    cache = {0:[1,0], 1:[0,1]}
    def fibo(N):
        if N in cache:
            return cache[N]

        result = list(map(lambda x,y: x+y, fibo(N-1), fibo(N-2)))
        cache[N] = result
        return result

    return fibo(N)


ns = []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        continue
    ns.append(int(row))

for n in ns:
    a, b = solution(n)
    print(f'{a} {b}')